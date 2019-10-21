
def my_sum(x,y):
    return x + y


def main():
    my_list = ['foo', 'bar', 1, 2, 3, 4, 5.0, [1, 2, '3', [4.5, 1, 2, '3'], 5]]
    my_other_list = [{
        'name': 'drew',
        'age': 1000
    }]
    my_empty_list = []
    my_empty_list.append(5)
    
    print(my_empty_list)
    
    my_list[1] = 'shtuff'

    print( my_list[1] )
    print( my_list[7][3][3] )
    
    print( my_other_list[0].get('name') )
    
    my_dict = {
        'name': 'foo',
        'age': 25,
        0: 50
    }
    print(my_dict[0])
    print(my_dict.get('age'))
    print(my_dict.get(0))
    
    
    shop_one = ['mtg cards', 'dnd book']
    shop_two = ['lettuce', 'cabbage']
    
    shopping_dict = {
        'game shop': shop_one,
        'walmart': shop_two
    }
    
    sums = [my_sum(1,2), my_sum(3,4), my_sum(5,6), my_sum(7,8)]
    sums[2] = ''
    
    print(f'sums: {sums}')
    
    range_l = list(range(100))
    print(f'r: {range_l}')
    print(range(100))
    
    ret_list = []
    for val in range(100):
        ret_list.append(val)
        
    print(ret_list)
    print(len(ret_list))
    print(ret_list + list('foobar'))
    
    print(list('foobar'))
    
    list_one = [1, 2, 3, 4, 5]
    list_two = [5, 4, 3, 2, 1]
    print(list_one == list_two)
    
    print(f'my list of sums: {[my_sum(1,2)]}')
    
    x = 'foo'
    y = 'bar'
    
    x += 'bar'
    z = x + y
    print(z)
    
    a = list(z)
    a[3] = 3
    print(a)
    
    print('foo bar jib jab'.split())


if __name__ == '__main__':
    main()