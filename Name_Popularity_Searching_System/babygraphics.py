"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    wid_ins = width - GRAPH_MARGIN_SIZE * 2
    gap = wid_ins / len(YEARS)
    return int(GRAPH_MARGIN_SIZE + year_index * gap)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    wid_ins = CANVAS_WIDTH - GRAPH_MARGIN_SIZE * 2
    gap = wid_ins / len(YEARS)
    for i in range(0, wid_ins, int(gap)):
        canvas.create_line(GRAPH_MARGIN_SIZE + i, 0, GRAPH_MARGIN_SIZE + i, CANVAS_HEIGHT)
    for i in range(len(YEARS)):
        year_index = i
        year = YEARS[i]
        x = get_x_coordinate(width=CANVAS_WIDTH, year_index=year_index)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for name in lookup_names:
        name_index = lookup_names.index(name)
        if name_index % 4 == 0:
            color = COLORS[0]
        elif name_index % 4 == 1:
            color = COLORS[1]
        elif name_index % 4 == 2:
            color = COLORS[2]
        elif name_index % 4 == 3:
            color = COLORS[3]

        for i in range(len(YEARS)):
            year_index = i
            year = YEARS[i]
            x = get_x_coordinate(width=CANVAS_WIDTH, year_index=year_index)
            if str(year) in name_data[name]:
                rank = name_data[name][str(year)]
                y = int(int(CANVAS_HEIGHT) - int(GRAPH_MARGIN_SIZE) * 2) / 1000 * int(rank)
                canvas.create_text(x + TEXT_DX, int(GRAPH_MARGIN_SIZE) + int(y), text=f'{name} {rank}', anchor=tkinter.SW, fill=color)
            else:
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2
                canvas.create_text(x + TEXT_DX, int(GRAPH_MARGIN_SIZE) + int(y), text=f'{name} *', anchor=tkinter.SW, fill=color)

            year_index_1 = i-1
            year_1 = YEARS[i-1]
            x_1 = get_x_coordinate(width=CANVAS_WIDTH, year_index=year_index_1)
            if str(year_1) in name_data[name]:
                rank_1 = name_data[name][str(year_1)]
                y_1 = int(int(CANVAS_HEIGHT) - int(GRAPH_MARGIN_SIZE) * 2) / 1000 * int(rank_1)
            else:
                y_1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2

            if i >= 1:
                canvas.create_line(int(x_1),  int(GRAPH_MARGIN_SIZE) + int(y_1), int(x), int(GRAPH_MARGIN_SIZE) + int(y), width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
