import sys


def add(a,b):
    return a+b


def subtract(a,b):
    return a-b


def main():
    print(f'args: {len(sys.argv)}')
    print(f'args: {sys.argv}')

    jump_table = {}
    jump_table['1'] = add
    jump_table['2'] = subtract

    print(jump_table)

    if len(sys.argv) > 1:
        user_in = sys.argv[1]
    else:
        user_in = input('Would you like to add (1) or subtract (2)? ')
        
    if len(sys.argv) > 2:
        first_int = int(sys.argv[2])
    else:
        first_int = int(input('first val: '))
        
    if len(sys.argv) > 3:
        sec_int = int(sys.argv[3])
    else:
        sec_int = int(input('second val: '))

    if user_in in jump_table:
        print(jump_table[user_in](first_int, sec_int))
    
    
if __name__ == '__main__':
    main()