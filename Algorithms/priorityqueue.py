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
    def insert(self, node, priority):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def redistance(self, node, priority):
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

    def insert(self, node, priority):
        node_tuple = (node.Distance, priority, node)
        if node_tuple in self.removed:
            self.removed.discard(node_tuple)
        heapq.heappush(self.heap, node_tuple)
        self.count += 1
        return

    def peek(self):
        return self.heap[0]

    def pop(self):
        while True:
            # if self.__len__() > 2 and self.heap[1][0] == self.heap[2][0]:
            # self.reprioritize(self.heap[2], self.heap[1][0] + 1)
            node_tuple = heapq.heappop(self.heap)
            if node_tuple in self.removed:
                self.removed.discard(node_tuple)
            else:
                self.count -= 1
                return node_tuple

    def redistance(self, node_tuple, distance):
        self.remove(node_tuple)
        # node_tuple[1].distance = priority
        # self.insert(priority, node_tuple[1])
        self.insert(node_tuple[2], distance)

    def remove(self, node_tuple):
        if node_tuple not in self.removed and node_tuple in self.heap:
            self.removed.add(node_tuple)
            self.count -= 1
        return
