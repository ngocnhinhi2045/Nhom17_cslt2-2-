n = input('Enter an 8-bit string: ')
while n != '':
    if n.count('0') + n.count('1') != 8 or len(n) != 8:
        print('Invalid bit string')
    else:
        num_ones = n.count('1')
        if num_ones % 2 == 0:
            print('Even parity bit is 0')
        else:
            print('Even parity bit is 1')
    n = input('Enter an 8-bit string: ')
