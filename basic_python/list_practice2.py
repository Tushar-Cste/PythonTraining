# Write a program to remove the duplicate number from list without using second list

num_list = [10, 20, 10, 10, 40, 30, 30, 40, 10, 60]

for item in num_list:
    if num_list.count(item) > 1:
        index = num_list.index(item)
        for item_index in range(index+1, len(num_list)):
            if len(num_list) > item_index and num_list[item_index] == item :
                num_list.pop(item_index)
            elif len(num_list) <= item_index:
                break
print(num_list)