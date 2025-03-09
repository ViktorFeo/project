# def my_recursive_func(x):
#     print(x)
#     my_recursive_func(x+1)
#
# my_recursive_func(1) # Переполняется стек вызовов
# Стек — это способ хранения данных, работающий по принципу «последним пришёл, первым вышел».

def my_recursive_func(x):
    if x <= 5:
        print(x)  # 1 2 3 4 5
        my_recursive_func(x + 1)
        print(x)  # 5 4 3 2 1


my_recursive_func(1)


def speller(word):
    if len(word) > 0:
        speller(word[1:])
        print(word[0])


speller('Artem')


def my_recursive_func(value):
    if len(value) <= 3:
        print(value)
        my_recursive_func(value + '*')


my_recursive_func('*')


def my_recursive_func(value):
    if len(value) <= 10:
        print(value)
        my_recursive_func(2 * value)


my_recursive_func('!')


def count_down(value):
    if value <= 0:
        print("done")
    else:
        print(value)
        count_down(value - 1)


count_down(-10)

def print_to(x):
    if x:
        print_to(x - 1)
        print(x)


print_to(5)


def func(n):
    if n == 1:
        print(1)
    else:
        func(n - 1)
        print(n)
        func(n - 1)

func(3)

def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


print(f'fact 4 = {factorial(4)}')


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f'fibo 8 = {fibonacci(8)}')


def fibonacci(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


print(f'fibo 9 = {fibonacci(9)}')


def get_product(a, b):
    if b == 0:
        return 0
    return a + get_product(a, b - 1)

print(get_product(10, 3))