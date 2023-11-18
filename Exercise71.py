epsilon = 0.00001
number = float(input())
guess = number / 2

while True:
    difference = guess**2 - number
    if abs(difference) <= epsilon:
        break
    guess = (guess + number/guess) / 2

print("Square root of", number, "is:", guess)