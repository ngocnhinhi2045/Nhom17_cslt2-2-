s = input('Enter a string: ')
x = ''
for i in s:
    x = i + x
if x == s:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
