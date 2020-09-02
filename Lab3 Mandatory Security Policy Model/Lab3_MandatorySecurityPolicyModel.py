import random

NONCONFIDENTIAL = 0
CONFIDENTIAL = 1
SECRET = 2
TOPSECRET = 3

levelList = [NONCONFIDENTIAL, CONFIDENTIAL, SECRET, TOPSECRET]
userList = ['USER1', 'USER2', 'USER3']
objectList = ['File1', 'File2', 'File3', 'File4', 'File5']

accessLevel = {'ADMIN': TOPSECRET}
objectLevel = dict()

accessLevelName = {'NONCONFIDENTIAL': NONCONFIDENTIAL,
                   'CONFIDENTIAL':    CONFIDENTIAL,
                   'SECRET':          SECRET,
                   'TOPSECRET':       TOPSECRET}
levelName = {NONCONFIDENTIAL: 'NONCONFIDENTIAL',
             CONFIDENTIAL:    'CONFIDENTIAL',
             SECRET:          'SECRET',
             TOPSECRET:       'TOPSECRET'}

# Рандомное присвоение уровней доступа субъектам
for i in range(len(userList)):
    accessLevel[userList[i]] = random.choice(levelList)
# Рандомное присвоение уровней доступа объектам
for j in range(len(objectList)):
    objectLevel[objectList[j]] = random.choice(levelList)

accessLevelTemp = accessLevel.copy()

while True:
    print('Objects:') # Печать объектов
    for k, v in objectLevel.items():
        print('\t', k, '\t', levelName[v])
    print('Subjects:') # Печать субъектов
    for k, v in accessLevelTemp.items():
        print('\t', k, '\t', levelName[v])

    login = input('Введите login под которым хотите войти: ')
    if login in accessLevelTemp:
        print('Идентификация прошла успешно, добро пожаловать в систему,', login)
        run = True
        while(run):
            cmd = input('Command >>>> ')
            # QUIT
            if cmd == 'QUIT':
                print('Работа пользователя', login, 'завершена. До свидания!')
                run = False
            # READ
            if cmd == 'READ':
                objectName = input('Над каким объектом производиться операция? >>>> ')
                if accessLevelTemp[login] >= objectLevel[objectName]:
                    print('Операция', cmd, 'прошла успешно')
                else:
                    print('Доступ запрещен!')
            # WRITE
            if cmd == 'WRITE':
                objectName = input('Над каким объектом производиться операция? >>>> ')
                if accessLevelTemp[login] <= objectLevel[objectName]:
                    print('Операция', cmd, 'прошла успешно')
                else:
                    print('Доступ запрещен!')
            # CHANGE
            if cmd == 'CHANGE':
                level = input('Введите уровень доступа >>>> ')
                if accessLevel[login] >= accessLevelName[level]:
                    accessLevelTemp[login] = accessLevelName[level]
                    print(login, 'is', level)
                else:
                    print('Доступ запрещен!')
    else:
        print('Пользователь с логином', login, 'не найден')