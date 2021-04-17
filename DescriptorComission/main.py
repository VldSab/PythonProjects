class Value:
    def __init__(self):
        self.value = None

    def __get__(self, instance, value):
        return self.value

    def __set__(self, instance, value):
        self.value = value - instance.commission * value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


def _main():
    new_account = Account(0.1)
    new_account.amount = 100
    print(new_account.amount)


if __name__ == '__main__':
    _main()

