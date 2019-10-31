from functools import *


'''
lambda <arg1, arg2, ... argn>: <expression>
'''


def my_reduce(xfunc, xlist):
    x = 0
    for val in xlist:
        x = xfunc(val,x)
    return x


def my_map(xfunc, xlist):
    x = []
    for val in xlist:
        x.append(xfunc(val))
    return x


def my_filter(xfunc, xlist):
    x = []
    for val in xlist:
        if xfunc(val):
            x.append(val)
    return x


def opposite(x):
    return x * -1


def odd(x):
    return x % 2 == 1


def add(a,b):
    return a+b


def main():
    div = '-'*35
    o = opposite
    
    print(f'o: {o(5)}')
    
    
    x = 6
    if x > 5:
        y = 1
        
    y = 2.1
    y = 'foobar'
    print(y)
    
    print(f'\n{div}\n')
    
    items1 = ['1', '2', '3', '4', '-5']
    items2 = [-1, 2, -3, 4, -5]
    items = list(my_map(opposite, items2))
    print(items2)
    print(items)
    
    print(f'\n{div}\n')
    
    odds = [2, 4, 6, 8, 0]
    print('my_list:')
    print(list(my_filter(odd, odds)))
    
    print(f'\n{div}\n')
    
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(my_reduce(add, nums))
    
    print(f'\n{div}\n')
    
    print('lambda: ', end='')
    print(reduce(lambda x,y: x + y, nums))
    # print(list(map(lambda , items1)))
    # print(list(filter(lambda , items1)))
    
    print(f'\n{div}\n')
    
    print(1 is True)
    
    


if __name__ == '__main__':
    main()