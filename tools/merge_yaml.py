
import sys
import yaml
import os.path as path

def convert(type, base_file, patch_file):
    with open(base_file, 'r') as f:
        base_data = yaml.safe_load(f.read())
    with open(patch_file, 'r') as f:
        patch_data = yaml.safe_load(f.read())

    result = {}
    for key in base_data[type].keys():
        if key in patch_data[type]:
            result[key] = patch_data[type][key]
        else:
            result[key] = ''
    return result

def main():
    if len(sys.argv) < 3:
        print('Usage: python %s <base_file> <patch_file>' % sys.argv[0])
        sys.exit(1)

    base_file, patch_file = sys.argv[1:]
    if not path.exists(base_file):
        print('File %s does not exist' % base_file)
        sys.exit(1)
    if not path.exists(patch_file):
        print('File %s does not exist' % patch_file)
        sys.exit(1)

    result = {
        'base': convert('base', base_file, patch_file),
        'extra': convert('extra', base_file, patch_file),
    }

    result = yaml.safe_dump(result, allow_unicode=True, width=float('inf'))
    print(result)

if __name__ == '__main__':
    main()
