# FIRST GUI

#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
  for pixel in row:
    if(pixel == 1):
      print("*", end = "") # passing "" to end overides the default end which is a new line
    else:
      print(' ', end = "")
  print('') # need a new line after every row

fill = '$'
empty = ' '

for line in picture:
  for pixel in line:
    if(pixel):
      print(fill, end = "") # passing "" to end overides the default end which is a new line
    else:
      print(empty, end = "")
  print('') # need a new line after every row

# VANILLA CHECK DUPLICATES (does use built in method .count())

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)

print('\n############################################################################################\n')