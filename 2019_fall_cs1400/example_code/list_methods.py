
def search(mlist, mval):
    for val in mlist:
        if val == mval:
            return True
    return False

def good_search(mlist, mval):
    return mval in mlist


def main():
    l = [3,2,1]
    a_list = [4,5,6]
    print(l+a_list)
    l.extend(a_list)
    
    l.insert(2, 999)
    print(l)
    
    print(l.pop())
    print(l)
    
    print(l.pop(2))
    print(l)
    
    sep = '-'*50
    print(sep)
    
    print(f'found: {999 in l}')
    
    l.sort()
    print(l)
    
    print(l.sort())
    l.sort(reverse=True)
    print(l)

    print(sep)
    x_list = [1,2,3]
    y_list = []
    for item in x_list:
        y_list.append(item)
        
    y_list.append(4)
    print(x_list)
    print(y_list)
    
    print(sep)
    x = [1,2,3]
    y = x
    print(f'y id: {id(y)}, x id: {id(x)}')
    print(f'y is x: {x is y}')
    print(f'y == x: {x == y}')
    y = [1,2,3]
    print(f'y is x: {x is y}')
    print(f'y == x: {x == y}')
    print(f'y id: {id(y)}, x id: {id(x)}')

if __name__ == '__main__':
    main()