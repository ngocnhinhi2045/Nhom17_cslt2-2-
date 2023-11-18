total_price = 0
while True:
    age = input("Enter customer's age: ")
    if age == "":
        break
    age = int(age)
    if age <= 2:
        price = 0
    elif 2 < age <= 12:
        price = 14
    elif age >= 65:
        price = 18
    else:
        price = 23
    total_price += price
#print('Total ticket price =','$','%.2f' % total_price)   
print('Total ticket price =','$',round(total_price,2))   
