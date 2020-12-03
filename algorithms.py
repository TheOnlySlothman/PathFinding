class Algorithms:
    def __init__(self):
        self.options = ["depth_first", "breadth_first", "dijkstra", "a_star"]
        self.default = "depth_first"

    def __getitem__(self, item):
        if item == "depth_first":
            from Algorithms import depthfirst
            return depthfirst.solve
        elif item == "breadth_first":
            from Algorithms import breadthfirst
            return breadthfirst.solve
        elif item == "dijkstra":
            from Algorithms import dijkstra
            return dijkstra.solve
        elif item == "a_star":
            from Algorithms import Astar
            return Astar.solve
