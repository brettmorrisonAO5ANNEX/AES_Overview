from manim import *
from extras import custom_colors

config.background_color = custom_colors.BACKGROUND_1
class FFT_Scene(Scene):
    def construct(self):

        #----------- SECTION 1 -----------#
        # intro text
        self.next_section(skip_animations=0)
        #---------------------------------#

        spn_text = Text("1. Substitution Permutation Networks", font_size=32, color=WHITE)
        finite_field_text = Text("2. Finite Field Theory", font_size=32, color=WHITE).next_to(spn_text, DOWN).align_to(spn_text, LEFT)
        text_group = VGroup(spn_text, finite_field_text).move_to(ORIGIN)
        finite_field_text.scale(0.75).to_edge(UP + LEFT, buff=0.75)
        self.add(finite_field_text)

        standard_field_circle = Circle(radius=1.5, color=custom_colors.TURQUOISE, fill_opacity=0.5)
        sub_elem_labels = ['a', 'b', 'c', 'd', 'e', 'f', '...']
        center = standard_field_circle.get_center()
        sub_elem_points = [(center),
                           (center + LEFT * 0.5 + UP),
                           (center + RIGHT * 1.2 + UP * 0.4),
                           (center + UP * 1.3),
                           (center + LEFT * 0.8 + DOWN * 0.7),
                           (center + RIGHT * 0.6 + DOWN * 0.8),
                           (center + LEFT * 0.9 + UP * 0.1)]
        sub_elems = VGroup()
        for i in range(7):
            p = Dot(sub_elem_points[i], color=custom_colors.TURQUOISE)
            p_t = MathTex(f"{sub_elem_labels[i]}").scale(0.75).move_to(p.get_bottom() + DOWN * 0.2)
            elem = VGroup(p, p_t)
            sub_elems.add(elem)
        standard_field = VGroup(standard_field_circle, sub_elems)

        standard_field_def = MathTex(r"E = \left\{ a,\ b,\ c,\ d,\ e,\ f,\ ... \right\}").move_to(
            standard_field.get_bottom() + DOWN * 0.5)
        #standard_field_ops = MathTex(r"f = \left\{+,\ -,\ \ast,\ \div \right\}").move_to(
        #    standard_field_def.get_bottom() + DOWN * 0.5).align_to(standard_field_def, LEFT)

        self.play(FadeIn(standard_field_circle))
        for i in range(7):
            self.play(FadeIn(sub_elems[i]), run_time=0.25)
        self.play(Write(standard_field_def))
        #self.play(Write(standard_field_ops))



