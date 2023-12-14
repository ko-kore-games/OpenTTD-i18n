
import sys
import yaml
import os.path as path

# A script to generate diff between original files

def diff(type, old_file, new_file):
    with open(old_file, 'r') as f:
        old_data = yaml.safe_load(f.read())
    with open(new_file, 'r') as f:
        new_data = yaml.safe_load(f.read())

    old = old_data[type]
    new = new_data[type]

    result = {}
    keys = [*old.keys(), *new.keys()]
    for key in keys:
        if key in old and key in new:
            if old[key] != new[key]:
                result[key] = new[key]
        elif key in old and key not in new:
            result[key] = None
        elif key not in old and key in new:
            result[key] = new[key]
    return result

def main():
    if len(sys.argv) < 3:
        print('Usage: python %s <old_file> <new_file>' % sys.argv[0])
        sys.exit(1)

    old_file, new_file = sys.argv[1:]
    if not path.exists(old_file):
        print('File %s does not exist' % old_file)
        sys.exit(1)
    if not path.exists(new_file):
        print('File %s does not exist' % new_file)
        sys.exit(1)

    result = {
        'base': diff('base', old_file, new_file),
        'extra': diff('extra', old_file, new_file),
    }

    result = yaml.safe_dump(result, sort_keys=False, default_flow_style=False, allow_unicode=True, width=float('inf'))
    print(result)

if __name__ == '__main__':
    main()
