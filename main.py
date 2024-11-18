text = """Первая строка б
Вторая строка
Третья строка б
бббббббб
Фантазия заканчивается
Оперативно б"""
count = 0
lines = text.split('\n')
for line in lines:
    if 'б' in line:
        count += 1
print("Количество строк с буквой б: ", count)