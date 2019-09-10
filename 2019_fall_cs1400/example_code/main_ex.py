import math


def count(start=1, end=10):
    for x in range(start, end, 5):
        print(x)
        break
        
    y = 5
    while y <= 10:
        print('still true', end=' ')
        y += 1
        
    print('\\nthe end', end=' ')


def main():
    print('hello world')
    
    x = 4/3
    y = x * math.pi
    print(str(y))
    
    count(1, 100)


if __name__ == '__main__':
    main()