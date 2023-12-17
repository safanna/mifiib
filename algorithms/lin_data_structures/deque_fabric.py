"""
В городе  стоит завод, в этом заводе есть столовая, а в этой столовой всего одна касса,
возле которой всегда образуется очередь.
Рабочие на заводе делятся на две категории: обычные трудяги-работяги и начальство.
Когда трудяга приходит на обед, он встаёт в конец очереди, а когда приходит кто-либо из начальства,
он встает в середину очереди.
Если в очереди нечётное количество людей, то сразу за центром.
Так как на этом заводе работают очень хитрые рабочие, вам поручили отслеживать их порядок в очереди.
Реализуйте методы:
worker(i) — рабочий с номером   встаёт в конец очереди.
boss(i) — начальник с номером  встаёт в середину очереди. У каждого человека номер уникален.
next() — первый рабочий из очереди уходит к кассе. Гарантируется, что на момент такого запроса очередь не пуста.
Для каждого запроса типа next программа должна вывести номер рабочего или начальника, который должен пройти к кассе.
"""

from collections import deque


class solution:
    def __init__(self):
        self.first = deque()
        self.second = deque()

    def worker(self, i):
        self.second.append(i)

        if len(self.second) > len(self.first):
            x = self.second.popleft()
            self.first.append(x)

    def boss(self, i):
        self.second.appendleft(i)

        if len(self.second) > len(self.first):
            x = self.second.popleft()
            self.first.append(x)

    def next(self):
        res = self.first.popleft()

        if len(self.second) > len(self.first):
            x = self.second.popleft()
            self.first.append(x)

        return res