from Algorithms.priorityqueue import HeapPQ
from collections import deque


def solve(maze):
    visited_nodes = []
    # 2 dimensional array corresponding to each pixel and if the corresponding node has been visited
    # visited_bool = [[False for _ in range(maze.width)] for _ in range(maze.height)]
    # queue = deque([maze.start])
    queue = HeapPQ()
    # 2 dimensional array corresponding to each pixel and the corresponding nodes previous node
    # prev = [[None for _ in range(maze.width)] for _ in range(maze.height)]
    # distances = [[float("inf") for _ in range(maze.width)] for _ in range(maze.height)]
    priority = 1

    # distances[maze.start.Position[1]][maze.start.Position[0]] = 0
    maze.start.Distance = 0
    queue.insert(maze.start, priority)
    priority += 1

    while queue.count > 0:
        current = queue.pop()

        # prev.append(current.value)
        # prev[current.value.Position[1]][current.value.Position[0]] = current.value

        if current[2] == maze.end:
            break

        for x in current[2].Neighbours:
            if x is not None and not x.Previous:
                d = abs(current[2].Position[0] - x.Position[0]) + abs(current[2].Position[1] - x.Position[1])\
                    + current[0]
                if d < x.Distance:
                    # distances[x.Position[1]][x.Position[0]] = d
                    x.Distance = d
                    x.Previous = current[2]
                    if x not in visited_nodes:
                        visited_nodes.append(x)
                        queue.insert(x, priority)
                        priority += 1
                    elif (x.Distance, x) in queue.heap:
                        queue.redistance((x.Distance, x), d)


    current = maze.end
    path = deque()
    while current is not None:
        path.appendleft(current)
        current = current.Previous

    return visited_nodes, path
