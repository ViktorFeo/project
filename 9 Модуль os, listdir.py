# Путь к файлу:
# Относительный - путь к файлу относительно текущей папки, документа, программы и т.д.
# lessons\python - относительный
# Абсолютный - полный путь к файлу, начиная с корня диска
# D:\lessons\python
# os.path.abspath(os.path.join('..', 'new_folder'))

import os

folder_name = 'project'
file_name = 'my_file.txt'

rel_path = os.path.join('docs', folder_name, file_name)
print(rel_path)
abs_path = os.path.abspath(file_name)
print(abs_path)


def print_dirs(project):
    print('\nСодержимое директории', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print('    ', path)


project_list = ['lessons']
for i in project_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', i))
    print_dirs(path_to_project)

print("Корень диска:", os.path.abspath(os.sep).split(os.sep)[0])


def find_file(cur_path, file_name):
    # print('переходим', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        # print('    ', path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            # print('Это директория')
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


file_path = find_file(os.path.abspath(
    os.path.join('..', '..', 'lessons')), 'kek.txt')
if file_path:
    print('Абсолютный путь к файлу: ', file_path)
else:
    print('Файл не найден.')

speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# data = speakers_file.read()
# print(data)
for i in speakers_file:
    print(i, end='')
speakers_file.close()
print()
print()




print()
# Открываем файл 'speakers.txt' для чтения в кодировке UTF-8
speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# Инициализируем пустой список для хранения количества символов в каждой строке
sym_count = []
# Проходим по каждой строке в файле
for i_line in speakers_file:
   print(i_line, end='')  # Выводим строку
   sym_count.append(str(len(i_line)))  # Добавляем длину строки в список
# Соединяем элементы списка с переносами строк
sym_count_str = '\n'.join(sym_count)
# Закрываем файл 'speakers.txt'
speakers_file.close()
# Открываем файл 'sym_count.txt' для записи
count_file = open('sym_count.txt', 'w')
# Записываем строку с длинами строк
count_file.write(sym_count_str)
# Закрываем файл 'sym_count.txt'
count_file.close()
# Печатаем пустую строку
print()

file = open('numbers.txt', 'r', encoding='utf-8')
num_count = 0
for i in file:
    num_count += int(i)
file.close()
count_file = open('answer.txt', 'w')
count_file.write(str(num_count))
count_file.close()