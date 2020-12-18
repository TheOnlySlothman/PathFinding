from Algorithms import depthfirst, breadthfirst, dijkstra, Astar
import threading
import time


class Result:
    def __init__(self, name, t, v_length, distance, p_length):
        self.v_length = v_length
        self.p_length = p_length
        self.time = t
        self.distance = distance
        self.name = name


def solve(maze):
    # methods = [threading.Thread(target=depthfirst.solve, args=maze),
    #           threading.Thread(target=breadthfirst.solve, args=maze),
    #           threading.Thread(target=dijkstra.solve, args=maze),
    #           threading.Thread(target=Astar.solve, args=maze)]

    methods = [depthfirst.solve,
               breadthfirst.solve,
               dijkstra.solve,
               Astar.solve]

    results = [() for _ in range(len(methods))]

    for x in range(len(methods)):
        t0 = time.time()
        visited, path, name = methods[x](maze)
        t1 = time.time()

        results[x] = Result(name, t1 - t0, len(visited), path[-1].Distance, len(path))

        maze.reset()

    for y in results:
        print(y.name,
              "Time Elapsed: " + str(y.time),
              "Algorithm Visited Nodes: " + str(y.v_length),
              "Algorithm Path Distance " + str(y.distance),
              "Algorithm Path Length: " + str(y.p_length),
              "",
              sep="\n")
    return None, None, None
