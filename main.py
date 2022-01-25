from PIL import Image
from mazes import Maze
from algorithms import Algorithms
from images import Images

import argparse


def draw_nodes(position_list, img, name):
    img = img.convert('RGB')
    img_pixels = img.load()

    # for x in position_list:
    # img_pixels[x[0], x[1]] = (0, 200, 0)

    for x in range(len(position_list)):
        # Blue - red
        r = int((x / len(position_list)) * 255)
        img_pixels[position_list[x][0], position_list[x][1]] = (r, 0, 255 - r)

    img.save(f'{name}.png')


def draw_path(position_list, img, name):
    img = img.convert('RGB')
    img_pixels = img.load()

    for i in range(len(position_list) - 1):

        a = position_list[i]
        b = position_list[i + 1]
        # Blue - red
        r = int((i / len(position_list)) * 255)
        px = (r, 0, 255 - r)
        if a[0] == b[0]:
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                img_pixels[a[0], y] = px
        elif a[1] == b[1]:
            for x in range(min(a[0], b[0]), max(a[0], b[0])):
                img_pixels[x, a[1]] = px
        else:
            print('problem')
    img.save(f'{name}.png')


def start(algorithm, input_file, output_name):
    img = Image.open(input_file)
    maze = Maze(img)

    # for x in maze.node_char_list:
    # print(x)

    draw_nodes([x.Position for x in maze.node_list], img, './Solved Images/node_map')
    # print("Total Nodes: " + str(len(maze.node_list)))
    result = algorithm(maze)

    if result.path is not None and result.visited is not None:
        draw_nodes([x.Position for x in result.visited], img, f'./Solved Images/{output_name}_visited')
        draw_path([x.Position for x in result.path], img, f'./Solved Images/{output_name}_path')
        print(result.name,
              "Algorithm Visited Nodes: " + str(len(result.visited)),
              "Algorithm Path Length: " + str(len(result.path)),
              "Time Elapsed: " + str(result.completion_time),
              "Algorithm Path Distance " + str(result.path[-1].Distance),
              "",
              sep="\n")


def main():
    al = Algorithms()
    images = Images()
    parser = argparse.ArgumentParser()
    parser.add_argument("Algorithm", help="Selected Algorithm to use for pathfinding", default=al.default,
                        choices=al.options, nargs='?')
    parser.add_argument("Image", help="Selected Image for pathfinding", default=images.default,
                        choices=images.options, nargs='?')
    parser.add_argument("output_name", nargs='?', default="algorithm")
    args = parser.parse_args()
    # print(args)
    start(al.__getitem__(args.Algorithm), images.__getitem__(args.Image), args.output_name)


def test():
    start(Algorithms().__getitem__('race'), Images().__getitem__('braid200'), 'algorithm')


def do_all():
    algorithms = ["depthfirst", "breadthfirst", "dijkstra", "Astar"]
    images = ["tiny", "braid200", "normal", "small", "combo400"]

    for a in algorithms:
        for i in images:
            start(Algorithms().__getitem__(a), Images().__getitem__(i), i + '_' + a)


if __name__ == '__main__':
    main()
