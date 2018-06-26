while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    while True:
        print('Hello Joe, what is the password? (It is a fish)')
        password = input()
        if password != 'swordfish':
            continue
        else:
            break
    break
print('Access granted.')
