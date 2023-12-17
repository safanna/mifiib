def reverse(sll):
    """
    изменить следование элементов на противоположное, «голова» и «хвост» списка при этом поменяются местами.
    У контейнеров STL этот метод называется reverse().
    """
    p = sll
    prev = None
    next = None
    while p:
        next = p.next
        p.next = prev
        prev = p
        p = next
    return prev


def has_cycle(sll):
    """
    Предположим, каким-то образом один из элементов списка стал указывать на какой-то элемент из предыдущих.
    В списке возник цикл. Как обнаружить его наличие? Используем приём «заяц и черепаха».
    Поставим в первый элемент списка два указателя.
    Затем первый, «быстрый», продвинем на два элемента вперёд, а «медленный» — на одну.
    Будем повторять, таким образом «быстрый указатель» будет «убегать» от медленного.

    Если «быстрый указатель» достигнет конца списка — цикла нет,
    в противном случае указатели встретятся, когда заяц догонит черепаху.
    Реализуйте описанный прием.
    На вход подаётся первый элемент списка. Верните True, если в этом списке есть цикл, и False, если нет.
    """
    fast = sll
    slow = sll
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def merge_sorted(p, q):
    """
    Реализуйте функцию, принимающую первые элементы двух отсортированных по неубыванию односвязных списков
     и возвращающую первую вершину нового списка,
     который состоит из элементов первых двух и тоже отсортирован по неубыванию.
    """
    dummy = slNode()
    dummy.next = None
    t = dummy;
    while(True):
        if not p:
            t.next = q
            break
        elif not q:
            t.next = p
            break
        if p.item < q.item:
            t.next = p
            t = p
            p = p.next
        else:
            t.next = q
            t = q
            q = q.next
    t = dummy.next
    return t


def insert(head, k, val):
    """
    вставить новый элемент после k-го элемента односвязного списка за один проход.
    ""
    :param head:
    :param k:
    :param val:
    :return:
    """
    for i in range(k):
        head = head.next
        if not head:
            return
    dummy = slNode()
    dummy.next = head.next
    dummy.val = val
    head.next = dummy


def kth_element(head, k):
    """
    найти k-тый элемент с конца.
    Создаём два указателя, первый (head) двигаем на  шагов вперёд. Затем двигаем оба одновременно.
    Теперь задний (tail) отстаёт на  шагов от head и, когда head дойдёт до последнего элемента,
    tail будет указывать на нужный элемент.
    ""
    :param head:
    :param k:
    :return:
    """
    tail = head
    for i in range(k):
        head = head.next
        if not head:
            return None
    while head.next:
        head = head.next
        tail = tail.next
    return tail


