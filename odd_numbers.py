a = 1
b = 2
c = 4

if (a % 2 != 0):
    # a is odd. Hence compare
    if (a > b and a > c):
        # a is the largest
        print('a is the largest odd number')
    elif (a > b and a < c):
        # c is the largest
        if (c % 2 != 0):
            # c is odd
            print('c is the largest odd number')
    elif (a > c and a < b):
        # b is the largest
        if (b % 2 != 0):
            # b is odd
            print('b is the largest odd number')
        else:
            print('a is the largest odd number')
elif (b % 2 != 0):
    # b is odd. Hence compare
    if (b > c):
        # b is the largest odd number
        print('b is the largest odd number')
    else:
        # c is larger than b. Hence see if it's odd or not
        if (c % 2 != 0):
            # c is odd
            print('c is the largest odd number')
        else:
            # b is smaller than c but it is odd. Hence it is the largest
            print('b is the largest odd number')
elif (c % 2 != 0):
    # c is odd. And it is the only odd number. Hence it is also the largest odd number
    print('c is the largest odd number')
else:
    # c is also even. Hence no even numbers.
    print('No odd numbers')
    
