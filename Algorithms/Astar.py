from Algorithms.priorityqueue import HeapPQ
from collections import deque
import time
from result import Result


def solve(maze):
    name = 'Astar'
    visited_nodes = []
    queue = HeapPQ()
    node_id = 1

    maze.start.Distance = 0
    d_end = abs(maze.end.Position[0] - maze.start.Position[0]) + abs(maze.end.Position[1] - maze.start.Position[1])
    queue.insert(maze.start, d_end, node_id)
    node_id += 1
    start_time = time.time()

    while queue.count > 0:
        current = queue.pop()
        if current[2] == maze.end:
            break

        for x in current[2].Neighbours.values():
            if x is not None and not x.Previous:
                d = abs(current[2].Position[0] - x.Position[0]) + abs(current[2].Position[1] - x.Position[1]) \
                    + current[2].Distance
                d_end = d + abs(maze.end.Position[0] - x.Position[0]) + abs(maze.end.Position[1] - x.Position[1])
                if d < x.Distance:
                    x.Distance = d
                    x.Previous = current[2]
                    if x not in visited_nodes:
                        visited_nodes.append(x)
                        queue.insert(x, d_end, node_id)
                        node_id += 1

    completion_time = time.time() - start_time
    current = maze.end
    path = deque()
    while current is not None:
        path.appendleft(current)
        current = current.Previous

    return Result(name, visited_nodes, path, path[-1].Distance, completion_time)
