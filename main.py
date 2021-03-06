from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game Made By Min Khant Soe")
root.resizable(False, False)

top_bar = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_percentage(20)
)

top_bar.place(x=0, y=0)

game_title = Label(
    top_bar,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 38)
)
game_title.place(
    x=utils.width_percentage(25),
    y=0
)

left_bar = Frame(
    root,
    bg="black",
    width=utils.width_percentage(25),
    height=utils.height_percentage(80)
)

left_bar.place(x=0, y=utils.height_percentage(20))

center_location = Frame(
    root,
    bg="black",
    width=utils.width_percentage(80),
    height=utils.height_percentage(80)
)

center_location.place(
    x=utils.width_percentage(20),
    y=utils.height_percentage(20)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_location)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Calling the label from the Cell class
Cell.create_cell_count_label(left_bar)
Cell.cell_count_label_object.place(
    x=0,
    y=0
)

Cell.randomize_mines()

# Run The Game
root.mainloop()
