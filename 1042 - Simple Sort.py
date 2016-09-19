#ead three integers and sort them in ascending order.
# After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.

x, y, z = map(int, raw_input().split())

test = [x, y, z]
n = sorted(test)
print n[0]
print n[1]
print n[2]
print ""
print test[0]
print test[1]
print test[2]
