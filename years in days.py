#insert your age in days to know the year, month and days

day = input()

year = day / 365

day = day % 365 # returns the remainder "35"

month = day / 30

day = day % 30

print "%d ano(s)" % year
print "%d mes(es)" % month
print "%d dia(s)" % day
