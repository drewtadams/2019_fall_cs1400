# set variable for our multiplier (we may want to change this in the future, who knows)
multiplier = 10

# we need to store the input and convert it to an integer, otherwise we see some funky stuff from mult_age
age = int(input('what\'s your age? '))

# multiply the age input by our multiplier
mult_age = age * multiplier

# this is one way to set up our print string - see the second print statement below
print_str = 'your age multiplied by ' + str(multiplier) + ' is ' + str(mult_age) + ' years old'

"""
three different ways to print out our string to the console - note that they all display the exact
same message but are structured differently. the method you choose is based on your program and
what you're trying to do with it, but for this program, the last example is the one you would want
to use.
"""
print('your age multiplied by ' + str(multiplier) + ' is ' + str(mult_age) + ' years old')
print(print_str)
print(f'your age multiplied by {multiplier} is {mult_age} years old')