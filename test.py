# 1

# file = open('numbers.txt', 'r', encoding='utf-8')
# num_count = 0
# for i in file:
#     num_count += int(i)
# file.close()
# count_file = open('answer.txt', 'w')
# count_file.write(str(num_count))
# count_file.close()

# 2

# file = open('zen.txt', 'r', encoding='utf-8')
#
# lst = []
# for line in file:
#     lst.append(line)
# for line in reversed(lst):
#     print(line, end ='')
#
# file.close()

# 3

# import os
#
# directory_path = input("Введите путь до каталога: ")
# file_count = 0
# dir_count = 0
# total_size = 0
#
# for path, dirs, files in os.walk(directory_path):
#     for file in files:
#         file_path = os.path.join(path, file)
#         file_count += 1
#         total_size += os.path.getsize(file_path)
#     for subdir in dirs:
#         dir_count += 1
#
# total_size_in_kb = total_size / 1024
#
# print(f"{directory_path}")
# print(f"Размер каталога (в Кбайтах): {total_size_in_kb}")
# print(f"Количество подкаталогов: {dir_count}")
# print(f"Количество файлов: {file_count}")

# 4

# file = open('../../Python_Basic/Module22/04_tournament/first_tour.txt', 'r')
# K = int(file.readline().strip())
# participants = []
# for line in file:
#     surname, name, score = line.strip().split()
#     participants.append((surname, name, int(score)))
# file.close()
#
# second_tour = [p for p in participants if p[2] > K]
# second_tour.sort(key=lambda x: x[2], reverse=True)
#
# output_file = open('second_tour.txt', 'w')
# output_file.write(f"{len(second_tour)}\n")
# for i, participant in enumerate(second_tour, start=1):
#     surname, name, score = participant
#     formatted_name = f"{name[0]}. {surname}"
#     output_file.write(f"{i}) {formatted_name} {score}\n")
# output_file.close()

# 5
# with open('../../Python_Basic/Module22/05_frequency_analysis/text.txt', 'r') as file:
#     text = file.read()
#
# letter_counts = {}
# total_letters = 0
#
# for char in text:
#     if char.isalpha():
#         char = char.lower()
#         if char in letter_counts:
#             letter_counts[char] += 1
#         else:
#             letter_counts[char] = 1
#         total_letters += 1
#
# letter_frequencies = []
# for letter, count in letter_counts.items():
#     frequency = count / total_letters
#     letter_frequencies.append((letter, frequency))
#
# def sort_key(item):
#     return -item[1], item[0]
#
#
# letter_frequencies_sorted = sorted(letter_frequencies, key=sort_key)
#
# with open('analysis.txt', 'w') as output_file:
#     for letter, frequency in letter_frequencies_sorted:
#         output_file.write(f"{letter} {frequency:.3f}\n")

# # 6
# import os
# import zipfile
#
# zip_path = "voina-i-mir.zip"
# unzip_folder = "voina-i-mir"
#
# os.makedirs(unzip_folder, exist_ok=True)
#
# with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#     zip_ref.extractall(unzip_folder)
#
# extracted_files = os.listdir(unzip_folder)
# print("Распакованные файлы:", extracted_files)
#
# text_file = None
# for file in extracted_files:
#     if file.endswith(".txt"):
#         text_file = os.path.join(unzip_folder, file)
#         break
#
# with open(text_file, 'r', encoding='utf-8') as f:
#     text = f.read()
#
# letter_counts = {}
# for char in text:
#     if char in letter_counts:
#         letter_counts[char] += 1
#     else:
#         letter_counts[char] = 1
#
# sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
#
# print("Частота встречаемости букв:")
# for letter, count in sorted_letters:
#     print(f"{letter}: {count}")

# words = ["Python", "мы любим", "тебя"]
# for index in range(7):
#     try:
#         print(index, words[index])
#     except:
#         print(f'Индекс {index} вышел за границы списка')
# print('Знай это')

# Module 23(10)

# 1

# summ = 0
# line_number = 0
#
# with open('people.txt', 'r', encoding='utf-8') as f, open('errors.log', 'w', encoding='utf-8') as error_log:
#     for line in f:
#         line_number += 1
#         line = line.rstrip('\n')
#         try:
#             if len(line) < 3:
#                 raise ValueError(f'Ошибка: менее трёх символов в строке {line_number}.')
#             summ += len(line)
#         except ValueError as e:
#             print(e)
#             error_log.write(str(e) + '\n')
#             summ += len(line)
#
# print(f'Общее количество символов: {summ}.')

# 2

# import random
#
# total_sum = 0
# success = True
# current_numbers = []
#
# with open('out_file.txt', 'w') as file:
#     while total_sum < 777:
#         try:
#             if random.randint(1, 13) == 1:
#                 raise Exception('Вас постигла неудача!')
#
#             number = int(input('Введите число: '))
#             total_sum += number
#             current_numbers.append(number)
#             file.write(f'{number}\n')
#         except Exception as e:
#             print(e)
#             success = False
#             break
#
#     if not success:
#         print('\nСодержимое файла out_file.txt:')
#         print('\n'.join(map(str, current_numbers[:-1])))
#
#     if success and total_sum >= 777:
#         print('Вы успешно выполнили условие для выхода из порочного цикла!')

# 3

# def validate_registration(line):
#     line = line.strip()
#     parts = line.split()
#     if len(parts) != 3:
#         raise IndexError("НЕ присутствуют все три поля")
#
#     name, email, age = parts
#
#     if not name.isalpha():
#         raise NameError("Поле «Имя» содержит НЕ только буквы")
#
#     if '@' not in email or '.' not in email:
#         raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку")
#
#     age = int(age)
#     if age < 10 or age > 99:
#         raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")
#
#
# with open('registrations.txt', 'r', encoding='utf-8') as file:
#     with open('registrations_good.log', 'w', encoding='utf-8') as good_file, \
#             open('registrations_bad.log', 'w', encoding='utf-8') as bad_file:
#
#         for line in file:
#             try:
#                 validate_registration(line)
#                 good_file.write(line)
#             except (IndexError, NameError, SyntaxError, ValueError) as e:
#                 bad_file.write(f"{line.strip()}        {str(e)}\n")

# 4

# import time
# user_name = input('Введите имя пользователя: ')
# while True:
#     print('')
#     response = input('Введите 1 или 2: ')
#     if response == '1':
#         try:
#             with open('chat.txt', 'r') as file:
#                 messages = file.readlines()
#                 print(''.join(messages))
#         except FileNotFoundError:
#             print('Служебное сообщение: пока ничего нет.\n')
#     elif response == '2':
#         new_message = input('Введите сообщение: ')
#         with open('chat.txt', 'a') as file:
#             file.write('{name}: {message}\n'.format(
#                 name=user_name, message=new_message))
#     else:
#         print('Неизвестная команда.\n')

# 4

# chat_history_file = 'chat_history.txt'
#
# def load_chat_history():
#     try:
#         with open(chat_history_file, 'r', encoding='utf-8') as file:
#             return file.readlines()
#     except FileNotFoundError:
#         print('Файл не найден. Будет создан новый файл.')
#         return []
#     except Exception as e:
#         print(f'Ошибка при чтении файла: {e}')
#         return []
#
#
# def save_message_to_file(message):
#     try:
#         with open(chat_history_file, 'a', encoding='utf-8') as file:
#             file.write(message + '\n')
#     except FileNotFoundError as e:
#         print(f'Ошибка при записи в файл: {e}')
#
#
# def handle_user(username):
#     while True:
#         print(f"\n{username}, выберите действие:")
#         print("1. Посмотреть текущий текст чата")
#         print("2. Отправить сообщение")
#         choice = input("Введите номер действия: ")
#
#         if choice == "1":
#             print("\nТекущий текст чата:")
#             chat_history = load_chat_history()
#             for message in chat_history:
#                 print(message.strip())
#         elif choice == "2":
#             message = input("Введите ваше сообщение: ")
#             full_message = f'{username}: {message}'
#             save_message_to_file(full_message)
#             print('Сообщение отправлено.')
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#
#
# print("Добро пожаловать в чат!")
# usernames = []
#
# while True:
#     username = input("Введите ваше имя: ")
#     if username in usernames:
#         print("Пользователь с таким именем уже существует. Попробуйте другое имя.")
#         continue
#     usernames.append(username)
#     print(f"Пользователь {username} присоединился к чату.")
#     handle_user(username)

# 5

# import math
#
#
# def get_sage_sqrt(number):
#     try:
#         if number < 0:
#             raise ValueError("Отрицательное число не может быть использовано для вычисления квадратного корня.")
#
#         sqrt_value = math.sqrt(number)
#         return sqrt_value
#
#     except TypeError as exc:
#         return f"Ошибка: {exc}. Переданное значение должно быть числом."
#
#     except ValueError as exc:
#         return f"Ошибка: {exc}"
#
#     except Exception as exc:
#         return f"Произошла непредвиденная ошибка: {exc}"
#
#
# numbers = [16, 25, -9, 0, 4.5, "abc"]
# for number in numbers:
#     result = get_sage_sqrt(number)
#     print(f"Квадратный корень числа {number}: {result}")

# Module 24(11)

# 1
