
import sys
import yaml
import os.path as path

def convert_line(line):
    entries = line.split(':')
    if len(entries) < 2:
        return None
    key = entries[0].strip()
    value = ':'.join(entries[1:]).strip()
    return (key, value)

def convert(data):
    lines = data.split('\n')
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line != '' and line[0]!= '#']
    lines = [convert_line(line) for line in lines]
    lines = [line for line in lines if line is not None]
    dict = {key: value for key, value in lines}
    content = {'weblate': dict,}
    result = yaml.dump(content, allow_unicode=True, width=float('inf'))
    return result

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 %s <path to file>' % sys.argv[0])
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
