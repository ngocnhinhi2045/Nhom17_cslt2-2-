import re
string = input("")
string = re.sub(r'\W+', '', string.lower())
is_palindrome = string == string[::-1]
is_single_word = string.count(' ') == 0

if is_palindrome and not is_single_word:
    print("Palindrome.")
else:
    print("Not palindrome.")