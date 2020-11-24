from Algorithms.priorityqueue import HeapPQ
from collections import deque
from distanced_node import DistancedNode


def solve(maze):
    visited_nodes = []
    visited_bool = [[False for _ in range(maze.width)] for _ in range(maze.height)]
    # queue = deque([maze.start])
    queue = HeapPQ()
    prev = [[None for _ in range(maze.width)] for _ in range(maze.height)]
    distances = [[float("inf") for _ in range(maze.width)] for _ in range(maze.height)]

    distances[maze.start.Position[1]][maze.start.Position[0]] = 0
    n = DistancedNode(0, maze.start)
    queue.insert(n)

    while len(queue) > 0:
        n = queue.pop()

        # prev.append(n.value)
        prev[n.value.Position[1]][n.value.Position[0]] = n.value

        if n.value == maze.end:
            break

        for x in n.value.Neighbours:
            if x is not None and x not in visited_nodes:
                d = abs(n.value.Position[0] - x.Position[0]) + abs(n.value.Position[1] - x.Position[1])
                visited_nodes.append(n.value)
                # visited_nodes[n.value.Position[0]][n.value.Position[1]] = n.value
                queue.insert(DistancedNode(d, x))






    current = maze.end
    path = deque()
    while current is not None:
        path.appendleft(current)
        current = prev[current.Position[1]][current.Position[0]]

    return visited_nodes, path
