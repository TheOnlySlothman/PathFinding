from collections import deque


def solve(maze):
    visited = []
    queue = deque([maze.start])

    while len(queue) > 0:

        current = queue.popleft()

        visited.append(current)

        if current == maze.end:
            break

        neighbours = [x for x in current.Neighbours if x is not None and x not in visited and x not in queue]
        for x in neighbours:
            x.Previous = current
            queue.append(x)

    current = maze.end
    path = deque()
    while current is not None:
        path.appendleft(current)
        current = current.Previous

    return visited, path
