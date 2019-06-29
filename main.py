# GUI implementation
# Author: Nguyen Van Manh
# Date: June 27, 2019

from tkinter import *
from tkinter.ttk import Combobox
from aStar import *

# Create the GUI interface
# Create a window
root = Tk()

# Give the GUI interface title
root.title('A* Demonstration')

# Select Start Node, Goal, and build Obstacles (Obstacles)
mapOption = StringVar()
setStartButton = Radiobutton(root, text="Set Start", value="start", var=mapOption)
setStartButton.grid(row=0, column=0, sticky=W, padx=20, pady=20)
setGoalButton = Radiobutton(root, text="Set Goal", value="goal", var=mapOption)
setGoalButton.grid(row=0, column=1, sticky=W)
setObstacleButton = Radiobutton(root, text="Build Obstacles", value="obstacle", var=mapOption)
setObstacleButton.grid(row=0, column=2, sticky=W)

# Heuristic Options.
heuristicOption = Combobox(root, values=[
                                    "Manhattan",
                                    "Diagonal",
                                    "Euclidean"], width=10)
heuristicOption.current(0)
heuristicOption.grid(row=0, column=4, sticky=W)


# Execute A* Star Algorithm.
def callback():
    print("click")


# Create and style grid frame
frame = Frame(root, highlightbackground="black", highlightcolor="black",
              highlightthickness=4, width=200, height=100, bd=0)
# Stick frame to root
frame.grid(row=1, columnspan=10, sticky=N+S+E+W, padx=20, pady=20)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)


class GridButton(Button):
    def __init__(self, x, y, *args, **kwargs):
        Button.__init__(self, x, y, *args, **kwargs)


btnList = []
obstacleList = []
start = []
goal = []


def location(xcor, ycor):
    # print(xcor, ycor)
    value = mapOption.get()
    if value == "obstacle":
        btnList[xcor][ycor]['text'] = "X"
        btnList[xcor][ycor]['fg'] = "black"
        obstacleList.append((xcor, ycor))
    if value == "start":
        btnList[xcor][ycor]['text'] = "S"
        btnList[xcor][ycor]['fg'] = "red"
        start.append((xcor, ycor))
        setStartButton.config(state=DISABLED)
        setStartButton.deselect()
    if value == "goal":
        btnList[xcor][ycor]['text'] = "G"
        btnList[xcor][ycor]['fg'] = "blue"
        goal.append((xcor, ycor))
        setGoalButton.config(state=DISABLED)
        setGoalButton.deselect()


mapWidth = 30
mapHeight = 15
# example values
for x in range(mapWidth):
    row = []
    for y in range(mapHeight):
        btn = Button(frame, height=1, width=2, command=lambda xcor=x, ycor=y: [location(xcor, ycor)])
        btn.grid(column=x, row=y)
        row.append(btn)
    btnList.append(row)


def run():
    # enable setStart and setGoal
    setStartButton.config(state=NORMAL)
    setGoalButton.config(state=NORMAL)

    # A* search
    map = GridWithWeights(mapWidth, mapHeight)
    map.obstacles = obstacleList
    startNode = start[0]
    goalNode = goal[0]
    option = heuristicOption.get()
    node_track, cost = a_star_search(map, startNode, goalNode, option)
    nodes_along_path = shortest_path(node_track, start=startNode, goal=goalNode)

    for loc in node_track:
        if loc != startNode and loc != goalNode:
            btnList[loc[0]][loc[1]]['text'] = "+"
            btnList[loc[0]][loc[1]]['fg'] = "grey"

    for node in nodes_along_path:
        if node != startNode and node != goalNode:
            btnList[node[0]][node[1]]['text'] = "*"
            btnList[node[0]][node[1]]['fg'] = "orange"

    # re-set-up new round
    obstacleList.clear()
    start.clear()
    goal.clear()


runButton = Button(root, text="  RUN  ", height=2, width=4, command=run)
runButton.grid(row=0, column=9, sticky=W+E, padx=20)

def clear():
    # cleanup grid
    for btnRow in btnList:
        for btn in btnRow:
            btn['text'] = ""
            btn['fg'] = "white"

    # clean up lists.
    obstacleList.clear()
    start.clear()
    goal.clear()

clearButton = Button(root, text="CLEAR", height=2, width=6, command=clear)
clearButton.grid(row=0, column=8, sticky=W+E, padx=10)

root.mainloop()
