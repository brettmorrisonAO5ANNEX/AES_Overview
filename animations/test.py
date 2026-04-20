from manim import *
from extras import custom_colors

config.background_color = custom_colors.BACKGROUND_1
class TestScene(Scene):
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

        pt_text = Text("plaintext", font_size=28, color=WHITE).shift(LEFT * 4)
        ct_text = Text("ciphertext", font_size=28, color=WHITE).shift(RIGHT * 4)

        input_arrow = Arrow(pt_text.get_right(), s_box.get_left(), color=custom_colors.FOREGROUND_1)
        s_to_p_arrow = CurvedArrow(s_box.get_bottom(), p_box.get_bottom(), color=custom_colors.FOREGROUND_1)
        p_to_s_arrow = CurvedArrow(p_box.get_top(), s_box.get_top(), color=custom_colors.FOREGROUND_1)
        output_arrow = Arrow(p_box.get_right(), ct_text.get_left(), color=custom_colors.FOREGROUND_1)

        self.play(FadeIn(s_box),
                  FadeIn(p_box))
        self.wait(1)

        self.play(FadeIn(pt_text),
                  FadeIn(ct_text))
        self.wait(1)

        self.play(GrowArrow(input_arrow))
        self.play(Create(s_to_p_arrow))
        self.play(Create(p_to_s_arrow))
        self.play(GrowArrow(output_arrow))
        self.wait(1)

        #----------- SECTION 3 -----------#
        # S-Box intro
        self.next_section(skip_animations=1)
        #---------------------------------#
        self.play(FadeOut(pt_text),
                  FadeOut(ct_text),
                  FadeOut(p_box),
                  FadeOut(input_arrow),
                  FadeOut(s_to_p_arrow),
                  FadeOut(p_to_s_arrow),
                  FadeOut(output_arrow),
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
        self.next_section(skip_animations=0)
        #---------------------------------#
        p_box.move_to(ORIGIN)
        self.play(FadeOut(original_sub_group),
                  FadeOut(green_rect),
                  FadeOut(invalid_sub_group),
                  FadeOut(red_rect),
                  FadeOut(output_arrow_1),
                  FadeOut(output_byte_1),
                  FadeIn(p_box), run_time=1)
        
        # create input and output bytes for P-Box 
        input_byte = MathTable([["b_0", "b_1", "b_2", "b_3", "b_4", "b_5", "b_6", "b_7"]], 
                               include_outer_lines=True,
                               v_buff=1,
                               h_buff=1).shift(UP * 1.75).scale(0.5)
        input_byte.get_entries_without_labels().set_color(BLACK)
        input_colors = [custom_colors.ORANGE, custom_colors.RED, custom_colors.PINK, custom_colors.PURPLE,
                  custom_colors.BLUE, custom_colors.CYAN, custom_colors.TURQUOISE, custom_colors.GREEN]
        
        output_byte = MathTable([["b_6", "b_2", "b_5", "b_1", "b_7", "b_4", "b_0", "b_3"]], 
                               include_outer_lines=True,
                               v_buff=1,
                               h_buff=1).shift(DOWN * 1.75).scale(0.5)
        output_byte.get_entries_without_labels().set_color(BLACK)
        output_colors = [custom_colors.TURQUOISE, custom_colors.PINK, custom_colors.CYAN, custom_colors.RED,
                         custom_colors.GREEN, custom_colors.BLUE, custom_colors.ORANGE, custom_colors.PURPLE]

        # fill input with ordered colors, output with permutation colors
        for i in range(8):
            input_byte.add_highlighted_cell((1, i+1), color=input_colors[i], fill_opacity=1)
            output_byte.add_highlighted_cell((1, i+1), color=output_colors[i], fill_opacity=1)

        perm_box = RoundedRectangle(corner_radius=0.25, height=1, width=4.5, color=custom_colors.FOREGROUND_1).move_to(ORIGIN + LEFT * 4)

        input_byte_copy = input_byte.copy()
        output_byte_copy = output_byte.copy().scale(0.75).move_to(perm_box.get_center())

        input_arrow = Arrow(input_byte.get_bottom(), p_box.get_top(), color=custom_colors.FOREGROUND_1)
        func_arrow = Arrow(p_box.get_left(), perm_box.get_right(), color=custom_colors.FOREGROUND_1)
        output_arrow = Arrow(p_box.get_bottom(), output_byte.get_top(), color=custom_colors.FOREGROUND_1)

        self.play(FadeIn(input_byte),
                  FadeIn(perm_box))
        self.play(GrowArrow(input_arrow))
        self.play(GrowArrow(func_arrow),
                  input_byte_copy.animate.move_to(perm_box.get_center()).scale(0.75))
        self.play(Transform(input_byte_copy, output_byte_copy))
        self.play(GrowArrow(output_arrow),
                  FadeOut(input_byte_copy),
                  FadeOut(output_byte_copy),
                  Transform(output_byte_copy, output_byte))
        

        
        
        

        
        











        




        