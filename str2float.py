# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    DIGITAL = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7': 7, '8': 8, '9': 9}
    s1, s2 = s.split('.')
    s2 = [s2[len(s2)-1-x] for x in range(len(s2))]
    def s2n(s):
        return DIGITAL[s]
    def fn1(n1, n2):
        return n1*10+n2
    def fn2(n1, n2):
        return 0.1*n1+n2
    return reduce(fn1, map(s2n, s1))+reduce(fn2, map(s2n, s2))*0.1
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
