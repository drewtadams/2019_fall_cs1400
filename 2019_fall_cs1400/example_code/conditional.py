from random import randint


def guess():
    rand_int = randint(1,10)
    
    while True:
        user_input = int(input('Guess a number between 1 and 10: '))
        if user_input > rand_int:
            print('>')
        elif user_input < rand_int:
            print('<')
        else:
            print('nailed it')
            break



def main():
    score = int(input('enter your score: '))
    
    if score > 89:
        print('A')
    elif score > 79:
        print('B')
    elif score > 69:
        print('C')
    else:
        print('F')
        
    print('foobar')
    
    
    if score > 89 and score <= 100:
        print('A student')
    elif score > 79 or score < 70:
        print('ya failed')
        
        
    my_bool = False
    not_my_bool = not my_bool
    print(not_my_bool)
    
    val_a = False
    val_b = True
    if(val_a and val_b):
        print('yup')
        
    some_val = 7
    while some_val > -1:
        some_val -= 1
        
        if some_val > 5:
            break
        print(f'some_val: {some_val}')
        
    while False:
        pass # do something
    
    input_val = 0
    while input_val <= 1 or input_val >= 10:
        input_val = int(input('Enter a number between 1 and 10: '))
    
    if input_val == 4:
        print(input_val)
        print(f'rand int is {randint(1,10)}')
        
    for roll in range(10):
        print(randint(1,100))
    
        
if __name__ == '__main__':
    #main()
    guess()