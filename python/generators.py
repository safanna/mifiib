def count(start=1, step=1):
    """
    Создать функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
    По умолчанию она начинается с единицы и шаг равен 1,
    но пользователь может указать любой шаг и любое число в качестве аргумента функции,
    с которого будет начинаться последовательность.
    :param start:
    :param step:
    :return:
    """
    counter = start
    while True:
        yield counter
        counter += step


def repeat_list(list_):
    list_values = list_.copy()
    while True:
        value = list_values.pop(0)
        list_values.append(value)
        yield value


# for i in repeat_list([1, 2, 3]):
#     print(i)


# """
# декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной, содержащей количество вызовов, используйте nonlocal область декоратора.
# :param func:
# """
def counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        func(*args, **kwargs)
        count += 1
        print(f"Функция {func} была вызвана {count} раз")

    return wrapper


@counter
def say_word(word):
    print(word)


def cache(func):
    cache_dct = {}
    def wrapper(n):
        nonlocal cache_dct
        if n in cache_dct:
            print("Берем из кэша")
        else:
            print("Считаем")
            cache_dct[n] = func(n)
        return cache_dct[n]
    return wrapper

@cache
def f(n):
    return n * 123456789

# print(f(1))
# print(f(2))
# print(f(1))
# print(f(4))


def linear_solve(a, b):
    return b/a

print(linear_solve(2, 9))


def D(a,b,c):
    return b**2 - 4*a*c

def quadratic_solve(a,b,c):
    if D(a,b,c) < 0:
        return "Нет вещественных корней"
    elif D(a,b,c) == 0:
        return -b/(2*a)
    else:
        return (-b-D(a,b,c)**0.5)/(2*a), (-b+D(a,b,c)**0.5)/(2*a)


M = {'a' : 1,
     'b' : 0,
     'c' : -1}

print(quadratic_solve(**M))


def min_list(L):
    """
    Напишите рекурсивную функцию,
    находящую минимальный элемент списка без использования циклов и встроенной функции min()
    :param L:
    :return:
    """
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

print(min_list([1, 2, 0, 5, 1]))

def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res

print(mirror(567))


def equal(N, S):
    """
    реализовать функцию equal(N, S), проверяющую, совпадает ли сумма цифр числа N с числом S.
    При написании программы следует обратить внимание на то, что если S стала отрицательной,
    то необходимо сразу вернуть False.
    :param N:
    :param S:
    :return:
    """
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)


def e():
    n = 1
    while True:
        yield (1 + 1 / n) ** n
        n += 1
last = 0
for a in e(): # e() — генератоp
    if (a - last) < 0.001: # ограничение на точность
        print(a)
        break # после достижения которого завершаем цикл
    else:
        last = a # иначе — присваиваем новое значение

# iter_obj = iter("Hello!")
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

result = filter(lambda x: x % 2 == 0, [-2, -1, 0, 1, -3, 2, -3])

print(list(result))   # [-2, 0, 2]

data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]
print(min(data, key=lambda x: x[0] / x[1] ** 2))  # отбор по ключу