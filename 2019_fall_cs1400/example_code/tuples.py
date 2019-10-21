
def m_sum(val_one, val_two):
    return val_one + val_two


def you_win():
    print('you\'re a winner')
    
    
def odd(val):
    return val % 2 == 1

def even(val):
    return val % 2 == 0
    
    
    



"""
purpose: use to help explain tuples
"""
def main():
    t = (1,2,3)
    
    print(m_sum(1,2))
    
    print(f'{1 + m_sum(1,2)}')
    
    is_even = not odd(5)
    print(is_even)
    
    if even(6) or odd(4):
        pass
    
    x = ()
    print(x)
    
    d = { 'foo': 'bar' }
    print(d.get('foo'))
    d['foo'] = 1
    print(d)
    
    
    


if __name__ == '__main__':
    main()