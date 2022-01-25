import time

from Algorithms.priorityqueue import HeapPQ
from collections import deque

from result import Result


def solve(maze):
    name = 'dijkstra'
    visited = []
    queue = HeapPQ()
    node_id = 1

    maze.start.Distance = 0
    queue.insert(maze.start, maze.start.Distance, node_id)
    node_id += 1
    start_time = time.time()

    while queue.count > 0:
        current = queue.pop()

        # prev.append(current.value)
        # prev[current.value.Position[1]][current.value.Position[0]] = current.value

        if current[2] == maze.end:
            break

        for x in current[2].Neighbours.values():
            if x is not None and not x.Previous:
                d = abs(current[2].Position[0] - x.Position[0]) + abs(current[2].Position[1]
                                                                      - x.Position[1]) + current[2].Distance
                if d < x.Distance:
                    # distances[x.Position[1]][x.Position[0]] = d
                    x.Distance = d
                    x.Previous = current[2]
                    if x not in visited:
                        visited.append(x)
                        queue.insert(x, x.Distance, node_id)
                        node_id += 1

    completion_time = time.time() - start_time
    current = maze.end
    path = deque()
    while current is not None:
        path.appendleft(current)
        current = current.Previous

    return Result(name, visited, path, path[-1].Distance, completion_time)
