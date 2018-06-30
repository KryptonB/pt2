def spam():
    eggs = 1
    print(eggs)

def bacon():
    eggs = 3
    print(eggs)
    spam()
    print(eggs)

eggs = 2
bacon()
print(eggs)
