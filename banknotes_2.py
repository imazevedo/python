val = int(raw_input())
values = [100, 50, 20, 10, 5, 2, 1]


while not int(val) in range(1,1000000):
    val = input()#choose a shift


print val
for v in values:
    print '%d nota(s) de R$ %d,00' % (val / v, v)
    val = val % v

