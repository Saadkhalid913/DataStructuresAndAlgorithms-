import math


def func(x: float):
    '''
    define however you want, input: float, rtype: float  
    '''
    return x ** 2


def RiemannSum(a: float, b: float, f, dx: float):
    s = 0
    while a < b:
        s += f(a)
        a += dx
    return s * dx


print(RiemannSum(0, 5, func, 0.0001))
