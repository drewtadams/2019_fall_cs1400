
def main():
    write_file = open('./some_file', 'w')
    write_file.write('1,2,3\n4,5,6\n7,8,9')
    write_file.close()
    
    master_list = []
    read_file = open('some_file', 'r')
    for line in read_file:
        master_list += line.strip().split(',')
        
    cur_index = 0
    while cur_index < len(master_list):
        master_list[cur_index] = int(master_list[cur_index])
        cur_index += 1
            
    # master_list += my_list
    # for val in my_list:
    #    master_list.append(int(val))
    print(master_list)
    read_file.close()


if __name__ == '__main__':
    main()