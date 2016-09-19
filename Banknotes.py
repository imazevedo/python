#finding the minimum notes

shift = input()
while not int(shift) in range(1,1000000):
    shift = input()#choose a shift

notas_100 = shift/100
notas_50 = (shift-notas_100*100)/50
notas_20 = (shift-notas_100*100 - notas_50*50)/20
notas_10 = (shift-notas_100*100 - notas_50*50-notas_20*20)/10
notas_5 = (shift-notas_100*100 - notas_50*50-notas_20*20-notas_10*10)/5
notas_2 = (shift-notas_100*100 - notas_50*50-notas_20*20-notas_10*10-notas_5*5)/2
nota_1 = (shift-notas_100*100 - notas_50*50-notas_20*20-notas_10*10-notas_5*5-notas_2*2)

print shift
print "%d nota(s) de R$ 100,00" % notas_100
print "%d nota(s) de R$ 50,00" % notas_50
print "%d nota(s) de R$ 20,00" % notas_20
print "%d nota(s) de R$ 10,00" % notas_10
print "%d nota(s) de R$ 5,00" % notas_5
print "%d nota(s) de R$ 2,00" % notas_2
print "%d nota(s) de R$ 1,00" % nota_1
