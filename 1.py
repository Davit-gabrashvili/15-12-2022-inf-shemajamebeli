import math 

radius = eval(input("enter length")) 

a = 2 * radius * math.sin(math.pi / 5)
area = round((3 * 3 ** 0.5)/2 * a ** 2, 2)


print("area is", area)