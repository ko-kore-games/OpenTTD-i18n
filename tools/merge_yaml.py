
import sys
import yaml
import os.path as path

def convert(base_file, patch_file):
    with open(base_file, 'r') as f:
        base_data = yaml.safe_load(f.read())
    with open(patch_file, 'r') as f:
        patch_data = yaml.safe_load(f.read())

    out_data = {}
    for key in base_data['weblate'].keys():
        if key in patch_data['weblate']:
            out_data[key] = patch_data['weblate'][key]
        else:
            out_data[key] = ""
    result = yaml.safe_dump(out_data, default_flow_style=False, allow_unicode=True)
    return result

def main():
    if len(sys.argv) < 3:
        print('Usage: python %s <base_file> <patch_file>' % sys.argv[0])
        sys.exit(1)

    base_file = sys.argv[1]
    patch_file = sys.argv[2]
    if not path.exists(base_file):
        print('File %s does not exist' % base_file)
        sys.exit(1)
    if not path.exists(patch_file):
        print('File %s does not exist' % patch_file)
        sys.exit(1)

    print(convert(base_file, patch_file))

if __name__ == '__main__':
    main()
