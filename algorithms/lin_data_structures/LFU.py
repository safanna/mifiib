"""
кеш-память. К счастью, кешировать на самом деле ничего не придётся,
нужно лишь знать, лежит ли определённая ячейка в вашей кеш-памяти. Назовем страницей одну «ячейку памяти».
То есть мы реализуем только логику добавления/удаления страниц памяти из кеша,
сами страницы нам не интересны, и хранить/выделять память/читать ни откуда не нужно.
Итак, есть:
pageCnt — количество страниц в оперативной памяти компьютера, pageCnt .
size — размер кеша, который предстоит реализовать.
должно работать за , здесь может помочь знание о том, что pageCnt>100000.

LFU (Least frequently used) — наименее часто использованный.
Выбрасываем тот, который был меньше всего использован.
При этом стоит помнить, что мы запоминаем всю историю обращений,
 а не только те вызовы, которые происходили во время нахождения страницы в кеше.
Здесь уже не получится сделать за , но всё равно постарайтесь максимально оптимизировать свою программу.
Стоит упомянуть, что возможна (и вполне вероятна) ситуация, когда нужно будет выбирать из двух элементов,
частота использований которых одинаковая. Для успешного прохождения тестирования выбрасывайте наименьший из таких.
"""


from .doublelinkedlist import dlList


class Solution:
    def __init__(self, pageCnt, capacity):
        self.place = [None] * pageCnt
        self.cnt = [0] * pageCnt
        self.size = 0
        self.capacity = capacity
        self.cache = dlList()

    def get(self, page):
        self.cnt[page] += 1

        node = self.place[page]
        if node is not None:
            self.update(node)
        else:
            self.add(page)

    def contains(self, page):
        return not (self.place[page] is None)

    def update(self, node):
        while node.prev is not None and (self.cnt[node.data] > self.cnt[node.prev.data]
                                         or (self.cnt[node.data] == self.cnt[node.prev.data]
                                             and node.data > node.prev.data)):
          self.cache.swap(node.prev, node)

    def add(self, page):
        if self.size == self.capacity:
            self.size -= 1
            self.cache.pop_back()

        self.cache.push_back(page)
        self.size += 1
        self.update(self.cache.back())
