def spam():
    eggs = 1
    eggs2 = 'rrr'
    print(eggs)

def bacon():
    eggs = 3
    print(eggs)
    spam()
    print(eggs)
    print(eggs)

eggs = 2
bacon()
print(eggs)
