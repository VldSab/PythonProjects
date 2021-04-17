import os
import tempfile
import random
import string


class File:
    def __init__(self, file_path):
        if os.path.exists(file_path):
            self.file_path = file_path
            self._counter = 0
        else:
            with open(file_path, 'w') as f:
                self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, 'r') as f:
                file = f.read()
            return file
        except FileNotFoundError:
            return ''

    def write(self, text):
        try:
            with open(self.file_path, 'w') as f:
                f.write(text)
        except FileNotFoundError:
            print("File not found")

    def __add__(self, other):
        sample = "".join(random.choices(string.ascii_lowercase, k=10))
        with open(os.path.join(tempfile.gettempdir(), sample), 'w') as f:
            f.write(self.read() + other.read())
            new_file = File(os.path.join(tempfile.gettempdir(), sample))
        return new_file

    def __str__(self):
        return os.path.abspath(self.file_path)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            if self._counter < len(lines):
                result = lines[self._counter]
                self._counter += 1
                return result
            else:
                self._counter = 0
                raise StopIteration


def _main():
    path_to_file = 'some_filename'
    print(os.path.exists(path_to_file))

    file_obj = File(path_to_file)
    print(os.path.exists(path_to_file))

    file_obj.write('some text')
    print(file_obj.read())
    file_obj.write('other text')
    print(file_obj.read())
    file_obj_1 = File(path_to_file + '_1')
    file_obj_2 = File(path_to_file + '_2')
    file_obj_1.write('line 1\n')
    file_obj_2.write('line 2\n')
    new_file_obj = file_obj_1 + file_obj_2
    print(isinstance(new_file_obj, File))
    print(new_file_obj)
    for line in new_file_obj:
        print(ascii(line))


if __name__ == '__main__':
    _main()
