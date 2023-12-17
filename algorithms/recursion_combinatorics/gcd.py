def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def gcd(a, b):
    """
    Переписать оптимизированный вариант алгоритма Евклида так, чтобы в цикле не было условной конструкции.
    :param a:
    :param b:
    :return:
    """
    if a < b:
        a, b = b, a
    while b != 0:
        ost = a % b
        a = b
        b = ost
    return a


def gcd(a, b):
    """
    Реализуйте алгоритм Евклида c рекурсией.
    :param a:
    :param b:
    :return:
    """
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


def n_gcd(array, n):
    """
    Реализуйте функцию n_gcd, которая будет принимать на вход массив из чисел
    и возвращать наибольший общий делитель среди них всех.
    :param array:
    :param n:
    :return:
    """
    answer = array[0]
    for i in range(1, n):
        answer = gcd(answer, array[i])
    return answer
