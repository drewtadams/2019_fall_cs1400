full_str = 'hello world'
substr = 'hello'
my_list = [1,2,3,4,5,6,7,8,9,0]

val = input('enter an int')

print(len(full_str))
print(len(my_list))

print(full_str[6])
print(full_str[6:11])

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
print(f'last in lorem: "{lorem_ipsum[-1]}"')

print(lorem_ipsum[::-2])

x = len(lorem_ipsum)
while x >= 0:
    x -= 1
#    print(lorem_ipsum[x])
    
for i in range(len(lorem_ipsum)):
#    print('%-3d: ' % (i), end='')
#    print(f'{lorem_ipsum[i]}')
    pass
    
for i in range(10):
#    print(i)
    pass
    
#print(full_str[:len(full_str)])



data = 'fname lname age'
age = (data[-1:-4:-1])[::-1]

print(f'age: {age}')


my_list = [1,2,3,4,5,6,7,8,'9',0]
print(my_list[4])
if 9 in my_list:
    print("there's a 9")
else:
    print('no 9')


if 'hello' in full_str:
    print('hello exists')
else:
    print('no hello')
    

