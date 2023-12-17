class slNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class slList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_head = slNode(data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

        if not self.tail:
            self.tail = new_head

    def push_back(self, data):
        new_tail = slNode(data=data, prev=self.tail)
        if self.tail:
            self.tail.next = new_tail
        self.tail = new_tail

        if not self.head:
            self.head = new_tail

    def pop_back(self):
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        return value

    def pop_front(self):
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return value

    def push_after(self, pos, x):
        tmp = self.head
        for i in range(pos):
            if tmp is not None:
                tmp = tmp.next

        if tmp is not None:
            tmp.next = slNode(data=x, next=tmp.next, prev=tmp)
            if tmp.next.next is not None:
                tmp.next.next.prev = tmp.next

    def pop_after(self, pos):
        tmp = self.head
        for i in range(pos):
            if tmp is not None:
                tmp = tmp.next

        if tmp is not None and tmp.next is not None:
            tmp.next = tmp.next.next
            if tmp.next is not None:
                tmp.next.prev = tmp


"""
Дана первая вершина списка. 
Напишите программу, которая позволяет пройтись по всему списку 
и после каждого элемента добавить предшествующую ему часть (новые добавленные в том числе). 
В порядке от последнего к первому.
Например, из листа
1->2->3 должно получиться 1->2->1->3->1->2->1
"""


def add(node, val):
    new_node = slNode(node.next, node, val);
    if node.next:
        node.next.prev = new_node
    node.next = new_node


def expand(start):
    while start:
        tail = start.prev
        while tail:
            add(start, tail.item)
            start = start.next
            tail = tail.prev
            start = start.next


"""
Реализуйте ещё один метод для двусвязного списка, который принимает:
Два индекса — l, r.
Третий индекс — i.
Ваша функция должна «вырезать» участок с l по r индексы (l — включительно, r — нет) 
из листа и вставить после -ого элемента (номера элементов считаются до вырезания, начиная с ).
Если хотя бы один из индексов выходит за пределы листа, завершите метод не изменяя список.
Например, после запроса
l = 2, r = 4, i = 5
список 1->2->3->4->5->6->7 превратится в 1->>4->5->2->3-6->7 .
"""


class slList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_head = slNode(data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

        if not self.tail:
            self.tail = new_head

    def push_back(self, data):
        new_tail = slNode(data=data, prev=self.tail)
        if self.tail:
            self.tail.next = new_tail
        self.tail = new_tail

        if not self.head:
            self.head = new_tail

    def pop_back(self):
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        return value

    def pop_front(self):
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return value

    def push_after(self, pos, x):
        tmp = self.head
        for i in range(pos):
            if tmp is not None:
                tmp = tmp.next

        if tmp is not None:
            tmp.next = slNode(data=x, next=tmp.next, prev=tmp)
            if tmp.next.next is not None:
                tmp.next.next.prev = tmp.next

    def pop_after(self, pos):
        tmp = self.head
        for i in range(pos):
            if tmp is not None:
                tmp = tmp.next

        if tmp is not None and tmp.next is not None:
            tmp.next = tmp.next.next
            if tmp.next is not None:
                tmp.next.prev = tmp

    def replace(self, l, r, idx):
        anchor = self.head
        for i in range(idx):
            if anchor is None:
                break
            anchor = anchor.next

        if anchor is None:
            return

        left = self.head
        for i in range(l):
            if left is None:
                break
            left = left.next

        right = self.head
        for i in range(r - 1):
            if right is None:
                break
            right = right.next

        if right is None:
            return
        if left.prev is not None:
            left.prev.next = right.next
        if right.next is not None:
            right.next.prev = left.prev

        next = anchor.next

        if next is not None:
            next.prev = right
        anchor.next = left
        left.prev = anchor
        right.next = next
