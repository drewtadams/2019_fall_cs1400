# define the sum_nums function - don't forget the colon and indentation!
def sum_nums(num_one, num_two):
    num_one = 1 + num_one
    return num_one + num_two


def print_rando_stuff():
    foobar = str("foobar")
    my_var = "foobar"
    another_var = ("foobar")
    m_var = 'foobar'

    # this is a multiline string
    x = """
    Lorem Ipsum is simply dummy
    text of the printing and typesetting.
    Lorem Ipsum has been the industry's standard dummy text ever since
    the 1500s, when an unknown printer took a galley of type and scrambled
    it to make a type specimen book. It has survived not only five centuries,
    but also the leap into electronic typesetting, remaining essentially unchanged.
    """

    # note that x is being reassigned here, so the lorem ipsum is never printed
    x = 'what\'s up\n    not much'  # escaping single quote, newline
    y = 'foo\tbar\nf\tb'            # tabs and newlines
    z = '\\'                        # escaping the backslash

    # print our variables
    print(foobar)
    print(my_var)
    print(another_var)
    print(m_var)
    print(x)
    print(y)
    print(z)


def print_rando_sums():
    # ask for a number
    first_num = int(input('give me a number: '))

    # ask for another number
    second_num = int(input('give me another number: '))

    # add previous numbers together
    num_sum = first_num + second_num

    # display results 3 different ways
    print('1. the sum of your two numbers is ' + str(num_sum))
    print('2. the sum of your two numbers is', num_sum)		# note there is no space after 'is' because one is automatically inserted when passing num_sum as a parameter
    print(f'3. the sum of your two numbers is {num_sum}')

    # print the string value of the sum of 13 and 777
    print(str(sum_nums(13, 777)))

    # pass a function call (sum_nums) as a parameter
    sum_one = sum_nums(12, 23)
    sum_two = sum_nums(sum_one, sum_nums(34, 45))
    print(sum_two)


def main():
    # call to the print_rando_stuff function
    print_rando_stuff()

    # call to the print_rando_sums function
    print_rando_sums()

    print('\n\t -- finished --\n')


# if this file is the one being run in python, call the main function
if __name__ == '__main__':
    main()