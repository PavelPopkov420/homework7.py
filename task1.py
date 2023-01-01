weekdays_list = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
weekdays_keys = {1: 'day_1.txt',2:'day_2.txt',3:'day_3.txt',4:'day_4.txt',5:'day_5.txt',6:'day_6.txt',7:'day_7.txt'}

action = int(input('Выберите действие 1-просмотр, 2 - новая запись, 3 - добавление к текущей записи: '))
while action < 1 or action > 3:
    action = int(input('Ошибка, введите действе снова(от 1 до 3): '))

if action == 1:
    day = int(input('Выберите день недели(от 1 до 7): '))
    with open(weekdays_keys[day], 'r', encoding='utf-8') as my_f:
        print(my_f.readlines(event))

elif action == 2:
    day = int(input('Выберите день недели(от 1 до 7): '))
    event = input('Какое событие у вас в этот день? : ')
    with open(weekdays_keys[day], 'w', encoding='utf-8') as my_f:
        my_f.write(event)

elif action == 3:
    day = int(input('Выберите день недели(от 1 до 7): '))
    event = input('Какое событие у вас в этот день? : ')
    with open(weekdays_keys[day], 'a', encoding='utf-8') as my_f:
        my_f.write('\n')
        my_f.write(event)