def add(mask, x):
    if not search(mask, x):
        return mask + (1 << x)
    else:
        return mask


def search(mask, x):
    return mask & x

#Проверка что Саша и Света прошли все курсы
# if b_sasha or b_sveta == ((1 << N) - 1):
#     print("YES")
# else:
#     print("NO")


def set_print(x):
    n = 0
    while x > 0:
        if x % 2 == 1:
            print(chr(ord('a') + n))
        x = x // 2
        n += 1


def gen_set(N):
    for x in range(1 << N):
        set_print(x)


gen_set(4)