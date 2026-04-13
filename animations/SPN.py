from manim import *

#---- GLOBALS ----#
colors = [BLUE_A, GREEN_A, YELLOW_A, RED_A,
          BLUE_B, GREEN_B, YELLOW_B, RED_B,
          BLUE_C, GREEN_C, YELLOW_C, RED_C,
          BLUE_D, GREEN_D, YELLOW_D, RED_D]

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

        # size of SPN components are relative to this table
        state = MathTable([["b_{00}", "b_{04}", "b_{08}", "b_{12}"],
                           ["b_{01}", "b_{05}", "b_{09}", "b_{13}"],
                           ["b_{02}", "b_{06}", "b_{10}", "b_{14}"],
                           ["b_{03}", "b_{07}", "b_{11}", "b_{15}"]],
                           include_outer_lines=True,
                           v_buff=1,
                           h_buff=1).scale(0.5)
        state.get_entries_without_labels().set_color(BLACK)
        
        #SPNs
        cipher = Rectangle(width=state.get_width() + 0.5, height=state.get_height() + 0.5, color=GRAY, fill_opacity=0.5)
        cipher_group = VGroup(cipher)

        s_box_sq = Rectangle(width=state.get_width(), height=(state.get_height() / 2) - 0.25, color=BLUE, fill_opacity=1)
        s_box_text = Text("S-Box", font_size=20, color=BLACK).move_to(s_box_sq.get_center())
        s_box = VGroup(s_box_sq, s_box_text)

        p_box_sq = Rectangle(width=state.get_width(), height=(state.get_height() / 2) - 0.25, color=YELLOW, fill_opacity=1).move_to(s_box.get_bottom() + DOWN)
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

        # animate state jumbling
        # 1. init state
        self.play(FadeOut(spn_comp_group))
        initialize_state(state)
        self.play(FadeIn(state))

        # 2. animate color changes
        rnd = RandomColorGenerator(sample_colors=colors)
        for _ in range(3):
            animations = update_state(rnd, state)
            self.play(*animations, run_time=1)
            self.wait(0.5)

        # 3. update a round counter
    





#---- HELPERS ----#
def initialize_state(state):
    for r in range(4):
        for c in range(4):
            state.add_highlighted_cell((r+1, c+1), color=colors[r*4 + c])

def update_state(rnd, state):
    animations = []

    for r in range(4):
        for c in range(4):
            cell = state.get_highlighted_cell((r+1, c+1))
            animations.append(
                cell.animate.set_fill(rnd.next())
            )
    return animations