# conditions
# if name is less than 3 charaters long print the following message:
# name must be at least 3 characters
# if it's more than 50 characters long print the following message:
# name can be a maximum of 50 characters
# otherwise print the following message:
# name looks good!

name = input('Enter your name: ')
name_len = len(name)
if name_len < 3:
    print('Name must be at least 3 characters')
elif name_len > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good!')