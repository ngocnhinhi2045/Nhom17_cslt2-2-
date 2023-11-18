import math
x1 = float(input("Enter the x part of the coordinate: "))
y1 = float(input("Enter the y part of the coordinate: "))
x2 = input("Enter the x part of the coordinate (blank to quit): ")
perimeter = 0
while x2 != "":
    x2 = float(x2)
    y2 = float(input("Enter the y part of the coordinate: "))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    perimeter += distance
    x1 = x2
    y1 = y2
    x2 = input("Enter the x part of the coordinate (blank to quit): ")
distance = math.sqrt((x1 - 0) ** 2 + (y1 - 0) ** 2)
perimeter += distance
print("The perimeter of that polygon is", perimeter)
