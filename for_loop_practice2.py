# Create a F in the following format using nested for loop
#       xxxxx
#       xx
#       xxxxx
#       xx
#       xx

numbers = [5, 2, 5, 2, 2]

for item in numbers:
    str = ''
    for itr in range(item):
        str += 'X'
    print(str)
            

