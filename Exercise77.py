binary_number = input('Enter a binary number: ')
decimal_number = 0
for i in range(len(binary_number)):
    digit = int(binary_number[i])
    decimal_number += digit * 2**(len(binary_number)-i-1)
print("The equivalent decimal number is", decimal_number)