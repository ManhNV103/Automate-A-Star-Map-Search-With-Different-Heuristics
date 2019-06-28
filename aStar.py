# A Star + Heuristic Library
# Author: Nguyen Van Manh
# Some parts of the code are adopted from different articles at https://www.redblobgames.com/
# Date: June 27, 2019

import heapq
from math import sqrt


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []

    def notObstacle(self, loc):
        return loc not in self.obstacles

    def isValidLoc(self, loc):
        (x, y) = loc
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, loc):
        (x, y) = loc
        neighborsList = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1),
                         (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)]
        neighborsList = filter(self.isValidLoc, neighborsList)
        neighborsList = filter(self.notObstacle, neighborsList)
        return neighborsList


# need to fix this.
class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)  # return 1 if weight not exist


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    # add an item with its priority.
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    # pop an item with the lowest priority.
    def pop(self):
        return heapq.heappop(self.elements)[1]


def shortest_path(node_track, start, goal):
    """
    Find the "shortest" path (possible) by reversing from the goal to the start.
    :param node_track: list of node inspected and their parent. came_from
    :param start: start node
    :param goal: goal node
    :return:
    """
    currentNode = goal
    path = []
    while currentNode != start:
        path.append(currentNode)
        currentNode = node_track[currentNode]
    path.append(start)
    path.reverse()  # reverse to get the original order from the start to the goal
    return path

# Heuristics
def manhattan(goal, node):
    (x1, y1) = goal
    (x2, y2) = node
    return abs(x1 - x2) + abs(y1 - y2)

def diagonal(goal, node):
    (x1, y1) = goal
    (x2, y2) = node
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return dx + dy + (sqrt(2) - 2) * min(dx, dy)

def euclidean(goal, node):
    (x1, y1) = goal
    (x2, y2) = node
    dx = abs(x1 - x2)
    dy = abs(x1 - x2)
    return sqrt(dx*dx + dy*dy)


def a_star_search(graph, start, goal):
    # Create and initiate the priority queue.
    pQueue = PriorityQueue()
    pQueue.put(start, 0)

    # Create and initiate node_track and cost
    node_track = {start: None}
    cost = {start: 0}

    while not pQueue.empty():
        currentNode = pQueue.pop()

        if currentNode == goal:
            break

        for successor in graph.neighbors(currentNode):
            g_n = cost[currentNode] + graph.cost(currentNode, successor)
            if successor not in cost or g_n < cost[successor]:
                cost[successor] = g_n
                f_n = g_n + diagonal(goal, successor)
                pQueue.put(successor, f_n)
                node_track[successor] = currentNode

    return node_track, cost