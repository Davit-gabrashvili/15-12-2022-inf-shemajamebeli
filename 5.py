from math import tan, pi
n=eval(input("enter the number of sides"))
a=eval(input("Enter the side: "))
area=(n * a ** 2)/ (4 * tan(pi/n))
print(f"The area of the polygon is {area}")