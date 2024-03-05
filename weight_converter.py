# weight conversion
#Take weight input from the user
# Take the unit of Weight L/l for pounds and K/k for Kilos
# If unit is pounds the output should be shown into kilos
# Output: You are x kilos
# If unit is kilos the output should be shown into pounds
# Output: You are x pounds
# If unit is invalid
# Output: Invalid weight unit

 
weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.lower() == 'k':
    converter_weight = int(weight) * 2.205
    print(f'You are {converter_weight} pounds')
elif unit.lower() == 'l':
    converter_weight = int(weight) * 0.45
    print(f'You are {converter_weight} kg')
else:
    print('Invalid weight unit')