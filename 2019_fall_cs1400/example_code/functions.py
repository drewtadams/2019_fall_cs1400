import random


def get_rando_number_list(num_iterations):
    ret_list = []
    for x in range(0,num_iterations):
        ret_list.append(random.randint(1,10))
    
    return ret_list


def get_num_dictionary(list_size, start_iter=0, end_iter=5):
    cur_dict = {}
    for val in range(start_iter, end_iter+1):
        cur_dict[val] = get_rando_number_list(list_size)
    
    return cur_dict


def get_list():
    return [1, 2, 3, 4, 5]


def sum_list(a_list):
    cur_val = 0
    for x in a_list:
        cur_val += x
        
    return cur_val


def main():
#    y = [6, 7, 8, 9, 0]
    
#    print(sum_list(get_list()))
#    print(sum_list(y))
    print(get_num_dictionary(3))
    


if __name__ == '__main__':
    main()