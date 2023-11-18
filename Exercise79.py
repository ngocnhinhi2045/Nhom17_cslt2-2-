from random import randint
num_integers = 100
max_integer = randint(1, num_integers)
print(max_integer)
num_updates = 0
for i in range(num_integers - 1):
    current_integer = randint(1, num_integers)
    if current_integer > max_integer:
        max_integer = current_integer
        num_updates += 1
        print(current_integer, '<= Update')
    else:
        print(current_integer)
print('The maximum integer found was', max_integer)
print('The maximum integer was updated', num_updates, 'times')
