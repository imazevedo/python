#Read 3 floating-point numbers. After, print the roots of bhaskaras formula.
# If its impossible to calculate the roots because a division by zero or a square root of a negative number,
# presents the message "Impossivel calcular"
import math
A, B, C = map(float, raw_input().split())
if A == 0:
    print "Impossivel calcular"
else:
    delta = B**2 - 4*A*C
    if delta < 0:
        print "Impossivel calcular"
    else:
        R1 = (-B + math.sqrt(delta))/(2*A)
        R2 = (-B - math.sqrt(delta))/(2*A)
        print "R1 = %.5f" % R1
        print "R2 = %.5f" % R2
