from .gcd import gcd


def scm(a, b):
    """
    Исправить функцию scm так, чтобы переполнения не случалось.
    :param a:
    :param b:
    :return:
    """
    return a / gcd(a, b) * b


