# coding=utf-8
##Make a program that reads three floating point values: A, B and C. Then, calculate and show:
# a) the area of the rectangled triangle that has base A and height C.
# b) the area of the radiuss circle C. (pi = 3.14159)
# c) the area of the trapezium which has A and B by base, and C by height.
# d) the area of ​​the square that has side B
# e) the area of the rectangle that has sides A and B.

A, B, C = raw_input().split()
A = float(A)
B = float(B)
C = float(C)
print "TRIANGULO: %.3f" % ((A*C)/2)
print "CIRCULO: %.3f" % (3.14159*C**2)
print "TRAPEZIO: %.3f" % ((A+B)*C/2)
print "QUADRADO: %.3f" % (B**2)
print "RETANGULO: %.3f" % (A*B)
