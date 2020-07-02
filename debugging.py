# debugging
# # linting
# # idde/editors (often come with some static debugging built in)
# # READ THE ERROR
# # pdb - pythong debugger 

# pdb

## pdb.set_trace:
#### opens an interactive environment in the terminal
#### typing `help` will show you available commands
#### typing `help command_name` will show you documentation about a partivular commnad
###### step is really useful
#### can also change variables while in pdb environment to test things out

import pdb

def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

add(4, 5)