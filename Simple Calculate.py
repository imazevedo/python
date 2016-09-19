#in this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

prod_code, unit_numbers, unit_price = raw_input().split()
prod_code2, unit_numbers2, unit_price2 = raw_input().split()

prod_code = int(prod_code)
unit_numbers = int(unit_numbers)
unit_price = float(unit_price)


prod_code2 = int(prod_code2)
unit_numbers2 = int(unit_numbers2)
unit_price2 = float(unit_price2)

print "VALOR A PAGAR: R$ %.2f" % (unit_numbers*unit_price + unit_numbers2*unit_price2)
