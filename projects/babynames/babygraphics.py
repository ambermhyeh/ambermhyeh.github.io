"""
File: babygraphics.py
Name: Amber Yeh
--------------------------------
This program is part of the SC101 Baby Names Project.

It is adapted from Nick Parlante's Baby Names assignment
and has been modified by Jerry Liao to align with the
learning objectives of the stanCode SC101 course.
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
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, this function returns the x coordinate
    of the vertical line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    vertical_spacing = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)  # The spacing of each vertical line
    x_coordinate = int(GRAPH_MARGIN_SIZE + vertical_spacing * year_index)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Draw 2 horizontal lines #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, (CANVAS_WIDTH - GRAPH_MARGIN_SIZE), GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), (CANVAS_WIDTH - GRAPH_MARGIN_SIZE),
                       (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), width=LINE_WIDTH)
    # Draw vertical lines according to list Year#
    width = CANVAS_WIDTH
    for i in range(len(YEARS)):
        x = get_x_coordinate(width, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE) + TEXT_DX, text=str(YEARS[i]),
                           anchor=tkinter.NW)


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
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    width = CANVAS_WIDTH
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        color = COLORS[i % len(COLORS)]
        for j in range(len(YEARS)):  # j = 0, 1, 2, ..., total number of years
            year = str(YEARS[j])
            rank, text = get_rank_and_text(year, name, name_data)
            x = get_x_coordinate(width, j)
            y = get_y_coordinate(rank)
            # create a text for the rank of the name in the current year.
            canvas.create_text(x + TEXT_DX, y - TEXT_DX, text=text,
                               anchor=tkinter.SW, fill=color)
            if j > 0:
                # when j > 0, draw a line starting from the rank of the previous year to the rank of the current year.
                canvas.create_line(prev_x, prev_y, x, y, width=LINE_WIDTH, fill=color)
            prev_x = x
            prev_y = y


def get_rank_and_text(year, name, name_data):
    """
    Args:
        year (str): The indexed year from the YEARS list
        name (str): The indexed name from the lookup_names list
        name_data (dict): Dictionary holding baby name data

    Returns:
        rank (str): The rank of the indexed name and year in the name_data dictionary.
                    If the rank does not exist, return MAX_RANK
        text (str): "{The name to look up} {rank}"
                    If the rank does not exist, return "{The name to look up} *"
    """
    if year in name_data[name]:
        rank = name_data[name][year]
        text = f'{name} {rank}'
    else:
        rank = MAX_RANK
        text = f'{name} *'
    return rank, text


def get_y_coordinate(rank):
    """
    Args:
        rank (str): The rank of the indexed name and year in the name_data dictionary.
    Returns:
        y_coordinate (float): The y coordinate of the plot associated with the indexed year.
    """
    y_coordinate = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK * int(rank)
    return y_coordinate


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
