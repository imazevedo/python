X, Y = map(int, raw_input().split())

itens = {1:4,2:4.5,3:5,4:2,5:1.5}

if X in itens:
   itens[X] = itens[X] * Y
print ("Total: R$ %.2f") % itens[X]
