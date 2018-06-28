def powerer(number, power):
    return (number**power)

while True:
    print('')
    print('Please enter the number')
    number = input()

    if number == 'q':
        print('Goodbye!')
        break
    
    number = int(number)

    print('Please enter the power')
    power = int(input())

    print(str(number) + ' to the power '+ str(power) + ' is ' + str(powerer(number, power)))
