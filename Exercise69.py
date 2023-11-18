approximation = 0
denominator = 2
sign = 1
for _ in range(15):
    term = 4 / (denominator * (denominator + 1) * (denominator + 2))
    approximation += sign * term
    denominator += 2
    sign *= -1
    print("Approximation of π:", 3 + approximation)