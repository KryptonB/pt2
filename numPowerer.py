def powerer(number, power):
    return (number**power)

print('Please enter the number')
number = int(input())

print('Please enter the power')
power = int(input())

print(str(number) + ' to the power '+ str(power) + ' is ' + str(powerer(number, power)))
