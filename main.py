from tkinter import *
from tkinter.ttk import Combobox

# Create the GUI interface
# Create a window
root = Tk()

# Give the GUI interface title
root.title('A* Demonstration')

# Select Start Node, Goal, and build Walls (Obstacles)
mapOption = StringVar()
setStartButton = Radiobutton(root, text="Set Start", value="start", var=mapOption).grid(row=0, column=0, sticky=W,
                                                                                        padx=20, pady=20)
setGoalButton = Radiobutton(root, text="Set Goal", value="goal", var=mapOption).grid(row=0, column=1, sticky=W)
setWallButton = Radiobutton(root, text="Build Wall", value="wall", var=mapOption).grid(row=0, column=2, sticky=W)

# Heuristic Options.
heuristicOption = Combobox(root, values=[
                                    "Manhattan",
                                    "Diagonal",
                                    "Euclidean",
                                    "Custom heuristic"])
heuristicOption.current(0)
heuristicOption.grid(row=0, column=4, sticky=W)


# Execute A* Star Algorithm.
def callback():
    print("click")


runButton = Button(root, text="  RUN  ", height=2, width=4, command=callback)
runButton.grid(row=0, column=9, sticky=W+E, padx=20)

# Create and style grid frame
frame = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=4, width=200, height=100, bd=0)
# Stick frame to root
frame.grid(row=1, columnspan=10, sticky=N+S+E+W, padx=20, pady=20)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)


class GridButton(Button):
    def __init__(self, x, y, *args, **kwargs):
        Button.__init__(self, x, y, *args, **kwargs)


btnList = []
wallList = []
start = []
goal = []


def location(xcor, ycor):
    # print(xcor, ycor)
    value = mapOption.get()
    if value == "wall":
        btnList[xcor][ycor]['text'] = "X"
        btnList[xcor][ycor]['fg'] = "black"
        wallList.append([xcor,ycor])
    if value == "start":
        btnList[xcor][ycor]['text'] = "S"
        btnList[xcor][ycor]['fg'] = "red"
    if value == "goal":
        btnList[xcor][ycor]['text'] = "G"
        btnList[xcor][ycor]['fg'] = "blue"


# example values
for x in range(30):
    row = []
    for y in range(15):
        btn = Button(frame, height=1, width=2, command=lambda xcor=x, ycor=y: [location(xcor, ycor)])
        btn.grid(column=x, row=y)
        row.append(btn)
    btnList.append(row)


root.mainloop()
