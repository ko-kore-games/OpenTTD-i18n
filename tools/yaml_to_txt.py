
import sys
import yaml
import os.path as path

def get_key(line):
    key = line.split(':')[0]
    return key

def convert_line(line, updated):
    key = get_key(line)
    stripped = key.strip()
    if stripped in updated:
        return '%s:%s' % (key, updated[stripped])
    else:
        return line

def convert(type, base, updated):
    lines = base.split('\n')
    lines = [convert_line(line, updated[type]) if line != '' and line[0] != '#' else line for line in lines]
    result = '\n'.join(lines)
    return result

def main():
    if len(sys.argv) < 3:
        print('Usage: python %s <type> <base txt file> <updated yaml file>' % sys.argv[0])
        sys.exit(1)

    type, base_file, updated_file = sys.argv[1:]
    if not path.exists(base_file):
        print('File %s does not exist' % base_file)
        sys.exit(1)

    if not path.exists(updated_file):
        print('File %s does not exist' % updated_file)
        sys.exit(1)

    with open(base_file, 'r') as f:
        base = f.read()
    with open(updated_file, 'r') as f:
        updated = yaml.load(f, Loader=yaml.FullLoader)

    result = convert(type, base, updated)
    print(result)

if __name__ == '__main__':
    main()
