import sys


def main():
    print(f'\n\tnumber of arguments: {len(sys.argv)}')
    print(f'\targuments: {sys.argv}\n')
    
    sys.argv = ['cmd_line_args.py', 'foobar', '24']
    if len(sys.argv) > 1:
        x = sys.argv[1]
    else:
        x = 10
        
    y = 20
    
    print(str(x+y))


if __name__ == '__main__':
    main()