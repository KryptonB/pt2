totalMinutes = 0

print('Please enter your minutes')
totalMinutes = input()

hours = int(totalMinutes) // 60
minutes = int(totalMinutes) % 60

print(str(hours) + ' hour(s) and ' + str(minutes) + ' minutes')
