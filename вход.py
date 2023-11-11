def avtor():
    for file3 in open('Авторизация', 'r', encoding="UTF-8"):
        if file3[2:file3.find('\t', 2)] == login:
            print('Логин найден')
            if file3[file3.find('\t', 2) + 1:file3.find('\t', file3.find('\t', 2) + 1)] == password:
                print('Вы вошли')
                p = open('Логин', 'w', encoding="UTF-8")
                p.write(login)
                p.close()
                return
            else:
                print('Пароль не правильный')
                return
    file.write(str(int(g) + 1) + '\t' + login + '\t' + password + '\t' + 'f' + '\n')
    file.close()
    p = open('Логин', 'w', encoding="UTF-8")
    p.write(login)
    print("Пользователь создан")
    print('Вы вошли')
    p.close()
    return


p = open('Логин', 'r', encoding="UTF-8")
if p.read() == '':
    login = input('login')
    password = input('password')

    n = open('negat', 'r')
    p = open('pol', 'r')
    pol = p.read()
    neg = n.read()
    print(pol)
    print(neg)

    file = open('Авторизация', 'a', encoding="UTF-8")
    g = 0
    for nine in open('Авторизация', 'r', encoding="UTF-8"):
        g = nine[0]
    if g == 'Л':
        g = 0

    while login.count('\t') or password.count('\t'):
        if login.count('\t'):
            login = input("Логин болжен быть без таба ")
        else:
            password = input("Пароль болжен быть без таба ")

    avtor()
else:
    p = open('Логин', 'r', encoding="UTF-8")
    login = p.read()

l = 0
for nine in open('Авторизация', 'r', encoding="UTF-8"):
    if l == 0:
        l = 1
    else:
        print(nine, end='')
p.close()
