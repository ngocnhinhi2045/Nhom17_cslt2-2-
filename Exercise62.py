print('Original price---Discount---New price')
n = (4.95, 9.95, 14.95, 19.95, 24.95)
for i in n:
    discount = i * 0.6
    new_price = i - discount
    print('   $', i, '---------', '$', round(discount, 2), '--------$', round(new_price, 2), sep="")
