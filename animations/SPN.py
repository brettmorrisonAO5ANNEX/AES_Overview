from manim import *

class SPN_Scene(Scene):
    def construct(self):
        #-------- SECTION MARKER 1 --------#
        self.next_section(skip_animations=1)

        # intro
        spn_text = Text("1. Substitution-Permutation Networks (SPNs)", font_size=36).shift(UP * 0.5)
        fft_text = Text("2. Finite Field Theory", font_size=36).next_to(spn_text, DOWN).align_to(spn_text, LEFT)
        self.play(Write(spn_text))
        self.wait(1)
        self.play(Write(fft_text))
        self.wait(2)
        self.play(FadeOut(fft_text), spn_text.animate.scale(0.75).to_edge(UP + LEFT, buff=0.75))
        self.wait(1)

        #-------- SECTION MARKER 2 --------#   
        self.next_section(skip_animations=1)

        #SPNs
        cipher = Rectangle(width=2.5, height = 2.5, color=GRAY, fill_opacity=0.5)
        cipher_group = VGroup(cipher)

        s_box_sq = Rectangle(width=2, height=0.8, color=BLUE, fill_opacity=1)
        s_box_text = Text("S-Box", font_size=20, color=BLACK).move_to(s_box_sq.get_center())
        s_box = VGroup(s_box_sq, s_box_text)

        p_box_sq = Rectangle(width=2, height=0.8, color=YELLOW, fill_opacity=1).move_to(s_box.get_bottom() + DOWN * 0.75)
        p_box_text = Text("P-Box", font_size=20, color=BLACK).move_to(p_box_sq.get_center())
        p_box = VGroup(p_box_sq, p_box_text)

        spn_comp_group = VGroup(s_box, p_box).move_to(cipher.get_center())
        cipher_group.add(spn_comp_group)

        plaintext = Circle(radius=0.4, color=GRAY, fill_opacity=0.5).move_to(cipher.get_left() + LEFT * 1.5)
        plaintext_text = Text("PT", font_size=24).move_to(plaintext.get_center())
        plaintext_group = VGroup(plaintext, plaintext_text)

        ciphertext = Circle(radius=0.4, color=GRAY, fill_opacity=0.5).move_to(cipher.get_right() + RIGHT * 1.5)
        ciphertext_text = Text("CT", font_size=24).move_to(ciphertext.get_center())
        ciphertext_group = VGroup(ciphertext, ciphertext_text)

        cipher_extras = VGroup(plaintext_group, ciphertext_group)
        enter_line = Line(plaintext_group.get_right(), cipher_group.get_left(), color=WHITE)
        exit_line = Line(cipher_group.get_right(), ciphertext_group.get_left(), color=WHITE)
        cipher_extras.add(enter_line)
        cipher_extras.add(exit_line)

        self.play(FadeIn(cipher_group))
        self.play(FadeIn(cipher_extras))

        #-------- SECTION MARKER 3 --------#
        self.next_section(skip_animations=0)

        #TODO: animate PT entering the cipher

        state = MathTable([["FF", "FF", "FF", "FF"],
                           ["FF", "FF", "FF", "FF"],
                           ["FF", "FF", "FF", "FF"],
                           ["FF", "FF", "FF", "FF"]]).move_to(cipher.get_center())



        self.play(ReplacementTransform(spn_comp_group, state))
        self.wait(2)

