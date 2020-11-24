from collections import deque


def solve(maze):
    visited = []
    queue = deque([maze.start])
    prev = [[None for _ in range(maze.width)] for _ in range(maze.height)]

    while len(queue) > 0:

        current = queue.popleft()

        visited.append(current)

        if current == maze.end:
            break

        neighbours = [x for x in current.Neighbours if x is not None and x not in visited and x not in queue]
        for x in neighbours:
            prev[x.Position[1]][x.Position[0]] = current
            queue.append(x)

    current = maze.end
    path = deque()
    while current is not None:
        path.appendleft(current)
        current = prev[current.Position[1]][current.Position[0]]

    return visited, path
