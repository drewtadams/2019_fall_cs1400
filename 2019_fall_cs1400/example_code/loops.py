# import math
# import math as m
from math import *


def main():
    for x in range(1,11,2):
        print(x)
    
    x = ('-')*10
    print(f'{x}')
    
    x = 0
    y = False
    while x != 10:
        print(x)
        x += 1
        
        if x == 10:
            pass
        
        #if x == 10:
        #    x += 1
    
    x = 'foobar'
    for letter in x:
        print(letter, end='')
        print('')
        
    x = [1,2,3,4,5,6]
    for item in x:
        print(item)
        
    x = list(range(10))
    print(x)
    
    
    x = range(10,-1,-1)
    for value in x:
        print(value)
        
    print('\n\n\n')
        
    for foo in range(10):
        print('%-3d|%10d|%10d' % (foo, 10**foo, foo*2))
        
    for x in range(10):
        val = x * pi
        print('your salary is $%0.2f' % val)
        
    x = float(input('enter some int: '))
    print(x)
    if x == 1:
        print('done')
    elif x == 2:
        print('bar')
    else:
        print('foo')


if __name__ == '__main__':
    main()