
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
    return dict

def main():
    if len(sys.argv) != 3:
        print('Usage: python %s <base> <extra>' % sys.argv[0])
        sys.exit(1)

    base, extra = sys.argv[1:]

    if not path.exists(base):
        print('File %s does not exist' % base)
        sys.exit(1)
    if not path.exists(extra):
        print('File %s does not exist' % extra)
        sys.exit(1)

    with open(base, 'r') as f:
        base_data = f.read()
    
    with open(extra, 'r') as f:
        extra_data = f.read()

    base_data = convert(base_data)
    extra_data = convert(extra_data)
    data = {
        'base': base_data,
        'extra': extra_data,
    }

    result = yaml.dump(data, sort_keys=False, default_flow_style=False, allow_unicode=True, width=float('inf'))
    print(result)

if __name__ == '__main__':
    main()
