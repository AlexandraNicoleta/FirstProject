print "Calculates the largest prime factor of a number of your choice "
number = raw_input("Please choose a number: ")
i = 2
number = int(number)
ans = 0
while ans == 0:
    number = int(number)
    i = 2
    while i < number / 2:
        while number % i == 0:
            number = number / i
        if number == 1:
            number *= i
            break
        else:
            i = i + 1
    print (number)
    j = raw_input("Do you want to continue? \n Choose 1 for YES and 0 for NO: ")
    j = int(j)
    if j == 0:
        ans = 1
        print "BYE"
        break
    else:
        number = 0
        number = raw_input("Please choose a number: ")



