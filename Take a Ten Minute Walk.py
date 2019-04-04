def appointment(walk):
    n, e = 0, 0
    if len(walk) == 10:
        for i in walk:
            if i == 'n':
                n = n + 1
            elif i == 's':
                n = n - 1
            elif i == 'e':
                e = e + 1
            elif i == 'w':
                e = e - 1
        if n == 0 and e == 0:
            return True
        else:
            return False
    else:
        return False


walk = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']
if appointment(walk) == True:
    print('散步完成!')
else:
    print('散步未完成!')









