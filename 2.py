from cmath import cos
from math import radians, sin, cos, acos

radius = 6371.01

point1 = eval(input("Enter point 1 (latitude and longitude) in degrees:"))
point2 = eval(input("Enter point 2 (latitude and longitude) in degrees:"))

x1, y1 = point1
x2, y2 = point2

x1=radians(x1)
y1=radians(y1)

x2=radians(x2)
y2=radians(y2)

distance = radius * acos(sin ( x1 ) * sin ( x2 ) + cos( x1 ) * cos( x2 ) * cos( y1 - y2 ))

print("The distance between the two points is {d} km".format(d = str(distance)))