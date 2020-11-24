class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [None, None, None, None]

    def node_char_list_add(self, position):
        self.node_char_list[position[1]][position[0]] = 'O'

    # def node_map(self):
        # return [self.node_char_list[self.width * x:self.width * (x + 1)] for x in range(self.height)]

    def __init__(self, im):
        self.width = im.size[0]
        self.height = im.size[1]
        self.node_list = []

        data = list(im.getdata(0))
        self.node_char_list = []

        for x in data:
            if x == 0:
                self.node_char_list.append('X')
            else:
                self.node_char_list.append('-')

        self.node_char_list = [self.node_char_list[self.width * x:self.width * (x + 1)] for x in range(self.height)]

        count = 0

        self.start = None
        self.end = None

        top_node = [None] * self.width

        for x in range(1, self.width - 1):
            if data[x] > 0:

                self.start = Maze.Node((x, 0))
                self.node_list.append(self.start)
                count = count+1
                Maze.node_char_list_add(self, (x, 0))

                top_node[x] = self.start
                break

        for y in range(1, self.height - 1):
            row_beginning = self.width * y
            row_above = row_beginning - self.width
            row_below = row_beginning + self.width

            # prev = False
            current = False
            succeeding = data[row_beginning + 1] != 0

            left_node = None
            for x in range(1, self.width - 1):
                prev = current
                current = succeeding
                succeeding = data[row_beginning + 1 + x] != 0

                n = None

                if current == 0:
                    # is wall
                    continue
                # Create vertical connections and nodes
                if prev:
                    if succeeding:
                        # OOO
                        if data[row_above + x] != 0 or data[row_below + x] != 0:
                            # is node
                            n = Maze.Node((x, y))
                            self.node_list.append(n)
                            count = count+1
                            self.node_char_list_add((x, y))

                            left_node.Neighbours[3] = n
                            n.Neighbours[2] = left_node
                            left_node = n
                        # else:
                        # middle of corridor is not node
                    else:
                        # OOX
                        n = Maze.Node((x, y))
                        self.node_list.append(n)
                        count = count+1
                        self.node_char_list_add((x, y))

                        left_node.Neighbours[3] = n
                        n.Neighbours[2] = left_node
                else:
                    if succeeding:
                        # XOO is node
                        n = Maze.Node((x, y))
                        self.node_list.append(n)
                        count = count+1
                        self.node_char_list_add((x, y))

                        left_node = n
                    else:
                        # XOX
                        if (data[row_above + x] != 0) != (data[row_below + x] != 0):
                            # end of corridor is node
                            n = Maze.Node((x, y))
                            self.node_list.append(n)
                            count = count+1
                            self.node_char_list_add((x, y))

                        # else:
                        # middle of corridor is no node
                if n is not None:
                    if data[row_above + x] != 0:
                        n.Neighbours[0] = top_node[x]
                        top_node[x].Neighbours[1] = n
                        top_node[x] = None
                    if data[row_below + x] != 0:
                        top_node[x] = n

        final_row = self.width * (self.height - 1)

        for x in range(1, self.width - 1):
            if data[final_row + x] > 0:
                self.end = Maze.Node((x, self.height - 1))
                self.node_list.append(self.end)
                count = count+1
                self.node_char_list_add((x, self.height - 1))

                top_node[x].Neighbours[1] = self.end
                self.end.Neighbours[0] = top_node[x]
                break

                # if data[row_above + x] != 0 or data[row_below + x]:
                # n = Maze.Node(f'{x},{y}')
                # if data[row_above + x] != 0:
                # top_node[x].Neighbours[1] = n
                # n.Neighbours[0] = top_node[x]
        print("Count: " + str(count))
        print("Length: " + str(len(self.node_list)))
