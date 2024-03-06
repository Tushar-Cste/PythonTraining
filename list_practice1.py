# Write a program to find the largest number in a list

number_list = [20, 40, 15, 100, 35]
largest_num = number_list[0]
for item in number_list[1:5]:
    if item > largest_num:
        largest_num = item
print(f'Largest number from the list is {largest_num}')
