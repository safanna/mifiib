def gen_permutation(perm, k, used, N):
    """
    Переписать алгоритм так, чтобы перестановки выводились в антилексикографическом порядке.
    Если в лексикографическом порядке значимость разряда числа увеличивается справа налево,
    то в антилексикографическом — слева направо.
    Сравнение идёт сначала по самому правому символу, потом по второму с конца и так далее.
    """
    if k == N:
        for i in range(N):
            print(perm[i], end=" ");
        print()
    else:
        for x in range(N, 0, -1):
            if not used[x]:
                perm[N - k - 1] = x
                used[x] = True
                gen_permutation(perm, k + 1, used)
                used[x] = False


def gen_placement(place, k, used, N, K):
    """
    Подумайте, как можно изменить функцию генерации перестановок так, чтобы она вместо этого научилась генерировать размещения.
    Например, способы разместить N цифр на K местах при N=4, K=2:
    1 2    1 3    1 4    2 1    2 3    2 4    3 1    3 2    3 4    4 1    4 2    4 3
    """
    if k == K: # количество элементов в размещении K
        for i in range(K):
            print(place[i], end=" ")
        print()
    else:
        for x in range(1, N + 1):
            if not used[x]:
                place[k] = x
                used[x] = True
                gen_placement(place, k + 1, used);
                used[x] = False

~