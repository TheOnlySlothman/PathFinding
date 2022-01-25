import time
from collections import deque

from result import Result


def solve(maze):
    name = 'breadthfirst'
    visited = []
    queue = deque([maze.start])
    start_time = time.time()
    while len(queue) > 0:

        current = queue.popleft()

        visited.append(current)

        if current == maze.end:
            break

        # neighbours = [x for x in current.Neighbours if x is not None and x not in visited and x not in queue]
        neighbours = [x for x in current.Neighbours.values() if x not in visited and x not in queue]

        for x in neighbours:
            x.Previous = current
            queue.append(x)

    completion_time = time.time() - start_time
    current = maze.end
    path = deque()
    while current is not None:
        path.appendleft(current)
        current = current.Previous

    return Result(name, visited, path, path[-1].Distance, completion_time)
