# ООП) — это парадигма программирования, которая использует объекты и классы для организации кода.
# Основные концепции ООП включают:
# Класс (Class) — это шаблон или чертеж для создания объектов.
# Класс определяет свойства (атрибуты) и методы (функции), которые будут доступны объектам этого класса.
# Объект (Object) — это экземпляр класса.
# Объект имеет состояние (значения атрибутов) и поведение (методы).
# Наследование (Inheritance) — это механизм, позволяющий создавать новый класс на основе существующего.
# Новый класс наследует атрибуты и методы родительского класса.
# Инкапсуляция (Encapsulation) — это сокрытие внутренней реализации объекта
# и предоставление доступа только через публичные методы.
# Полиморфизм (Polymorphism) — это способность объектов с одинаковым интерфейсом (методами)
# вести себя по-разному в зависимости от их типа.
# Абстракция (Abstraction) — это процесс упрощения сложных систем путем выделения только важных характеристик объекта.

# Класс, атрибут класса, конструктор класса, метод объекта, объект(экземпляр класса)

from random import randint


class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name, age, isHappy=None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, 'age:', self.age, 'isHappy:', self.isHappy)


cat1 = Cat('Barsik', 3, True)
cat2 = Cat('Jopen', 2, False)


class OldUser:  # Определение класса User
    user_name = 'Admin'  # Атрибут класса, хранящий имя пользователя
    password = 'qwerty'  # Атрибут класса, хранящий пароль пользователя
    is_banned = False  # Атрибут класса, указывающий, забанен ли пользователь (по умолчанию False)


user_1 = OldUser()  # Создание экземпляра класса User с именем user_1
user_2 = OldUser()  # Создание экземпляра класса User с именем user_2
# Устанавливаем значение атрибута user_name для экземпляра user_2
# Теперь user_2 имеет собственный атрибут user_name со значением 'Tom'
# Это переопределяет значение атрибута класса User.user_name для данного экземпляра
user_2.user_name = 'Tom'
# Выводим значения атрибута user_name для обоих экземпляров
# На этом этапе оба экземпляра используют атрибут класса, который равен 'Admin'
print(user_1.user_name, user_2.user_name)  # Вывод: Admin Admin
OldUser.user_name = 'Noname'  # Изменяем значение атрибута user_name на уровне класса
# Выводим значения атрибута user_name для обоих экземпляров
# Поскольку атрибут изменен на уровне класса, оба экземпляра теперь используют новое значение
print(user_1.user_name, user_2.user_name)  # Вывод: Noname Noname


class Toyota:

    def __init__(self, color='red', price=1e6, max_speed=200, current_speed=0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def print_info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}'.format(
            self.color, self.price, self.max_speed, self.current_speed))

    def set_current_speed(self, speed):
        if int(speed) > int(self.max_speed):
            self.current_speed = self.max_speed
        else:
            self.current_speed = speed


car1 = Toyota('red', 1000000, 200, 0)
car1.set_current_speed(100)
car1.print_info()


class Monitor:
    name = "Samsung"
    matrix = "VA"
    resolution = "WQHD"
    frequency = 0


class Headphones:
    name = "Sony"
    sensitivity = 108
    micro = True


monitors = [Monitor() for _ in range(4)]
headphones = [Headphones() for _ in range(3)]

for index, number in enumerate([60, 144, 70, 60]):
    monitors[index].frequency = number

headphones[0].micro = False

print(monitors[0].name, monitors[0].matrix, monitors[0].resolution, monitors[0].frequency)
for i in monitors:
    print(i.name, i.matrix, i.resolution, i.frequency)


class User:  # Определение класса User
    user_name = 'Admin'  # Атрибут класса: имя пользователя (по умолчанию 'Admin')
    password = 'qwerty'  # Атрибут класса: пароль пользователя (по умолчанию 'qwerty')
    is_banned = False  # Атрибут класса: статус блокировки (по умолчанию False)
    friends = []  # Атрибут класса: список друзей (по умолчанию пустой список)

    def print_info(self):  # Метод для вывода информации о пользователе
        print('Name: {}\nPassword: {}\nBan status: {}'.format(
            self.user_name, self.password, self.is_banned)
        )  # Вывод информации о пользователе (имя, пароль, статус блокировки)

    def add_friend(self, friend):  # Метод для добавления друга
        # Если друг является экземпляром класса User, добавляем его имя в список друзей
        if isinstance(friend, User):
            self.friends.append(friend.user_name)
        else:
            # Иначе добавляем друга как есть (например, строку)
            self.friends.append(friend)


user_1 = User()  # Создание первого экземпляра класса User
user_2 = User()  # Создание второго экземпляра класса User
user_2.user_name = 'Lel'  # Изменение имени пользователя user_2 на 'Lel'
user_1.add_friend('Kek')  # Добавление строки 'Kek' в список друзей user_1
user_1.add_friend(user_2)  # Вывод информации о пользователе user_1
user_1.print_info()  # Вывод информации о пользователе user_1
# Вывод имени пользователя user_1 и списка его друзей
# *user_1.friends распаковывает список друзей, чтобы вывести их как отдельные аргументы
print(user_1.user_name, *user_1.friends)


class Family:
    surname = 'Common Family'
    money = 100000
    have_a_house = False

    def info(self):
        print('Family name: {}\nFamily founds: {}\nHave a House: {}'.format(
            self.surname, self.money, self.have_a_house))

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Current value: {}\n'.format(amount, self.money))

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print('House purchased! Current money: {}\n'.format(self.money))
        else:
            print('Not enough money!\n')


my_family = Family()
my_family.info()
print('Try to buy a house')
my_family.buy_house(10 ** 6)
if not my_family.have_a_house:
    my_family.earn_money(800000)
    print('Try to buy a house again')
    my_family.buy_house(10 ** 6, 10)

my_family.info()


class Employee:  # Определение класса Employee

    def __init__(self, name, salary):  # Конструктор класса, который вызывается при создании нового объекта
        self.name = name  # Инициализация атрибута name для текущего объекта
        self.salary = salary  # Инициализация атрибута salary для текущего объекта

    def print_info(self):  # Метод для вывода информации о сотруднике
        print('Name: {}\nSalary: {}'.format(self.name, self.salary))  # Вывод имени и зарплаты сотрудника


emp_1 = Employee('Tom', 10000)  # Создание первого объекта (экземпляра) класса Employee с именем 'Tom' и зарплатой 10000
emp_2 = Employee('Bob', 20000)  # Создание второго объекта (экземпляра) класса Employee с именем 'Bob' и зарплатой 20000
emp_1.print_info()  # Вывод информации о первом сотруднике (emp_1)
emp_2.print_info()  # Вывод информации о втором сотруднике (emp_2)


from garden import PotatoGarden

my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()

class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count += 1

    def info(self):
        return 'Точка с координатами {}, {}'.format(self.x, self.y)


p1 = Point()
print(p1.info())
p2 = Point(3, 4)
print(p2.info())
print(Point.count)