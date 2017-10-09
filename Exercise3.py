print "The sum of the squares of the first hundred natural numbers is "
sum_squared_num = 0
sum_squared = 0

for i in range(101):
    sum_squared_num = sum_squared_num + i**2
    sum_squared = (sum_squared + i)

sum_squared = sum_squared **2
difference = sum_squared - sum_squared_num

print (difference)
