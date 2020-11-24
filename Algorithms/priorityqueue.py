from abc import ABCMeta, abstractmethod
import heapq
from distanced_node import DistancedNode


class PriorityQueue:
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def insert(self, node):
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

    def insert(self, distanced_node):
        dnode_tuple = distanced_node.key, distanced_node.value
        if dnode_tuple in self.removed:
            self.removed.discard(dnode_tuple)
        heapq.heappush(self.heap, dnode_tuple)
        self.count += 1
        return

    def peek(self):
        return self.heap[0]

    def pop(self):
        while True:
            (distance, node) = heapq.heappop(self.heap)
            if (distance, node) in self.removed:
                self.removed.discard((distance, node))
            else:
                self.count -= 1
                return DistancedNode(distance, node)

    def reprioritize(self, node, priority):
        self.remove(node)
        node.key = priority
        self.insert(node)

    def remove(self, node):
        value = node.key, node.value
        if value not in self.removed:
            self.removed.add(node)
            self.count -= 1
        return
