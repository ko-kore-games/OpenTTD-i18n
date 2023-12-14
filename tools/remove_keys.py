
import sys
import yaml
import os.path as path

def convert(data):
    data = yaml.safe_load(data)
    result = ["''" if d == '' else d for d in data.values()]
    result = '\n\n'.join(result) + '\n'
    return result

def main():
    if len(sys.argv) < 2:
        print('Usage: python %s <path to file>' % sys.argv[0])
        sys.exit(1)

    path_to_file = sys.argv[1]
    if not path.exists(path_to_file):
        print('File %s does not exist' % path_to_file)
        sys.exit(1)

    with open(path_to_file, 'r') as f:
        data = f.read()

    print(convert(data))

if __name__ == '__main__':
    main()
