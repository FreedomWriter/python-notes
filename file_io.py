# FILE  I/O
# # stands for input / output
# # python has a built in fuction that allows us to open and write to files: `open`

# # with open('file_name.txt', mode="r")
# # # defaults to read mode
# # changing mode from mode="r" to mode="r+" allows a file to be written to as well as read

try:
    with open('test.txt', mode='r+') as my_file:
        # print(my_file.read())
        # # the read method reads files by a cursor. The first read will put the cursor at the end of the file so additional calls to .read() will print blank lines because there is nothing after the cursors current position to read
        # print(my_file.read())
        # print(my_file.read())

        # # to "read" the file a second time, the .seek() method must be called. .seek() expects an index to be passed to it and will place the cursor immediately before the specified index

        # my_file.seek(15)
        # print(my_file.read())
        # my_file.seek(0)
        # print(my_file.read())
        # print('\n')

        # .readline()
        ## will read file line by line from top to bottom.


        # print(my_file.readline())
        # # # invoking .readline() multiple times will move to the next line for each invocation
        # print(my_file.readline())
        # print(my_file.readline())

        # .readlines() - NOTE LINES IS PLURAL
        # # returns a list where each line is an item in the list (including \n)
        # print(my_file.readlines())

        # WRITING TO FILES
        # ## when in 'r+' (read and write) mode my_file.write("Look Ma, I'm writing to files!!!") will replace the first 32 chaaracters (because the string is 32 characters long) with the text
        # ## when in 'a' (for append) mode, my_file.write() will append the given text to the end of the last line in the file (will not add spaces or a new line)
        # ## using mode='w' will overwrite whatever is in the file
        text = my_file.write("Look Ma, I'm writing to files!!!")
        print(text) # prints the character count for text
        # print(my_file.readlines())
except FileNotFoundError as err:
        print('file does not exist')
        raise err
except IOError as err:
        print('io error') 
        raise err

# To close the file - good practice
## Only necessary not using with open('relative or absolute file path') as file_variable:
## so the import would look like:
## #my_file = open('test.txt')
## would make .close() necessary at the end of the file
# my_file.close()

# using 'write' mode will also create a file if one doesn't exist
with open('sad.txt', mode='w') as sad_file:
    sad_text = sad_file.write(":(")

# NEW PATH BUILT IN MODULE
# # pathlib
# # helps make sure that windows and unix machines can read the file paths
# # https://docs.python.org/3/library/pathlib.html#module-pathlib