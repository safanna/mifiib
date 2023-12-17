def f(x):
    return x**2


# Для монотонно возрастающей функции
def search(a, b, Y):
    l = a
    r = b + 1
    while l != r - 1:
        mid = (l + r) // 2
        if f(mid) > Y:
            r = mid
        else:
            l = mid
    if f(l) == Y:
        print(l)
    else:
        print('NO')


# Попробуйте изменить программу так, чтобы она работала для монотонно невозрастающей функции.
def search2(a, b, Y):
    l = a
    r = b + 1
    while l != r - 1:
        mid = (l + r) // 2
        if f(mid) < Y: # исправление вот здесь (:
            r = mid
        else:
            l = mid
    if f(l) == Y:
        print(l)
    else:
        print('NO')
