from collections import deque
import time

from result import Result


def solve(maze):
    name = 'depthfirst'
    visited = []
    stack = deque([maze.start])
    # prev = [[None for _ in range(maze.width)] for _ in range(maze.height)]
    start_time = time.time()

    while len(stack) > 0:

        current = stack.pop()

        visited.append(current)

        if current == maze.end:
            break

        # neighbours = reversed([x for x in current.Neighbours if x is not None and x not in visited and x not in stack])
        neighbours = reversed([x for x in current.Neighbours.values() if x not in visited and x not in stack])
        for x in neighbours:
            x.Previous = current
            stack.append(x)

    completion_time = time.time() - start_time
    current = maze.end
    path = deque()
    while current is not None:
        path.appendleft(current)
        # current = prev[current.Position[1]][current.Position[0]]
        current = current.Previous

    return Result(name, visited, path, path[-1].Distance, completion_time)
