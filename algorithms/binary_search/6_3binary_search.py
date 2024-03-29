from bisect import bisect_right, bisect_left

# Создадим массив для хранения количества тетрадей в каждой партии.
# Для каждого покупателя мы найдём такое наибольшее число тетрадей, которое он может купить.
# То есть найдём в массиве наибольшее число, которое меньше или равно заданного.
# Для того чтобы делать это наиболее эффективно, отсортируем наш массив по неубыванию и воспользуемся бинарным поиском.


def binsearch(array, n, Y):
    l = 0 # левая граница включительно
    r = n # правая граница не включительно
    while l != r - 1:
        mid = (l + r) // 2
        if array[mid] > Y:
            r = mid
        else:
            l = mid
    return array[l]


# Подумайте, как можно переделать функцию, чтобы она искала самое правое вхождение элемента?
def leftbin(array, n, Y):
    l = 0 # левая граница включительно
    r = n # правая граница не включительно
    while l != r - 1:
        mid = (l + r) // 2
        if array[mid] >= Y: # включаем равенство для левой границы
            r = mid
        else:
            l = mid
    if array[r] == Y: # левая включительно, поэтому в ней должен лежать искомый элемент
        return r
    else:
        return -1


# Подумайте, как можно переделать функцию, чтобы она искала самое левое вхождение элемента?
# Сделаем так, чтобы теперь, наоборот, левая граница была не включительно, то есть обозначала номер элемента,
# который точно меньше искомого, а правая граница была включительно, то есть обозначала номер элемента,
# который точно больше или равен искомому.
# Для этого нам нужно по-другому задать начальные значения l и r, а также в цикле изменить условие,
# при котором они меняются.
def leftbin(array, n, Y):
    l = -1 # левая граница не включительно
    r = n - 1 # правая граница включительно
    while l != r - 1:
        mid = (l + r) // 2
        if array[mid] >= Y: # включаем равенство для правой границы
            r = mid
        else:
            l = mid
    if array[r] == Y: # правая включительно, поэтому в ней должен лежать искомый элемент
        return r
    else:
        return -1

# Аналогом функций upper_bound и lower_bound в Python являются функции bisect_right (она же bisect) и bisect_left
# соответственно. Работать с ними можно через специальный модуль bisect.
# Разве что эти функции возвращают не указатель, а индекс элемента списка
# Воспользуйтесь функциями bisect_left и/или bisect_right и реализуйте свою функцию binsearch,
# которая будет принимать на вход список и искомый элемент, и возвращать True,
# если элемент присутствует в списке, иначе False.


def search(a, x):
    pos = bisect_left(a, x)
    if pos < len(a) and a[pos] == x:
        return True
    else:
        return False