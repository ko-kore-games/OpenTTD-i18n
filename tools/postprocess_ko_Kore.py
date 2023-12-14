
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

def convert_all(data):
    return {key: convert(value) for key, value in data.items()}

def convert(str):
    return reduce(lambda acc, rep: replace_punctuations(acc, rep[0], rep[1]), replacements, str)

def replace_punctuations(acc, src, dst):
    result = []
    brace_depth = 0
    for c in acc:
        if c == '{':
            brace_depth += 1
        elif c == '}':
            brace_depth -= 1
        if brace_depth == 0 and c == src:
            result.append(dst)
        else:
            result.append(c)
    return ''.join(result)

def postprocess(data):
    return {
        'base': convert_all(data['base']),
        'extra': convert_all(data['extra']),
    }

def main(args):
    if len(args) < 1:
        print('Usage: python %s <input yaml>' % sys.argv[0])
        sys.exit(1)
    with open(args[0], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    data = postprocess(data)
    result = yaml.safe_dump(data, sort_keys=False, default_flow_style=False, allow_unicode=True, width=float('inf'))
    print(result)

if __name__ == '__main__':
    main(sys.argv[1:])
