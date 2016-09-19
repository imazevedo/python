#Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four decimal places after the comma, according to the formula:

import math


x1, y1 = raw_input().split()

x1 = float(x1)
y1 = float(y1)

x2, y2 = raw_input().split()

x2 = float(x2)
y2 = float(y2)


distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print "%.4f" % distance

