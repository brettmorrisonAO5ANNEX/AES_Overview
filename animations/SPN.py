from manim import *

class SPN_Scene(Scene):
    def construct(self):
        # intro
        spn_text = Text("1. Substitution-Permutation Networks (SPNs)", font_size=36).shift(UP * 0.5)
        fft_text = Text("2. Finite Field Theory", font_size=36).next_to(spn_text, DOWN).align_to(spn_text, LEFT)
        self.play(Write(spn_text))
        self.wait(1)
        self.play(Write(fft_text))
        self.wait(2)
        self.play(FadeOut(fft_text), spn_text.animate.to_edge(UP, buff=1))
        self.wait(1)

        #SPNs
        # TODO: switch to rectngles and align vertically +
        s_box_sq = Square(side_length = 2, color=BLUE, fill_opacity=0.5).shift(LEFT * 2)
        s_box_text = Text("S-Box", font_size=24).move_to(s_box_sq.get_center())
        s_box = VGroup(s_box_sq, s_box_text)

        p_box_sq = Square(side_length=2, color=YELLOW, fill_opacity=0.5).shift(RIGHT * 2)
        p_box_text = Text("P-Box", font_size=24).move_to(p_box_sq.get_center())
        p_box = VGroup(p_box_sq, p_box_text)

        self.play(Create(s_box))
        self.play(Create(p_box))
            
        self.wait(2)

