
# entry function to the program
def main():
    info = {}
    info['Name'] = 'sam'
    info['age'] = 20
    info['occupation'] = 'young doctor'
    info['occupation'] = 'floutist'
    
    if 'last_name' in info:
        last_name = info['last_name']
    else:
        info['last_name'] = 'jordan'
        
    info.pop('age')
    
    print(info)
    
    for k in info:
        print(k,info[k])
      
    print('\n')
    for (key,value) in info.items():
        print(f'{key}: {value}')
        
    print(f'info: {len(info)}')
        
    dictionary_list = list(info.items())
    print(dictionary_list)
    
    print(dictionary_list[1][1])
    
    my_keys = list(info.keys())
    my_keys.sort(reverse=True)
    print(my_keys)
    
    s_l = [1,3,2,4,7,5,6]
    s_l.sort(reverse=True)
    print(s_l)
    
    divider = '-'*50
    print(f'\n{divider}\n')
    
    my_nums = [101, 3, 5, 7, 9, 11, 33, 100]
    my_nums.sort()
    
    middle = len(my_nums) // 2
    if len(my_nums) % 2 == 0:
        median = (my_nums[middle-1] + my_nums[middle]) / 2
        print(median)
    else:
        print(my_nums[middle])
        
    
    


if __name__ == '__main__':
    main()
    