# 1
from gettext import textdomain


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
# import random
#
#
# class Warrior:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#
#     def attack(self, other):
#         other.health -= 20
#         print(f"{self.name} атаковал {other.name}. У {other.name} осталось {other.health} здоровья.")
#
#     def is_alive(self):
#         return self.health > 0
#
#
# def fight(warrior1, warrior2):
#     while warrior1.is_alive() and warrior2.is_alive():
#         attacker, defender = random.choice([(warrior1, warrior2), (warrior2, warrior1)])
#         attacker.attack(defender)
#
#     if warrior1.is_alive():
#         print(f'Победил {warrior1.name}!')
#     else:
#         print(f'Победил {warrior2.name}!')
#
#
# warrior1 = Warrior('Воин 1')
# warrior2 = Warrior('Воин 2')
#
# fight(warrior1, warrior2)

class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi

    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)

print(my_circle.area)


# 2
# import random
#
#
# class Student:
#     def __init__(self, full_name, group_number, grades):
#         self.full_name = full_name
#         self.group_number = group_number
#         self.grades = grades
#
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
#
#
# first_names = ["Алексей", "Екатерина", "Дмитрий", "Ольга", "Сергей", "Татьяна", "Андрей", "Мария", "Николай", "Елена"]
# last_names = ["Иванов", "Смирнова", "Кузнецов", "Попова", "Васильев", "Новикова", "Федоров", "Морозова", "Волков",
#               "Алексеева"]
#
# students = []
# for i in range(10):
#     full_name = f"{last_names[i]} {first_names[i]}"
#     group_number = f"Группа {random.randint(101, 105)}"
#     grades = [random.randint(2, 5) for _ in range(5)]
#     students.append(Student(full_name, group_number, grades))
#
# sorted_students = sorted(students, key=lambda student: student.average_grade())
#
# print("{:<20} {:<15} {:<15}".format("ФИ", "Номер группы", "Средний балл"))
# print("-" * 50)
# for student in sorted_students:
#     print("{:<20} {:<15} {:<15.2f}".format(
#         student.full_name,
#         student.group_number,
#         student.average_grade()
#     ))

# 3
# class Parent:
#     def __init__(self, name, age, list_of_children):
#         self.name = name
#         self.age = age
#         self.list_of_children = list_of_children
#
#     def provide_info(self):
#         print(f"Родитель: {self.name}, Возраст: {self.age}")
#         if self.list_of_children:
#             print("Дети:")
#             for child in self.list_of_children:
#                 print(f"  {child.name}, Возраст: {child.age}")
#         else:
#             print("Детей нет.")
#
#     def calm_child(self, child):
#         if child in self.list_of_children:
#             child.state_of_calm = "да"
#             print(f"{self.name} успокоил(а) {child.name}.")
#         else:
#             print(f"{child.name} не является ребенком {self.name}.")
#
#     def feed_child(self, child):
#         if child in self.list_of_children:
#             child.state_of_hunger = "нет"
#             print(f"{self.name} покормил(а) {child.name}.")
#         else:
#             print(f"{child.name} не является ребенком {self.name}.")
#
#     def all_children_calm_and_fed(self):
#         for child in self.list_of_children:
#             if child.state_of_calm != "да" or child.state_of_hunger != "нет":
#                 return False
#         return True
#
#
# class Child:
#     def __init__(self, name, age, state_of_calm, state_of_hunger):
#         self.name = name
#         self.age = age
#         self.state_of_calm = state_of_calm
#         self.state_of_hunger = state_of_hunger
#
#     def info(self):
#         print(f"Ребёнок: {self.name}, Возраст: {self.age}")
#         print(f"  Спокоен(а): {self.state_of_calm}")
#         print(f"  Голоден(а): {self.state_of_hunger}")
#
#
# parent_name = input('Введите имя родителя: ')
# parent_age = int(input('Введите возраст родителя: '))
# num_children = int(input('Введите кол-во детей: '))
#
# children = []
# for i in range(num_children):
#     child_name = input(f'Введите имя ребенка {i + 1}: ')
#
#     while True:
#         child_age = int(input(f'Введите возраст ребенка {i + 1}: '))
#         if parent_age - child_age >= 16:
#             break
#         print(f"Ошибка: возраст {parent_name} должен быть больше возраста {child_name} хотя бы на 16 лет.")
#
#     state_of_calm = input(f'Ребенок {child_name} спокоен?: да/нет ')
#     state_of_hunger = input(f'Ребенок {child_name} голоден?: да/нет ')
#     child = Child(child_name, child_age, state_of_calm, state_of_hunger)
#     children.append(child)
#
# parent = Parent(parent_name, parent_age, children)
#
# parent.provide_info()
#
# while not parent.all_children_calm_and_fed():
#     print("\nТекущее состояние детей:")
#     for child in children:
#         child.info()
#
#     child_to_calm = input('\nВведите имя ребенка, которого нужно успокоить: ')
#     child_to_feed = input('Введите имя ребенка, которого нужно покормить: ')
#
#     for child in children:
#         if child.name == child_to_calm:
#             parent.calm_child(child)
#         if child.name == child_to_feed:
#             parent.feed_child(child)
#
# print("\nВсе дети спокойны и сыты!")
# for child in children:
#     child.info()


# 4 с магическим методом __add__(self, other)
# class Water:
#     def __add__(self, other):
#         if isinstance(other, Air): return Storm()
#         if isinstance(other, Fire): return Steam()
#         if isinstance(other, Earth): return Mud()
#         return None
#
#     def __str__(self):
#         return "Вода"
#
#
# class Air:
#     def __add__(self, other):
#         if isinstance(other, Water): return Storm()
#         if isinstance(other, Fire): return Lightning()
#         if isinstance(other, Earth): return Dust()
#         return None
#
#     def __str__(self):
#         return "Воздух"
#
#
# class Fire:
#     def __add__(self, other):
#         if isinstance(other, Water): return Steam()
#         if isinstance(other, Air): return Lightning()
#         if isinstance(other, Earth): return Lava()
#         return None
#
#     def __str__(self):
#         return "Огонь"
#
#
# class Earth:
#     def __add__(self, other):
#         if isinstance(other, Water): return Mud()
#         if isinstance(other, Air): return Dust()
#         if isinstance(other, Fire): return Lava()
#         return None
#
#     def __str__(self):
#         return "Земля"
#
#
# class Storm:
#     def __str__(self): return "Шторм"
#
#
# class Steam:
#     def __str__(self): return "Пар"
#
#
# class Mud:
#     def __str__(self): return "Грязь"
#
#
# class Lightning:
#     def __str__(self): return "Молния"
#
#
# class Dust:
#     def __str__(self): return "Пыль"
#
#
# class Lava:
#     def __str__(self): return "Лава"
#
#
# element_classes = {
#     '1': Water(),
#     '2': Air(),
#     '3': Fire(),
#     '4': Earth()
# }
#
#
# def print_menu():
#     print("\nВыберите элементы для смешивания:")
#     print("1 - Вода")
#     print("2 - Воздух")
#     print("3 - Огонь")
#     print("4 - Земля")
#     print("0 - Выход")
#
#
# while True:
#     print_menu()
#
#     choice1 = input("Первый элемент (1-4): ")
#     if choice1 == '0': break
#     if choice1 not in element_classes:
#         print("Некорректный выбор! Попробуйте снова.")
#         continue
#
#     choice2 = input("Второй элемент (1-4): ")
#     if choice2 == '0': break
#     if choice2 not in element_classes:
#         print("Некорректный выбор! Попробуйте снова.")
#         continue
#
#     elem1 = element_classes[choice1]
#     elem2 = element_classes[choice2]
#
#     result = elem1 + elem2
#
#     print(f"\nРезультат смешивания {elem1} + {elem2}:")
#     print(result)

# 5
class Human:
    def __init__(self, name, satiety_degree, home):
        self.name = name
        self.satiety_degree = satiety_degree
        self.home = home

    def eat(self):
        # + сытость - еда
        pass

    def work(self):
        # - сытость + деньги
        pass

    def play(self):
        # -сытость
        pass

    def buy_products(self):
        # + еда - деньги
        pass

    def live_through_the_day(self):
        pass

class Home:
    def __init__(self,fridge_with_food=50,money_cabinet=0):
        self.fridge_with_food = fridge_with_food
        self.money_cabinet = money_cabinet


