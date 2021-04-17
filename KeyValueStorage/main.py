import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="it's key name in our storage")
parser.add_argument("--val", help="it's value")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
data = {}
if args.key and args.val:
    if os.path.exists(storage_path):
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        with open(storage_path, 'r') as f:
            if os.path.getsize(storage_path) > 0:
                data = json.load(f)

        with open(storage_path, 'w') as f:
            if args.key in data:
                for key, value in data.items():
                    if key == args.key:
                        value.append(args.val)
            else:
                data[args.key] = [args.val]
            json.dump(data, f)
    else:
        path = tempfile.gettempdir()
        path = path + '/storage.data'
        file = open(path, 'w')
        data[args.key] = [args.val]
        json.dump(data, file)
        file.close()

elif args.key:
    if os.path.exists(storage_path):
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        with open(storage_path, 'r') as f:
            if os.path.getsize(storage_path) > 0:
                data = json.load(f)
        with open(storage_path, 'w') as f:
            if data and (args.key in data):
                print(", ".join(data[args.key]))
            json.dump(data, f)
    else:
        print(None)


""" 
#Masters code
import argparse
import json
import os
import tempfile

def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def write_data(storage_path, data):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    return parser.parse_args()


def put(storage_path, key, value):
    data = read_data(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)


def get(storage_path, key):
    data = read_data(storage_path)
    return data.get(key, [])


def main(storage_path):
    args = parse()

    if args.key and args.val:
        put(storage_path, args.key, args.val)
    elif args.key:
        print(*get(storage_path, args.key), sep=', ')
    else:
        print('The program is called with invalid parameters.')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
"""

