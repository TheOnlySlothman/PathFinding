from Algorithms import depthfirst, breadthfirst, dijkstra, Astar
import threading

from mazes import Maze
from result import Result


def threaded_solve(algorithm, maze):
    result = algorithm(maze)

    # result = Result(result.name, len(result.visited), result.path, result.distance, result.completion_time)

    print(result.name,
          "Time Elapsed: " + str(result.completion_time),
          "Algorithm Visited Nodes: " + str(len(result.visited)),
          "Algorithm Path Distance " + str(result.distance),
          "Algorithm Path Length: " + str(len(result.path)),
          "",
          sep="\n")


def solve(maze, threaded):
    if threaded:
        methods = [threading.Thread(target=threaded_solve, args=(depthfirst.solve, Maze(maze.image))),
                   threading.Thread(target=threaded_solve, args=(breadthfirst.solve, Maze(maze.image))),
                   threading.Thread(target=threaded_solve, args=(dijkstra.solve, Maze(maze.image))),
                   threading.Thread(target=threaded_solve, args=(Astar.solve, Maze(maze.image)))]

        for x in methods:
            x.start()
        for x in methods:
            x.join()
    else:
        methods = [depthfirst.solve,
                   breadthfirst.solve,
                   dijkstra.solve,
                   Astar.solve]

        for method in methods:
            result = method(maze)

            maze.reset()
            print(result.name,
                  "Time Elapsed: " + str(result.completion_time),
                  "Algorithm Visited Nodes: " + str(len(result.visited)),
                  "Algorithm Path Distance " + str(result.distance),
                  "Algorithm Path Length: " + str(len(result.path)),
                  "",
                  sep="\n")

    return Result(None, None, None, None, None)
