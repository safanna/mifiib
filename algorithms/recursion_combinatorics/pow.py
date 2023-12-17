def pow(a, b):
    """
    Реализовать любую рабочую функцию для возведения целого числа в целую неотрицательную степень.
    """
    ans = 1;
    for i in range(b):
        ans = ans * a
    return ans


def pow(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return pow(pow(a, b // 2), 2)
    else:
        return pow(pow(a, b // 2), 2) * a



