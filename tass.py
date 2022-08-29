import random
S = 0
while True:
    number= random.randint(1,6)
    if number!=6:
        S = S + number
        print("number dice", number)
        continue
    elif number == 6:
        print("number dice", number)
        S = S + number
        break
print('Sum of numbers:', S)