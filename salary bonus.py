#Make a program that reads a seller name, his/her fixed salary and the sale total made by himself/herself in the month (in money). Considering that this seller receives 15% over all products sold, write the final salary (total) of this seller at the end of the month , with two decimal places.


seller = raw_input()
fix_sal = input()
total_sales = input()

#15% over total sales

print ("TOTAL = R$ %.2f") % (total_sales*0.15+fix_sal)
