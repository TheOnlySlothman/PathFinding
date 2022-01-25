class Algorithms:
    def __init__(self):
        self.options = ["depthfirst", "breadthfirst", "dijkstra", "Astar", "race", 'race_unthreaded', "race_threaded"]
        self.default = "depthfirst"

    def __getitem__(self, item):
        if item == "depthfirst":
            from Algorithms import depthfirst
            return depthfirst.solve
        elif item == "breadthfirst":
            from Algorithms import breadthfirst
            return breadthfirst.solve
        elif item == "dijkstra":
            from Algorithms import dijkstra
            return dijkstra.solve
        elif item == "Astar":
            from Algorithms import Astar
            return Astar.solve
        elif item == "race" or item == 'race_unthreaded':
            from Algorithms import Algorithm_Race

            def solve(maze):
                return Algorithm_Race.solve(maze, False)
            return solve
        elif item == "race_threaded":
            from Algorithms import Algorithm_Race

            def solve(maze):
                return Algorithm_Race.solve(maze, True)
            return solve
