#Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:

A, B, C = raw_input().split()
A = int(A)
B = int(B)
C = int(C)
MAIORAB= (A+B+abs(A-B))/2
MAIORC = (MAIORAB+C+abs(MAIORAB-C))/2
print "%d eh o maior" % MAIORC
