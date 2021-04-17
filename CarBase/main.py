import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)
        return ext[-1]

    car_types = ['car', 'truck', 'spec_machine']


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count=None):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
    car_type = CarBase.car_types[0]


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl = None):
        super().__init__(brand, photo_file_name, carrying)
        parameters = body_whl.split('x')
        #по условию должно быть передано не больше трех параметров
        if len(parameters) > 3:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0
        else:
        #отлавливаем неправильные значения для параметров трака
            try:
                if len(parameters) > 0:
                    self.body_length = float(parameters[0])
                else:
                    self.body_length = 0.0
            except (ValueError, TypeError):
                self.body_length = 0.0
            try:
                if len(parameters) > 1:
                    self.body_width = float(parameters[1])
                else:
                    self.body_width = 0.0
            except (ValueError, TypeError):
                self.body_width = 0.0
            try:
                if len(parameters) > 2:
                    self.body_height = float(parameters[2])
                else:
                    self.body_height = 0.0
            except (ValueError, TypeError):
                self.body_height = 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

    car_type = CarBase.car_types[1]


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    car_type = CarBase.car_types[2]


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                #проверяем обязательные параметры на пустоту
                if len(row) < 6 or row[0] is None or row[1] is None or row[3] is None or row[5] is None:
                    continue
                #проверяем на правильность значения car_type, тип фотографии и на пустоту extras
                elif check_car_type(row[0]) and check_photo_name(row[3]) and is_brand_exist(row[1]) \
                        and check_exstras(row):
                    put_in_list(row, car_list)
                else:
                    continue
            except (ValueError, TypeError):
                continue
    return car_list


def check_car_type(car_type):
    types = ['car', 'truck', 'spec_machine']
    total = True if car_type in types else False
    return total


def check_photo_name(photo_name):
    names = ['.jpg', '.jpeg', '.png', '.gif']
    total = True if os.path.splitext(photo_name)[-1] in names else False
    return total


def check_exstras(row):
    if row[0] == 'spec_machine' and row[-1] == '':
        return False
    else:
        return True


#проверяем brand на пустоту
def is_brand_exist(brand):
    total = True if brand else False
    return total


def put_in_list(row, car_list):
    if row[0] == 'car':
        car = Car(row[1], row[3], row[5], row[2])
        car_list.append(car)
    elif row[0] == 'truck':
        truck = Truck(row[1], row[3], row[5], row[4])
        car_list.append(truck)
    elif row[0] == 'spec_machine':
        spec_machine = SpecMachine(row[1], row[3], row[5], row[6])
        car_list.append(spec_machine)


def _main():
    pass


if __name__ == '__main__':
    _main()

