# remove duplicate numbers using multiple list

numbers = [10, 20, 30, 10, 20, 10, 40]
uniques = []

for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)

