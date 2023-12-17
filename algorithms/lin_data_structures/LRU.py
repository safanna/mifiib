"""
кеш-память. К счастью, кешировать на самом деле ничего не придётся,
нужно лишь знать, лежит ли определённая ячейка в вашей кеш-памяти. Назовем страницей одну «ячейку памяти».
То есть мы реализуем только логику добавления/удаления страниц памяти из кеша,
сами страницы нам не интересны, и хранить/выделять память/читать ни откуда не нужно.
Итак, есть:
pageCnt — количество страниц в оперативной памяти компьютера, pageCnt .
size — размер кеша, который предстоит реализовать.
должно работать за , здесь может помочь знание о том, что pageCnt>100000.

LRU (least recently used) — наименее недавно использованный. Немного не по-русски верно?
Другими словами выбрасываем элемент, который был использован функцией get позднее других.
"""

from .doublelinkedlist import dlList


class Solution:
    def __init__(self, pageCnt, capacity):
        self.place = [None] * pageCnt
        self.size = 0
        self.capacity = capacity
        self.cache = dlList()

    def get(self, page):
        node = self.place[page]
        if not (node is None):
            self.remove(node)
        self.add(page)

    def contains(self, page):
        return not (self.place[page] is None)

    def remove(self, node):
        self.place[node.data] = None
        self.cache.remove(node)
        self.size -= 1

    def add(self, page):
        if not self.place[page] is None:
            return

        self.cache.push_front(page)
        self.place[page] = self.cache.front()

        if self.size == self.capacity:
            self.place[self.cache.back().data] = None
            self.cache.pop_back()
        else:
            self.size += 1
