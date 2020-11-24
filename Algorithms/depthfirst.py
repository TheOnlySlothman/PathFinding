from collections import deque


def solve(maze):
    visited = []
    stack = deque([maze.start])
    prev = [[None for _ in range(maze.width)] for _ in range(maze.height)]

    while len(stack) > 0:

        current = stack.pop()

        visited.append(current)

        if current == maze.end:
            break

        neighbours = reversed([x for x in current.Neighbours if x is not None and x not in visited and x not in stack])
        for x in neighbours:
            prev[x.Position[1]][x.Position[0]] = current
            stack.append(x)

    current = maze.end
    path = deque()
    while current is not None:
        path.appendleft(current)
        current = prev[current.Position[1]][current.Position[0]]

    return visited, path
