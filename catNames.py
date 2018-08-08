cats = []

while True:
    print('Enter cat name. Enter nothing to quit')
    cat = input()
    if cat == '':
        break
    else:
        cats = cats + [cat]

print('Your cat names are')

for cat in cats:
    print(cat)
