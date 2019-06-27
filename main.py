from tkinter import *
from tkinter.ttk import Combobox

# Create the GUI interface
# Create a window
root = Tk()

# Give the GUI interface title
root.title('A* Demonstration')

# Select Start Node, Goal, and build Walls (Obstacles)
mapOption = StringVar()
setStartButton = Radiobutton(root, text="Set Start", value="start", var=mapOption).grid(row=0, column=0, sticky=W,                                                                                      padx=20, pady=20)
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
runButton = Button(root, text="  RUN  ", height=2, width=4).grid(row=0, column=9, sticky=W+E, padx=20)


# Create and style grid frame
frame = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=4, width=200, height=100, bd=0)
# Stick frame to root
frame.grid(row=1, columnspan=10, sticky=N+S+E+W, padx=20, pady=20)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

# example values
for x in range(30):
    for y in range(15):
        btn = Button(frame, height=1, width=2)
        btn.grid(column=x, row=y)

for x in range(10):
    Grid.columnconfigure(frame, x, weight=1)

for y in range(5):
    Grid.rowconfigure(frame, y, weight=1)

root.mainloop()