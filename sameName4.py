def spam():
    print(eggs, end='')
    c = a + b
    print(a, b, c, sep=',')
    print(a, b, c, sep=',')
    #eggs = 'spam local'

eggs = 'global'
a = 3
b = 2
spam()
