from datetime import datetime

def operation(type_num, type_op, number1, number2, values):
    if type_num == 'r': type_num = "рациональные"
    elif type_num == 'c': type_num = "комплексные"
    time = datetime.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'Запрос был сделан: {time}\nЧисла: {type_num}\nВид операции: {type_op}\nЧисла: {number1, number2}\nПолученный результат: {values}\n')