import socket
import time


class ClientError(Exception):
    def __init__(self):
        super().__init__()


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((self.host, self.port))

    def get(self, ask):
        try:
            ask = 'get ' + ask + '\n'
            self.sock.send(ask.encode('utf-8'))
            data = self.sock.recv(1024).decode('utf-8')
            result = InputCorrector.check(data)
            result = InputCorrector.to_map(result)
            return result
        except ClientError:
            print('Wrong in Get')

    def put(self, metric, numeric, my_time=None):
        my_time = my_time if my_time else int(time.time())
        putter = 'put {} {} {}\n'.format(metric, numeric, my_time)
        try:
            self.sock.send(putter.encode('utf-8'))
            data = self.sock.recv(1024).decode('utf-8')
            result = InputCorrector.check(data)
            result = InputCorrector.to_map(result)
            return data
        except ClientError:
            print('Something wrong')


class InputCorrector:
    def __init__(self, string):
        self.string = string

    @staticmethod
    def check(string):
        splitter = '\n'
        new_list = string.split(splitter)
        return new_list

    @staticmethod
    def to_map(new_list):
        new_map = {}
        if new_list == '' or new_list is None or new_list[0] != 'ok':
            raise ClientError
        new_list.pop(0)
        new_list = [element for element in new_list if element != '' and element]
        for i in new_list:
            tmp = i.split()

            try:
                params = tmp[1:]
            except ClientError:
                print('Out of index')
                break

            params.reverse()
            try:
                params[0] = int(params[0])
                params[1] = float(params[1])
            except ClientError:
                print('Incorrect type')
                break
                
            if tmp[0] not in new_map:
                new_map[tmp[0]] = [tuple(params)]
            else:
                for key, value in new_map.items():
                    if key == tmp[0]:
                        value.append(tuple(params))
            return new_map
        else:
            return {}


def _main():
    client = Client("127.0.0.1", 8889, timeout=15)
    print(client.get("*"))


if __name__ == '__main__':
    _main()
