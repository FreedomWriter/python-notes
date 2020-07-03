# reg ex module

import re

string = 'search inside of this text please!'

# re.search(pattern, string, flags)

a = re.search('this', string) # prints a Match object, which also gives a span of the index of occurance

# will_error returns None
## trying .group() on a NOne value will error out
will_error= re.search('tasdklfj', string)
# print(will_error.group())

print(a.span())
print(a.start())
print(a.end())
# when we need to do multiple seaches .group() is really useful
print(a.group())
# reg ex module

# establishing a pattern

pattern = re.compile('this')
full_match_pattern = re.compile('search this inside of this text please!'
)
match_pattern = re.compile('search this ')
string = 'search this inside of this text please!'
full_match_pattern = re.compile('search this inside of this text please!'
)
pattern_search = pattern.search(string)

find_all = pattern.findall(string)
will_error= pattern.search(string)
full_match = pattern.fullmatch(string)
full_match_true = full_match_pattern.fullmatch(string)
match_method = match_pattern.match(string)

print(pattern_search.span())
print(pattern_search.start())
print(pattern_search.end())
print(find_all)
# prints None since the string provided isn't a full match for the string we are checking against
print(full_match)
# prints a Match object since it is a full match
print(full_match_true)
# prints match because we don't require a FULL match - .match() doesnt' care what comes after it's match, does care aobut before
print(match_method)

email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email_string = 'new@email.test'
email = email_pattern.search(email_string)
print(email)

# Password checker
## at least 8 characters
## letters, numbers, $%#@

def main(): 
    password = 'Geeky1y@1'
    reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$%#@])[A-Za-z\d@$!#%*?&]{8,20}$"
      
    # compiling regex 
    password_pattern = re.compile(reg) 
      
    # searching regex                  
    password_match = re.fullmatch(password_pattern, password) 
      
    # validating conditions 
    if password_match: 
        print("Password is valid.") 
    else: 
        print("Password invalid !!") 
  
# Driver Code      
if __name__ == '__main__': 
    main()