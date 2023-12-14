
import sys
import yaml
from functools import reduce

replacements = [
    [' ', ''],
    ['...', '…'],
    ['..', '‥'],
    ['.', '。'],
    [',', '、'],
    ['?', '？'],
    ['!', '！'],
    [':', '：'],
    [';', '；'],
]

def convert_updated(updated):
    return reduce(lambda acc, rep: replace_punctuations(acc, rep[0], rep[1]), replacements, updated)

def replace_punctuations(acc, src, dst):
    if len(src) > 1:
        return acc.replace(src, dst)
    result = []
    brace_level = 0
    for c in acc:
        if c == '{':
            brace_level += 1
        elif c == '}':
            brace_level -= 1
        if brace_level == 0 and c == src:
            result.append(dst)
        else:
            result.append(c)
    return result

def postprocess(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    data = convert_updated(data['weblate'])
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, default_flow_style=False)

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print('Usage: python3 %s <input yaml> <output yaml>' % sys.argv[0])
        sys.exit(1)
    input_file, output_file = args
    postprocess(input_file, output_file)

if __name__ == '__main__':
    main()
