#Write a function that takes a list value as an argument and returns
#a string with all the items separated by a comma and a space, with and
#inserted before the last item. For example, passing the previous spam list to
#the function would return 'apples, bananas, tofu, and cats'. But your function
#should be able to work with any list value passed to it.

a, b, c, d, e = raw_input().split()

list = [a, b, c, d, e]

print (list[0]+", " + list[1]+", " + list [2]+", " + list[3]+" " + "and" +" "+ list[4])
