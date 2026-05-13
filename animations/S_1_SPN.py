from manim import *
from extras import custom_colors
import extras.movable_table as mt

config.background_color = custom_colors.BACKGROUND_1
class SPN_Scene(Scene):
    def construct(self):
        
        #----------- SECTION 1 -----------#
        # intro text
        self.next_section(skip_animations=1)
        #---------------------------------#

        spn_text = Text("1. Substitution Permutation Networks", font_size=32, color=WHITE)
        finite_field_text = Text("2. Finite Field Theory", font_size=32, color=WHITE).next_to(spn_text, DOWN).align_to(spn_text, LEFT)
        text_group = VGroup(spn_text, finite_field_text).move_to(ORIGIN)

        self.play(Write(text_group), run_time=2)
        self.wait(1)
        self.play(FadeOut(finite_field_text), spn_text.animate.scale(0.75).to_edge(UP + LEFT, buff=0.75))
        self.wait(1)

        #----------- SECTION 2 -----------#
        # SPN introduction
        self.next_section(skip_animations=1)
        #---------------------------------#
        s_box_circle = Circle(radius=0.5, color=custom_colors.ORANGE, fill_opacity=0.5)
        s_box_text = Text("S", font_size=30, slant=ITALIC, color=WHITE).move_to(s_box_circle.get_center())
        s_box = VGroup(s_box_circle, s_box_text).shift(LEFT)

        p_box_circle = Circle(radius=0.5, color=custom_colors.BLUE, fill_opacity=0.5)
        p_box_text = Text("P", font_size=30, slant=ITALIC, color=WHITE).move_to(p_box_circle.get_center())
        p_box = VGroup(p_box_circle, p_box_text).shift(RIGHT)

        pt_text = Text("plaintext", font_size=28, color=WHITE)
        pt_text.add_updater(lambda m: m.next_to(s_box, LEFT, buff=2))
        ct_text = Text("ciphertext", font_size=28, color=WHITE)
        ct_text.add_updater(lambda m: m.next_to(p_box, RIGHT, buff=2))

        spn_input_arrow = Arrow(pt_text.get_right() + RIGHT * 0.25, 
                                s_box.get_left(), 
                                color=custom_colors.FOREGROUND_1, buff=0)
        spn_input_arrow.add_updater(lambda m: m.put_start_and_end_on(
            pt_text.get_right() + RIGHT * 0.25,
            s_box.get_left()
        ))
        s_to_p_arrow = CurvedArrow(s_box.get_bottom(), 
                                   p_box.get_bottom(), 
                                   color=custom_colors.FOREGROUND_1)
        s_to_p_arrow.add_updater(lambda m: m.put_start_and_end_on(
            s_box.get_bottom(),
            p_box.get_bottom()
        ))
        p_to_s_arrow = CurvedArrow(p_box.get_top(), 
                                   s_box.get_top(), 
                                   color=custom_colors.FOREGROUND_1)
        p_to_s_arrow.add_updater(lambda m: m.put_start_and_end_on(
            p_box.get_top(),
            s_box.get_top()
        ))
        spn_output_arrow = Arrow(p_box.get_right(),
                                 ct_text.get_left() + LEFT * 0.25,
                                 color=custom_colors.FOREGROUND_1, buff=0)
        spn_output_arrow.add_updater(lambda m: m.put_start_and_end_on(
            p_box.get_right(), 
            ct_text.get_left() + LEFT * 0.25
        ))

        #TODO: create bracket with 'n rounds' under the s-p cycle
        round_brace = BraceBetweenPoints(s_box.get_left(), p_box.get_right()).shift(DOWN)
        round_brace_txt = MathTex(r"n\ rounds").move_to(round_brace.get_bottom() + DOWN * 0.25)
        brace = VGroup(round_brace, round_brace_txt)

        self.play(FadeIn(s_box),
                  FadeIn(p_box))
        self.play(FadeIn(pt_text),
                  FadeIn(ct_text))
        self.play(Create(spn_input_arrow))
        self.play(FadeIn(brace))
        self.play(Create(s_to_p_arrow))
        self.play(Create(p_to_s_arrow))
        self.play(Create(spn_output_arrow))
        self.wait(1)

        #----------- SECTION 3 -----------#
        # S-Box intro
        self.next_section(skip_animations=1)
        #---------------------------------#
        self.play(FadeOut(pt_text),
                  FadeOut(ct_text),
                  FadeOut(p_box),
                  FadeOut(spn_input_arrow),
                  FadeOut(s_to_p_arrow),
                  FadeOut(p_to_s_arrow),
                  FadeOut(spn_output_arrow),
                  FadeOut(brace),
                  s_box.animate.move_to(ORIGIN))

        sub_table_rect = RoundedRectangle(corner_radius=0.25, height=1, width=2, color=custom_colors.RED, fill_opacity=0)
        separator = Line(sub_table_rect.get_top(), sub_table_rect.get_bottom(), color=custom_colors.RED)
        sub_table = VGroup(sub_table_rect, separator).shift(DOWN * 1.5)

        input_byte = MathTex(r"\left\{ b\right\}").shift(LEFT * 3)
        output_byte_0 = MathTex(r"\left\{ b_0'\right\}").move_to(sub_table.get_center() + RIGHT * 0.5)
        output_byte_1 = MathTex(r"\left\{ b_1'\right\}").shift(RIGHT * 3)

        input_arrow = Arrow(input_byte.get_right(), s_box.get_left(), color=custom_colors.FOREGROUND_1)
        output_arrow = Arrow(s_box.get_right(), output_byte_1.get_left(), color=custom_colors.FOREGROUND_1)

        self.play(FadeIn(input_byte),
                  FadeIn(sub_table),
                  FadeIn(output_byte_0))

        input_byte_copy = input_byte.copy()

        self.play(GrowArrow(input_arrow))
        self.play(input_byte_copy.animate.move_to(sub_table.get_center() + LEFT * 0.5))
        self.play(GrowArrow(output_arrow),
                  output_byte_0.animate.move_to(s_box.get_center() + RIGHT * 3))

        #----------- SECTION 4 -----------#
        # S-Box properties
        self.next_section(skip_animations=1)
        #---------------------------------#
        self.play(FadeOut(sub_table),
                  FadeOut(input_byte_copy))
        
        original_sub_group = VGroup(input_byte, input_arrow, s_box, output_arrow, output_byte_0)
        green_rect = RoundedRectangle(corner_radius=0.25, width=8, height=1.5, color=custom_colors.GREEN, fill_opacity=0).shift(UP * 1.5)

        invalid_sub_group = original_sub_group.copy().shift(DOWN * 1.5)
        red_rect = RoundedRectangle(corner_radius=0.25, width=8, height=3, color=custom_colors.RED, fill_opacity=0).shift(DOWN * 1.5)

        # redefine group elements for non-one to one animation
        invalid_sub_group[2][0].set_color(color=custom_colors.RED)
        output_byte_1.move_to(invalid_sub_group[4].get_center() + DOWN)
        output_arrow_1 = Arrow(invalid_sub_group[2].get_right(), output_byte_1.get_left(), color=custom_colors.FOREGROUND_1)
        invalid_sub_group[3] = always_redraw(
            lambda: Arrow(invalid_sub_group[2].get_right(), invalid_sub_group[4].get_left(), color=custom_colors.FOREGROUND_1))
                                             
        self.play(original_sub_group.animate.shift(UP * 1.5),
                  FadeIn(green_rect))
        self.play(FadeIn(invalid_sub_group),
                  FadeIn(red_rect))
        self.play(invalid_sub_group[4].animate.shift(UP),
                  GrowArrow(output_arrow_1),
                  FadeIn(output_byte_1))
        
        #----------- SECTION 5 -----------#
        # P-Box properties
        self.next_section(skip_animations=1)
        #---------------------------------#
        p_box.move_to(ORIGIN)
        self.play(FadeOut(original_sub_group),
                  FadeOut(green_rect),
                  FadeOut(invalid_sub_group),
                  FadeOut(red_rect),
                  FadeOut(output_arrow_1),
                  FadeOut(output_byte_1),
                  FadeIn(p_box), run_time=1)
        
        # create byte table with movable cells for P-Box demonstration
        byte_colors = [custom_colors.ORANGE, custom_colors.RED, custom_colors.PINK, custom_colors.PURPLE,
                       custom_colors.BLUE, custom_colors.CYAN, custom_colors.TURQUOISE, custom_colors.GREEN]
        byte_cells = [[r"b_0", r"b_1", r"b_2", r"b_3",
                       r"b_4", r"b_5", r"b_6", r"b_7"]]
        input_byte = mt.MovableTable(byte_cells, rows=1, cols=8).move_to(p_box.get_center() + UP * 2)
        for i in range(8):
            input_byte.cells[i].color_cell(byte_colors[i], opacity=1)

        perm_box = RoundedRectangle(corner_radius=0.25, height=1, width=5, color=custom_colors.FOREGROUND_1).move_to(ORIGIN + LEFT * 4)

        intermediate_byte = input_byte.copy()
        input_arrow = Arrow(input_byte.get_bottom(), p_box.get_top(), color=custom_colors.FOREGROUND_1)
        func_line = Line(p_box.get_left(), perm_box.get_right(), color=custom_colors.FOREGROUND_1)
        func_text = MathTex(r"f", font_size=28).move_to(func_line.get_center() + UP * 0.25)
    
        self.play(FadeIn(input_byte),
                  FadeIn(perm_box))
        self.play(GrowArrow(input_arrow))
        self.play(Create(func_line),
                  Write(func_text))
        self.play(intermediate_byte.animate.move_to(perm_box.get_center()).scale(0.75),
                  input_byte.animate.set_opacity(0.1))
        
        # permute intermediate byte to output byte
        movement_map = [(0, (0, 6)), (1, (0, 7)), (2, (0, 4)), (3, (0, 0)),
                        (4, (0, 1)), (5, (0, 2)), (6, (0, 5)), (7, (0, 3))]
        self.play(*intermediate_byte.move_cells(movement_map, 
                                                rate_func=rate_functions.ease_in_out_cubic),
                                                run_time=1)
        self.wait(1)
        
        intermediate_byte_copy = intermediate_byte.copy()
        output_byte = intermediate_byte.copy().scale(1.25).move_to(p_box.get_center() + DOWN * 2)
        output_arrow = Arrow(p_box.get_bottom(), output_byte.get_top(), color=custom_colors.FOREGROUND_1)

        self.play(Transform(intermediate_byte_copy, output_byte),
                  GrowArrow(output_arrow),
                  intermediate_byte.animate.set_opacity(0.1))
        self.wait(1)

        #----------- SECTION 6 -----------#
        # Round-key addition
        self.next_section(skip_animations=1)
        #---------------------------------#
        self.play(FadeOut(input_byte, input_arrow, func_line, func_text, 
                          intermediate_byte, perm_box, output_arrow, intermediate_byte_copy))

        s_box.move_to(ORIGIN + LEFT + DOWN * 0.5)
        self.play(p_box.animate.shift(RIGHT + DOWN * 0.5),
                  FadeIn(s_box, pt_text, ct_text))

        self.play(Create(spn_input_arrow))

        brace.shift(DOWN*0.5)
        self.play(FadeIn(brace))
        self.play(Create(s_to_p_arrow))
        self.play(Create(p_to_s_arrow))
        self.play(Create(spn_output_arrow))

        first_round_key = MathTex(r"\left\{ k_0\right\}").move_to(spn_input_arrow.get_center() + UP * 2)
        rest_round_key = MathTex(r"\left\{ k_i\right\}").shift(UP * 1.5)

        xor_circ = Circle(radius=0.15, color=custom_colors.FOREGROUND_1, fill_opacity=0)
        xor_line_1 = Line(xor_circ.get_left(), xor_circ.get_right(), color=custom_colors.FOREGROUND_1)
        xor_line_2 = Line(xor_circ.get_top(), xor_circ.get_bottom(), color=custom_colors.FOREGROUND_1)
        xor_elem = VGroup(xor_circ, xor_line_1, xor_line_2)

        first_xor = xor_elem.copy().move_to(spn_input_arrow.get_center())  
        first_round_xor = VGroup(first_xor,
                                 Line(first_round_key.get_bottom(), first_xor.get_top(), color=custom_colors.FOREGROUND_1))
        
        rest_xor = xor_elem.copy().move_to(p_to_s_arrow.get_top())
        # remove horizontal line in XOR to match curve of arrow
        rest_xor.remove(rest_xor[1])
        rest_round_xor = VGroup(rest_xor,
                                Line(rest_round_key.get_bottom(), rest_xor.get_top(), color=custom_colors.FOREGROUND_1))

        self.play(FadeIn(first_round_key, first_round_xor))
        self.play(FadeIn(rest_round_key, rest_round_xor))
        self.wait(1)
                  
        #----------- SECTION 7 -----------#
        # SPN decryption
        self.next_section(skip_animations=1)
        #---------------------------------#
        input_start, input_end = spn_input_arrow.get_start_and_end()
        s_to_p_start, s_to_p_end = s_to_p_arrow.get_start_and_end()
        p_to_s_start, p_to_s_end = p_to_s_arrow.get_start_and_end()
        output_start, output_end = spn_output_arrow.get_start_and_end()

        spn_input_arrow.clear_updaters()
        s_to_p_arrow.clear_updaters()
        p_to_s_arrow.clear_updaters()
        spn_output_arrow.clear_updaters()

        new_s_to_p = CurvedArrow(s_to_p_end, s_to_p_start, angle=-s_to_p_arrow.angle, color=custom_colors.FOREGROUND_1)
        new_p_to_s = CurvedArrow(p_to_s_end, p_to_s_start, angle=-p_to_s_arrow.angle, color=custom_colors.FOREGROUND_1)

        self.play(spn_input_arrow.animate.put_start_and_end_on(input_end, input_start),
                  ReplacementTransform(s_to_p_arrow, new_s_to_p),
                  ReplacementTransform(p_to_s_arrow, new_p_to_s),
                  spn_output_arrow.animate.put_start_and_end_on(output_end, output_start))
        self.wait(1)

        #----------- SECTION 8 -----------#
        # Finite Field Theory
        self.next_section(skip_animations=0)
        #---------------------------------#
        self.play(FadeOut(s_box, p_box, ct_text, pt_text, spn_input_arrow, spn_output_arrow,
                          new_s_to_p, new_p_to_s, first_round_xor, rest_round_xor,
                          first_round_key, rest_round_key, brace),
                  spn_text.animate.scale(1.25).move_to(finite_field_text.get_center() + UP).align_to(finite_field_text, LEFT), 
                  FadeIn(finite_field_text), run_time=1)
        self.wait(1)
        self.play(FadeOut(spn_text), finite_field_text.animate.scale(0.75).to_edge(UP + LEFT, buff=0.75))
        self.wait(1)



        

        
        
        

        
        











        




        