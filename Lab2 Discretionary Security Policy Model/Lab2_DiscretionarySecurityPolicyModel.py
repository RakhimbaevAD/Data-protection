import pprint

NUL_MASK = 0
READ_MASK = 1 << 2
WRITE_MASK = 1 << 1
GRANT_MASK = 1 << 0

RW_MASK = READ_MASK | WRITE_MASK
RG_MASK = READ_MASK | GRANT_MASK
WG_MASK = WRITE_MASK | GRANT_MASK
RWG_MASK = READ_MASK | WRITE_MASK | GRANT_MASK


accessMatrix = {'Admin': {'File1': RWG_MASK, 'File2': RWG_MASK,  'File3': RWG_MASK,  'File4': RWG_MASK,  'File5': RWG_MASK},
                'Guest': {'File1': NUL_MASK, 'File2': READ_MASK, 'File3': READ_MASK, 'File4': READ_MASK, 'File5': NUL_MASK},
                'User':  {'File1': RG_MASK,  'File2': RW_MASK,   'File3': RWG_MASK,  'File4': NUL_MASK,  'File5': WRITE_MASK}}

accessTypeNames = {NUL_MASK:   'Полный запрет',
                   GRANT_MASK: 'Передача прав',
                   WRITE_MASK: 'Запись',
                   WG_MASK:    'Запись, Передача прав',
                   READ_MASK:  'Чтение',
                   RG_MASK:    'Чтение, Передача прав',
                   RW_MASK:    'Чтение, Запись',
                   RWG_MASK:   'Полный доступ'}

while True:
    login = input('Введите login под которым хотите войти: ')
    if login in accessMatrix:
        print('Идентификация прошла успешно, добро пожаловать в систему,', login)
        print('Перечень ваших прав:')
        for k, v in accessMatrix[login].items():
            print('\t', k, '\t', accessTypeNames[v])
        run = True
        while(run):
            cmd = input('Жду ваших указаний >>>> ')
            if (cmd == 'quit'):
                print('Работа пользователя', login, 'завершена. До свидания!')
                run = False
            if (cmd == 'print'):
                pprint.pprint(accessMatrix)
				
            # Операция чтения
            if (cmd == 'read'):
                objectName = input('Над каким объектом производиться операция? >>>> ')
                if (accessMatrix[login][objectName] & READ_MASK) != NUL_MASK:
                    print('Операция прошла успешно')
                else:
                    print('Для выполнения операции', cmd, 'над объектом', objectName, 'недостаточно прав')
					
            # Операция записи
            if (cmd == 'write'):
                objectName = input('Над каким объектом производиться операция? >>>> ')
                if (accessMatrix[login][objectName] & WRITE_MASK) != NUL_MASK:
                    print('Операция прошла успешно')
                else:
                    print('Для выполнения операции', cmd, 'над объектом', objectName, 'недостаточно прав')

			# Операция передачи прав
            if (cmd == 'grant'):
                objectName = input('Над каким объектом производиться операция? >>>> ')
                grantType = input('Какое право передается? >>>> ')
                userName = input('Какому пользователю передается право? >>>> ')
                if grantType == 'r': #передаем право на чтение
                    if (accessMatrix[login][objectName] & RG_MASK) == RG_MASK:
                        accessMatrix[userName][objectName] |= READ_MASK
                        print('Вы передали права на', grantType, 'файла', objectName, 'пользователю', userName)
                    else:
                        print('У вас нет прав на эту операцию')
                if grantType == 'w': #передаем право на запись
                    if (accessMatrix[login][objectName] & WG_MASK) == WG_MASK:
                        accessMatrix[userName][objectName] |= WRITE_MASK
                        print('Вы передали права на', grantType, 'файла', objectName, 'пользователю', userName)
                    else:
                        print('У вас нет прав на эту операцию')
                if grantType == 'g': #передаем право на передачу прав
                    if (accessMatrix[login][objectName] & GRANT_MASK) == GRANT_MASK:
                        accessMatrix[userName][objectName] |= GRANT_MASK
                        print('Вы передали право на', grantType, 'файла', objectName, 'пользователю', userName)
                    else:
                        print('У вас нет прав на эту операцию')
                if grantType == 'rw': #передаем право на чтение и запись
                    if (accessMatrix[login][objectName] & RWG_MASK) == RWG_MASK:
                        accessMatrix[userName][objectName] |= RW_MASK
                        print('Вы передали права на', grantType, 'файла', objectName, 'пользователю', userName)
                    else:
                        print('У вас нет прав на эту операцию')
                if grantType == 'rwg': #наделяем полными правами
                    if (accessMatrix[login][objectName] & RWG_MASK) == RWG_MASK:
                        accessMatrix[userName][objectName] |= RWG_MASK
                        print('Вы передали права на', grantType, 'файла', objectName, 'пользователю', userName)
                    else:
                        print('У вас нет прав на эту операцию')
    else:
        print('Пользователь с логином', login, 'не найден')
