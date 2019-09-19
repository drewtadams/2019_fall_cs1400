import os


print(os.getcwd())

def write_to_file():
    #f = open('lorem.txt', 'w')
    #f.write('look at me I\'m cool')
    #f.close()
    
    f = open('lorem.txt', 'r')
    print(f.read())
    


def main():
    some_str = 'peanut butter'
    print(len(some_str))
    
    some_dig = '100'
    print( some_str.isdigit() )
    print( some_dig.isdigit() )
    
    x = 'my cat is a dog'
    split_x = x.split(' ')
    print(split_x)
    
    data = 'drew adams 20 123 some place else'
    split_data = data.split(' ')
    first_name = split_data[0]
    last_name =  split_data[1]
    address = split_data[3::]
    print(first_name)
    for item in split_data[3::]:
        print(item, end=' ')
        
    age = data.split(' ')[2]
    print(f'\n{age}')


if __name__ == '__main__':
#    main()
    write_to_file()