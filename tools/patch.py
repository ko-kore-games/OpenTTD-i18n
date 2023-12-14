
import sys
import yaml
import os.path as path

def apply(type, base_file, diff_file):
    with open(base_file, 'r') as f:
        base_data = yaml.safe_load(f.read())
    with open(diff_file, 'r') as f:
        diff_data = yaml.safe_load(f.read())

    base = base_data[type]
    diff = diff_data[type]

    result = {}
    keys = [*base.keys(), *diff.keys()]
    for key in keys:
        if key in base and key in diff:
            if diff[key] is None:
                continue
            else:
                result[key] = None
        elif key in base and key not in diff:
            result[key] = base[key]
        elif key not in base and key in diff:
            result[key] = diff[key]
    return result

def main():
    if len(sys.argv) < 3:
        print('Usage: python %s <base_file> <diff_file>' % sys.argv[0])
        sys.exit(1)

    base_file, diff_file = sys.argv[1:]
    if not path.exists(base_file):
        print('File %s does not exist' % base_file)
        sys.exit(1)
    if not path.exists(diff_file):
        print('File %s does not exist' % diff_file)
        sys.exit(1)

    result = {
        'base': apply('base', base_file, diff_file),
        'extra': apply('extra', base_file, diff_file),
    }

    result = yaml.safe_dump(result, sort_keys=False, default_flow_style=False, allow_unicode=True, width=float('inf'))
    print(result)

if __name__ == '__main__':
    main()
