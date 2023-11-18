total = 0
while True:
    price = input('Price of item: ')
    if price == '':
        break
    else:
        price = float(price)
    total += price
    total_cents = round(total * 100)
    remainder = total_cents % 5
    if remainder == 0:
        total_cents_to_pay = total_cents
    elif remainder < 2.5:
        total_cents_to_pay = total_cents - remainder
    else:
        total_cents_to_pay = total_cents + (5 - remainder)
print('Total cost: $', total)
print('Cash payment amount: $', total_cents_to_pay / 100)
