#Take an input of phone number
# Output should be text value of those number
# If there is other character without number we should ignore
# Suppose phone number is 1234
# Output should be One Two Three Four



phone_num = input('Phone: ')
out_text = ''
num_key = {
    '0' : 'Zero',
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Nine'
}

print(num_key.get('a'))


for index in range(len(phone_num)):
    if index > 0:
        out_text += ' '
    val = num_key.get(phone_num[index])
    if val is not None:
        out_text += val
print(out_text)