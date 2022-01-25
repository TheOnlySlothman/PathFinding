from abc import ABCMeta, abstractmethod
import heapq


class PriorityQueue:
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def insert(self, node, priority, second_priority):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def reprioritize(self, node, priority):
        pass

    @abstractmethod
    def remove(self, node):
        pass


class HeapPQ(PriorityQueue):

    def __init__(self):
        self.heap = []
        self.removed = set()
        self.count = 0

    def is_empty(self):
        return self.__len__() == 0

    def __len__(self):
        return self.count

    def insert(self, item, priority, unique_id):
        item_tuple = (priority, unique_id, item)
        if item_tuple in self.removed:
            self.removed.discard(item_tuple)
        heapq.heappush(self.heap, item_tuple)
        self.count += 1
        return

    def peek(self):
        while True:
            item_tuple = self.heap[0]
            if item_tuple in self.removed:
                heapq.heappop(self.heap)
                self.removed.discard(item_tuple)
            else:
                return self.heap[0]

    def pop(self):
        while True:
            # if self.__len__() > 2 and self.heap[1][0] == self.heap[2][0]:
            # self.reprioritize(self.heap[2], self.heap[1][0] + 1)
            item_tuple = heapq.heappop(self.heap)
            if item_tuple in self.removed:
                self.removed.discard(item_tuple)
            else:
                self.count -= 1
                return item_tuple

    def reprioritize(self, item_tuple, priority):
        self.remove(item_tuple)
        # node_tuple[1].distance = priority
        # self.insert(priority, node_tuple[1])
        self.insert(item_tuple[2], priority, item_tuple[1])

    def remove(self, item_tuple):
        if item_tuple not in self.removed and item_tuple in self.heap:
            self.removed.add(item_tuple)
            self.count -= 1
        return
