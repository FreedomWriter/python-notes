STRINGS
Can print a long string by beginning with 3 single quotes and ending with 3 single quotes
long_string = '''
WOW
O O
---
'''
print(f'\n# Can print a long string by beginning with 3 single quotes and ending with 3 single quotes, respects hard returns (\ n or other methods were not used to create line breaks)\n\nAn example:   \n\n {long_string}')
print(f'')

username = 'supercoder'
password = 'supersecret'

first_name = 'Natalie'
last_name = 'Davis'
full_name = first_name + ' ' + last_name
print(f"first_name = 'Natalie'\nlast_name = 'Davis'\nfull_name = first_name + ' ' + last_name   \n# prints: {full_name}")

# STRING TYPE CONVERSION
## print(type(str(100))) # evaluates to <class 'str'>
print('# STRING TYPE CONVERSION')
print(f"\ntype(str(100))   \n# prints: <class 'str'>")

# CONCATENATION - can only concatonate strings 'hello' + 5 will error out
print("\n# CONCATENATION - can only concatonate strings 'hello' + 5 will error out")
print(f"\nhowever, print('Hello' + ' Natalie')   \n# prints: {'Hello' + ' Natalie'}")

# ESCAPE SEQUENCE - use a backslash - signifies whatever comes after the \ is a string\# \t will add a tab
# \n will add a new line
print(f'\n# ESCAPE SEQUENCE - use a backslash - signifies whatever comes after the \ is a string')

weather_example = "It\'s \"kind of\" sunny"
print(f'\nvalue stored at weather_example:   \n# prints: {weather_example}')
print(f'\n\# \ t will add a tab\n# \ n will add a new line (spaces added between the \ and the respective letter in order to allow it to print)')


print('\n############################################################################################\n')


#FORMATTED STRINGS
# add an `f` before the quotes in a string and use {} for variables

print(f'\n#FORMATTED STRINGS\n# add an `f` before the quotes in a string and use curly brackets for variables')

name = "Natalie"
age = 40

print('Hi ' + name + '. You are ' + str(age) + ' years old. - using concatination') 

print(f'Hi {name}. You are {age} years old. - using "f"') 


print('\n############################################################################################\n')


# METHOD .format()
print('\n# METHOD .format()')
print("'Hi {}. You are {} years old.'.format('Natalie', '40') ")
print('# prints: Hi {}. You are {} years old.'.format('Natalie', '40') )
print("'Hi {}. You are {} years old.'.format(name, age)")
print('# prints: Hi {}. You are {} years old.'.format(name, age) )
print("'Hi {1}. You are {0} years old.'.format(name, age) - variable indexes")
print('# prints: Hi {1}. You are {0} years old.'.format(age,name) )
print("'Hi {new_name}. You are {new_age} years old.'.format(new_name='Ms. Natalie', new_age=50) - assigning a new value to the variables")
print('# prints: Hi {new_name}. You are {new_age} years old.'.format(new_name="Ms. Natalie", new_age=50) )


print('\n############################################################################################\n')


# String Indexes

selfish = "me me me" #01234567
selfish_number = "01234567"

print(f'# when selfish = "me me me"\nselfish[0] evaluates to "{selfish[0]}"\n' )

# when we use [] the first item is the `start` we can use a colon `:` and then add a `stop` [start:stop]

print(f'# selfish[0:1] evaluates to "{selfish[0:2]}" when selfish = "me me me"\n' )

# to get entire string give the value of the length of the string to 'stop'

print(f'# To get the entire string, provide the length of the string to "stop", so selfish[0:8] evaluates to {selfish[0:8]} where selfish = "me me me"\n')

# can provide a 'start' value followed by a colon `:` with no stop value to begin at a certain point and continue to the end of the string

print(f'# providing a start value with no end value will begin at the given start point and end at the end of the string, so selfish_number[3:] will evaluate to "{selfish_number[3:]}" where selfish_number = "01234567"\n')

# can provide a 'stop' value preceded by a colon `:` with no start value to begin at a 0 and continue to the provided value [:3]

print(f'# providing a stop value with no start value will begin at 0 and end at the given stop value, so selfish[:3] will evaluate to "{selfish_number[:3]}" where selfish_number = "01234567"\n')

# can add a thrid thing called a `stepover` - [start:stop:stepover] which says start here, end here and step over 'n' times. stepover defaluts to 1

print(f'# selfish[0:8:3] evaluates to "{selfish[0:8:3]}" when selfish = "me me me"\n' )

# [::2] - no "start", no "stop"

print(f'# selfish_number[::2] evaluates to "{selfish_number[::2]}" where selfish_number = "01234567"\n')

# [-'value'] means start at the end of the string and move back the provied value

print(f'# selfish_number[-2] evaluates to "{selfish_number[-2]}" where selfish_number = "01234567"\n')

# combining this knowledge makes reversing a string pretty simple in python - [::-1]

print(f'# selfish_number[::-1] evaluates to "{selfish_number[::-1]}" where selfish_number = "0123456". This a simple way to reverse a string\n')

# [start:stop:stepover] is referred to as slicing


print('\n############################################################################################\n')


Immutability
strings are immutable in that you cannot do something like selfish[0] ="8", though you can reassing the value of selfish like this selfish = "new string" or selfish = selfish + "new string to add to existing balue of selfish"

print(f' # STRINGS are IMMUTABLE\n # You cannot do something like selfish[0] ="8"\n # You can reassign the value of selfish like this:\n \n   selfish = "new string"\n \n# Or\n \n    selfish = selfish + "new string to add to existing value of selfish"')


print('\n############################################################################################\n')
