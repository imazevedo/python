money = input()

notes = [100, 50, 20, 10, 5, 2]
coins = ["1.00", "0.50", "0.25", "0.10", "0.05", "0.01"]
cents = [100, 50, 25, 10, 5, 1]

print "NOTAS:"
for v in notes:
    print "%d nota(s) de R$ %d.00" % (money/v, v)
    money = money % v

print "MOEDAS:"
money = money * 100
x = 0
for n in cents:
    print "%d moeda(s) de R$ %s" % (money/cents[x], coins[x])
    money %= n
    x = x + 1
