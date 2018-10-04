#!/usr/local/bin/python3
import sys
from numpy import *
import re

def parse_arg(name, default=None):
    prefix = '--{}='.format(name)
    arg = list(filter(lambda arg: arg.startswith(prefix), sys.argv[1:]))
    return arg[0][len(prefix):] if arg else default

def gen_x(lo, hi):
    diff = hi - lo
    return random.rand(15) * diff + lo

if __name__ == '__main__':
    rg = parse_arg('range', default='(-10,10)')
    lines = int(parse_arg('lines', default='100'))
    out = parse_arg('out', default='out.txt')
    expr = parse_arg('expr', default='sum(X)')
    lo, hi = map(float, re.findall('-?\d+(?:\.\d*)?', rg))
    sep = parse_arg('sep', default=',')
    with open(out, 'w') as f:
        for i in range(lines):
            X = gen_x(lo, hi)
            y = eval(expr)
            nums = append(X, [y])
            f.write(sep.join(map(str, nums)) + '\r\n')
