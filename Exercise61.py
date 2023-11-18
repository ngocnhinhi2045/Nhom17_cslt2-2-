count = 0
total = 0
print('Enter values:')
while True:
    n = int(input())
    if n == 0:
        if count == 0:
            print('ERROR')
            break
        else: 
            average = total / count
            print('Average =', average)
            break
    count += 1
    total += n
