print " \n  Fibonnaci even numbers\n"
F0, F1 = 0, 1
total = 0
while True:
    F0, F1 = F1, F0 + F1
    if F1 >= 4000000:
        break
    if F1 % 2 == 0:
        total += F1
print(total)
