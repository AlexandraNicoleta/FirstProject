print "Hello"
print "This is a calculator that sums up the multiples of 3 and 5 of the numbers below 1000."
number = raw_input("Please choose a number: ")
sum = 0
ans = 0
while ans == 0:
    for i in range(int(number)):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    print sum
    j = raw_input("Do you want to continue? 1 for YES   0 for NO:  ")
    j = int(j)
    if j == 0:
        print "BYE"
        ans = 1
        break

    else :
        number = raw_input("Please choose a number: ")
        sum = 0
