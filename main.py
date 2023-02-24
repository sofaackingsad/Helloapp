print("Hello Python from PyCharm")
s = "*" *30
print("New project")
print(s)

#Написать алгоритм генерации пароля

import random
chars='abcdefghijklmnopkrstunvwxyzABCDEFGHIJKLMNOPQRSTUNVWXYZ0123456789!.,/?\|=+-_)(*&^%$#@~'
try:
    password=''
    len=int(input("Длина пароля от 8 до 20: "))
    if len < 8:
        print('Неверный ввод!')
    elif len > 20:
        print('Неверный ввод!')
    elif len >=8 and len <=20:
        for i in range(len):
            password+=random.choice(chars);
        print('Пароль получился:\n',password)
except ValueError:
    print('Длина пароля должна состоять из целочисленных цифр')