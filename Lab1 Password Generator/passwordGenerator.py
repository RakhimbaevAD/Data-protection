from random import choice

with open ('alfabet.txt', 'r', encoding='utf-8') as alfabet:
    fileLinesList = alfabet.read().splitlines()
symbols = ''.join(fileLinesList)
print('Пароль будет сгенерирован из следующих символов:')
print('\t', symbols, '\n')

amount=int(input('Введите количество паролей, которое нужно сгенерировать: '))
length=int(input('Введите длину паролей: '))
for i in range(amount):
    password = ''
    for i in range(length):
        password += choice(symbols)
    print(password)
    with open('passwordList.txt', 'a') as passwordList:
        print(password, file = passwordList)
