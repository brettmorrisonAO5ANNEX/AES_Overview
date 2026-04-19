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

        input_arrow = Arrow(pt_text.get_right(), s_box.get_left(), color=WHITE)
        s_to_p_arrow = CurvedArrow(s_box.get_bottom(), p_box.get_bottom())
        p_to_s_arrow = CurvedArrow(p_box.get_top(), s_box.get_top())
        output_arrow = Arrow(p_box.get_right(), ct_text.get_left())

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
        # SPN introduction
        self.next_section(skip_animations=0)
        #---------------------------------#
        self.play(FadeOut(pt_text),
                  FadeOut(ct_text),
                  FadeOut(p_box),
                  FadeOut(input_arrow),
                  FadeOut(s_to_p_arrow),
                  FadeOut(p_to_s_arrow),
                  FadeOut(output_arrow),
                  s_box.animate.move_to(ORIGIN))
        self.wait(1)

        sub_table_rect = RoundedRectangle(corner_radius=0.25, height=1, width=2, color=custom_colors.RED, fill_opacity=0)
        separator = Line(sub_table_rect.get_top(), sub_table_rect.get_bottom(), color=custom_colors.RED)
        sub_table = VGroup(sub_table_rect, separator).shift(DOWN * 1.5)

        input_byte = MathTex(r"\left\{ b\right\}").shift(LEFT * 3)
        output_byte_0 = MathTex(r"\left\{ b_0'\right\}").move_to(sub_table.get_center() + RIGHT * 0.5)
        output_byte_1 = MathTex(r"\left\{ b_1'\right\}").shift(RIGHT * 3)

        input_arrow = Arrow(input_byte.get_right(), s_box.get_left())
        output_arrow = Arrow(s_box.get_right(), output_byte_1.get_left())

        self.play(FadeIn(input_byte),
                  FadeIn(sub_table),
                  FadeIn(output_byte_0))

        input_byte_copy = input_byte.copy()

        self.play(GrowArrow(input_arrow))
        self.play(input_byte_copy.animate.move_to(sub_table.get_center() + LEFT * 0.5))
        self.play(GrowArrow(output_arrow),
                  output_byte_0.animate.move_to(s_box.get_center() + RIGHT * 3))











        




        