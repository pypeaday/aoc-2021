""" day 12 """

from typing import List, Dict, Tuple
import itertools


class Cave:
    def __init__(self, name: str, is_big: bool = False):
        self.name = name
        self.big = is_big
        self.edges: List[str] = []
        self.visited: bool = False

    def visit(self):
        if self.big:
            self.visited = False
        else:  # little
            self.visited = True


class Edge:
    def __init__(self, p1: "Cave", p2: "Cave"):
        self.p1 = p1
        self.p2 = p2
        self.caves = [p1.name, p2.name]


def get_data(
    filepath: str = "./data/day12_sample.txt",
) -> Tuple[List[str], Dict[str, "Cave"], List["Edge"], List[str]]:
    caves: Dict[str, "Cave"] = {}
    edges: List["Edge"] = []
    cave_names: List[str] = []
    cave_map: List[str] = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            # list of caves as given in data
            cave_map.append(line.strip())
            two_caves = [char.strip() for char in line.split("-")]
            cave_names.extend(two_caves)
            for cave in two_caves:
                caves[cave] = Cave(cave, cave == cave.upper())
            edges.append(Edge(caves[two_caves[0]], caves[two_caves[1]]))
    return cave_names, caves, edges, cave_map


# def is_connected(cave: "Cave", next_cave: "Cave", edges: List["Edge"]) -> bool:
#     for edge in edges:
#         if all([cave.name in edge.caves, next_cave.name in edge.caves]):
#             return True
#     return False


def is_connected_simple(cave_map: List[str], p1: str, p2: str) -> bool:

    edge = f"{p1}-{p2}"
    if edge in cave_map:
        return True
    edge = f"{p2}-{p1}"
    if edge in cave_map:
        return True
    return False


def get_possible_paths_simple(data: List[str], cave_map: List[str]):
    paths: Dict[int, Dict[str, List]] = {0: {"end": []}}
    for i in range(
        1, len(data) + 1
    ):  # search for solution based on increasing distance
        paths[i] = dict()
        for next_cave in paths[i - 1].keys():
            if next_cave == "start":
                continue
            caves = [
                c for c in set(data) if is_connected_simple(cave_map, c, next_cave)
            ]
            print(caves)
            path = paths[i - 1][next_cave]
            for cave in caves:
                if cave == cave.lower() and cave in path:
                    # small cave already visited in this path
                    continue
                paths[i][cave] = [*path, next_cave]
    return paths


# def get_possible_paths(data: List[str], caves: Dict[str, "Cave"], edges: List["Edge"]):
#     # paths keyd by length of path valuing
#     paths: Dict[int, Dict[int, List[str]]] = {0: {0: ["end"]}}
#     for i in range(1, len(data) + 1):

#         connected_caves: List["Cave"] = get_connected_caves(paths[i-1])
#         for cave in connected_caves:
#             _path = [cave, *paths[i-1]["end"]]
#     next_cave = "end"
#     for cave in caves:
#         if is_connected(cave, next_cave, edges):


#     paths: Dict[int, List] = {0: ["end"]}
#     for i in range(1, len(data) + 1):
#         next_cave: str
#         for next_cave in paths[i - 1]:
#             for cave in caves:
#                 if is_connected(cave, next_cave, edges):
#                     paths[i].append(cave)

#     _all: List[tuple] = list(itertools.permutations(data))
#     all_possible_paths: List[tuple] = []
#     for _path in _all:
#         if _path[0] != "start":
#             continue
#         if _path[1] != "end":
#             continue
#         all_possible_paths.append(_path)
#     return all_possible_paths
