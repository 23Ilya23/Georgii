from tkinter import Tk, Canvas
from grid import Grid
from human import Human
 
 
root = Tk()
canvas = Canvas(root , width=800, height=600)
canvas.pack()
 
grid = Grid(canvas)
grid.display()

p1 = Human(canvas, 200, 500)
p1.display()
 
root.mainloop()
