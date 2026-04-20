from manim import *

#TODO:
# create table
# define a grid system relative to top left corner of table
# create function to move cell from one position to another

class MovableCell(VGroup):
    cell = None
    coordinates = None
    
    def __init__(self, coordinates, label, width=0.75, height=0.75):
        cell_rect = Rectangle(width=width, height=height, color=WHITE, fill_opacity=0)
        cell_label = MathTex(label, font_size=24).move_to(cell_rect.get_center())
        self.cell = VGroup(cell_rect, cell_label)
        self.coordinates = coordinates

    def color_cell(self, color, opacity=0.5):
        self.cell[0].set_fill(color, opacity=opacity)

# a class to represent a table with movable cells
class MovableTable(VGroup):
    # create a table with given cell labels and dimensions
    # cell_labels should be a 2D list of Latex strings
    # no fill color by default
    #
    # each element in returned VGroup is a cell with its
    # corresponding coordinates in the table
    def create_movable_table(cell_labels, rows, cols, cell_width=0.75, cell_height=0.75):
        movable_table = VGroup()
        for r in range(rows):
            for c in range(cols):
                table_element = MovableCell((r, c), cell_labels[r][c], 
                                   width=cell_width, height=cell_height)
                table_element.cell.move_to(RIGHT * (c * cell_width) +
                            DOWN * (r * cell_height))
                movable_table.add(table_element)
        return movable_table.move_to(ORIGIN)
    





            

class MovableTableScene(Scene):
    def construct(self):
        cell_labels = [[r"b_0", r"b_1", r"b_2", r"b_3"],
                       [r"b_4", r"b_5", r"b_6", r"b_7"],
                       [r"b_8", r"b_9", r"b_{10}", r"b_{11}"],
                       [r"b_{12}", r"b_{13}", r"b_{14}", r"b_{15}"]]
        table = MovableTable.create_movable_table(cell_labels, rows=4, cols=4)
        self.play(FadeIn(table))
                                                                           
