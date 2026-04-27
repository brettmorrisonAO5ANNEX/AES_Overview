from manim import *


# a class to represent a cell in a movable table object
# a cell has coordinates, a label, and a rectangle mobject that can be colored
class MovableCell(VGroup):
    def __init__(self, coordinates, label, width=0.75, height=0.75):
        super().__init__()
        self.coordinates = coordinates

        cell_rect = Rectangle(width=width, height=height, color=WHITE, fill_opacity=0)
        cell_label = MathTex(label, font_size=24).move_to(cell_rect.get_center())                 
        self.add(cell_rect, cell_label) 

    def color_cell(self, color, opacity=0.5):
        # access the cell_rect VMobject for coloring
        self[0].set_fill(color, opacity=opacity)


# a class to represent a table with movable cells
class MovableTable(VGroup):
    # create a table with given cell labels and dimensions
    # cell_labels should be a 2D list of Latex strings
    # no fill color by default
    #
    # cells are stored in a dictionary by their cell numbers
    def __init__(self, cell_labels, rows, cols, cell_width=0.75, cell_height=0.75):
        super().__init__()
        self.num_rows = rows
        self.num_cols = cols

        # size and position reference for cell placement and movement
        # added to self so reference is updated if table is moved or scaled
        reference_rect = Rectangle(width=cols*cell_width, height=rows*cell_height, 
                                   color=WHITE, fill_opacity=0)
        self.reference_rect = reference_rect
        self.add(reference_rect)

        self.cells = {}
        for r in range(rows):
            for c in range(cols):
                cell = MovableCell((r, c), cell_labels[r][c], width=cell_width, height=cell_height)
                cell.move_to(self.coords_to_point((r, c)))

                # store cell in dictionary based on cell number
                cell_num = r * cols + c
                self.cells[cell_num] = cell
                self.add(cell)
    
        # center table at the origin
        self.move_to(ORIGIN)
    
    # converts relative cell coordinates to absolute screen position
    def coords_to_point(self, coords):
        r, c = coords

        # reference point for cell placement
        cell_height = self.reference_rect.height / self.num_rows 
        cell_width = self.reference_rect.width / self.num_cols
        v_shift = (self.reference_rect.get_top() + DOWN * (cell_height / 2))
        h_shift = (self.reference_rect.get_left() + RIGHT * (cell_width / 2))
        top_left_cell = v_shift + h_shift

        # destination is center of cell at (r, c)
        dest_point = top_left_cell + RIGHT * (c * cell_width) + DOWN * (r * cell_height)
        return dest_point

    # returns an animation of the specified cell moving 
    # to the table destination coordinates linearly
    def linear_move_cell(self, cell_num, dest_coords):
        dest_pos = self.coords_to_point(dest_coords)
        cell = self.cells[cell_num]

        #update cell coordinates
        cell.coordinates = dest_coords

        return cell.animate.move_to(dest_pos)
    
    def non_linear_move_cell(self, cell_num, dest_coords, path_arc):
        dest_post = self.coords_to_point(dest_coords)
        cell = self.cells[cell_num]

        #update cell coordinates
        cell.coordinates = dest_coords

        return MoveAlongPath(cell, path_arc, rate_func=linear)
            
# Test Scene for debugging
class MovableTableScene(Scene):
    def construct(self):
        cell_labels = [[r"b_0", r"b_1", r"b_2", r"b_3"],
                       [r"b_4", r"b_5", r"b_6", r"b_7"],
                       [r"b_8", r"b_9", r"b_{10}", r"b_{11}"],
                       [r"b_{12}", r"b_{13}", r"b_{14}", r"b_{15}"]]
        table = MovableTable(cell_labels, rows=4, cols=4)
        table.cells[0].color_cell(RED, opacity=1)

        self.play(FadeIn(table))

        arc1 = ArcBetweenPoints(table.cells[0].get_center(), table.cells[10].get_center(), angle=-PI/2)
        arc2 = ArcBetweenPoints(table.cells[10].get_center(), table.cells[0].get_center(), angle=-PI/2)

        self.play(table.non_linear_move_cell(0, (2, 2), arc1),
                  table.non_linear_move_cell(10, (0, 0), arc2))
        self.wait(1)
        
                                                                           
