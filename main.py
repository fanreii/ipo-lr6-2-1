text = """Первая строка б
Вторая строка
Третья строка б
бббббббб
Фантазия заканчивается
Оперативно б""" # изначальные строки
count = 0 # переменная для дальнейшего подсчета суммы
lines = text.split('\n') # разделение текста на линии по абзацу
for line in lines: # для каждой линии в разделенном тексте
    if 'б' in line: # если в линии встречается б
        count += 1 # увеличение переменной sum на 1
print("Количество строк с буквой б: ", count) # вывод результата 
