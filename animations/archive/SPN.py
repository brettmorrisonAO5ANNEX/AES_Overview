from manim import *

#---- GLOBALS ----#
colors = [BLUE_A, GREEN_A, YELLOW_A, RED_A,
          BLUE_B, GREEN_B, YELLOW_B, RED_B,
          BLUE_C, GREEN_C, YELLOW_C, RED_C,
          BLUE_D, GREEN_D, YELLOW_D, RED_D]

class SPN_Scene(Scene):
    def construct(self):
        #-------- SECTION MARKER 1 --------#
        # intro 
        self.next_section(skip_animations=0)

        spn_text = Text("1. Substitution-Permutation Networks (SPNs)", font_size=36).shift(UP * 0.5)
        fft_text = Text("2. Finite Field Theory", font_size=36).next_to(spn_text, DOWN).align_to(spn_text, LEFT)
        self.play(Write(spn_text))
        self.wait(1)
        self.play(Write(fft_text))
        self.wait(2)
        self.play(FadeOut(fft_text), spn_text.animate.scale(0.75).to_edge(UP + LEFT, buff=0.75))
        self.wait(1)
        
        #-------- SECTION MARKER 2 --------#
        # basic SPN structure
        self.next_section(skip_animations=0)

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

        s_box_sq = Rectangle(width=state.get_width(), height=(state.get_height() / 2) - 0.25, color=BLUE, fill_opacity=0.5)
        s_box_text = Text("S-Box", font_size=20, color=WHITE).move_to(s_box_sq.get_center())
        s_box = VGroup(s_box_sq, s_box_text)

        p_box_sq = Rectangle(width=state.get_width(), height=(state.get_height() / 2) - 0.25, color=YELLOW, fill_opacity=0.5).move_to(s_box.get_bottom() + DOWN)
        p_box_text = Text("P-Box", font_size=20, color=WHITE).move_to(p_box_sq.get_center())
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
        self.play(FadeOut(spn_comp_group))

        #-------- SECTION MARKER 3 --------#
        # jumbling plaintext in SPN
        #TODO: animate PT entering the cipher
        self.next_section(skip_animations=0)

        # animate state jumbling with round counter
        round_text = Text("Round: ", font_size=30)
        round_tracker = ValueTracker(0)
        round_counter = always_redraw(
            lambda: Text(
                f"{int(round_tracker.get_value())}", 
                font_size=30).move_to(round_text.get_right() + RIGHT * 0.25)
        )
        round_group = VGroup(round_text, round_counter).move_to(cipher.get_bottom() + DOWN * 0.5)

        # 1. init state
        init_state = state.copy()
        initialize_state(4, 4, init_state)
        self.play(FadeIn(init_state), FadeIn(round_group))
        
        # 2. animate color changes
        rnd = RandomColorGenerator(sample_colors=colors)
        prev_state = init_state

        for _ in range(4):
            (prev_state, animation) = update_state(4, 4, rnd, state, prev_state)
            self.play(round_tracker.animate.increment_value(1))
            self.play(animation)

        #---- SECTION MARKER 4 ----#
        # S-Box description
        self.next_section(skip_animations=0)

        self.play(FadeOut(prev_state),
                  FadeOut(round_group),
                  FadeIn(spn_comp_group))
        self.play(FadeOut(cipher_extras),
                  FadeOut(cipher),
                  FadeOut(p_box),
                  s_box.animate.move_to(ORIGIN))

        sub_function_circle = Circle(radius=0.4, color=GRAY, fill_opacity=0.5).move_to(s_box.get_center() + DOWN * 1.5)
        sub_function_text = Text("S", font_size=24, slant=ITALIC).move_to(sub_function_circle.get_center())
        sub_function_group = VGroup(sub_function_circle, sub_function_text)
        input_byte = MathTex(r"\left\{ b \right\}").scale(1.1).move_to(sub_function_group.get_left() + LEFT * 1.5)
        output_byte = MathTex(r"\left\{ b' \right\}").scale(1.1).move_to(sub_function_group.get_right() + RIGHT * 1.5)
        input_line = Line(input_byte.get_right() + RIGHT * 0.1, sub_function_circle.get_left(), color=WHITE)
        output_line = always_redraw(
            lambda: Line(sub_function_circle.get_right(), 
                         output_byte.get_left() + LEFT * 0.1, 
                         color=WHITE)
        )
        sub_group = VGroup(sub_function_group, input_byte, output_byte, input_line, output_line)

        self.play(FadeIn(input_byte), FadeIn(sub_function_group))
        self.wait(0.5)
        self.play(Create(input_line))
        self.wait(0.5)
        self.play(Create(output_line), FadeIn(output_byte))
        self.wait(2)
        self.play(FadeOut(s_box),
                  sub_group.animate.move_to(ORIGIN))
        
        alternate_byte = MathTex(r"\left\{ b'' \right\}").scale(1.1).move_to(output_byte.get_center() + DOWN)
        alternate_line = Line(sub_function_circle.get_right(), alternate_byte.get_left() + LEFT * 0.1, color=WHITE)
        red_rectangle = Rectangle(width=6, height=4, color=RED, fill_opacity=0)

        self.play(Create(red_rectangle))
        self.play(output_byte.animate.shift(UP))
        self.play(Create(alternate_line),
                  FadeIn(alternate_byte))
        self.wait(2)

        #---- SECTION MARKER 5 ----#
        # P-Box description
        self.next_section(skip_animations=0)

        p_box.move_to(ORIGIN)
        self.play(FadeOut(sub_group),
                  FadeOut(alternate_byte),
                  FadeOut(alternate_line),
                  FadeOut(red_rectangle),
                  FadeIn(p_box), run_time=1)
        self.wait(1)

        expanded_init_byte = MathTable([["b_{0}", "b_{1}", "b_{2}", "b_{3}",
                                         "b_{4}", "b_{5}", "b_{6}", "b_{7}"]],
                                        include_outer_lines=True,
                                        v_buff=1,
                                        h_buff=1).scale(0.5).move_to(p_box.get_center() + UP * 2)
        expanded_output_byte = MathTable([["b_{2}", "b_{5}", "b_{0}", "b_{7}",
                                           "b_{3}", "b_{1}", "b_{4}", "b_{6}"]],
                                          include_outer_lines=True,
                                          v_buff=1,
                                          h_buff=1).scale(0.5).move_to(p_box.get_center() + DOWN * 2)
        init_byte_colors = [BLUE_C, TEAL_C, GREEN_C, YELLOW_C, GOLD_C, RED_C, MAROON_C, PURPLE_C]
        output_byte_colors = [GREEN_C, RED_C, BLUE_C, PURPLE_C, YELLOW_C, TEAL_C, GOLD_C, MAROON_C]

        for i in range(8):
            expanded_init_byte.add_highlighted_cell((1, i+1), color=init_byte_colors[i])
            expanded_output_byte.add_highlighted_cell((1, i+1), color=output_byte_colors[i])

        input_line = Line(expanded_init_byte.get_bottom(), p_box.get_top(), color=WHITE)
        output_line = Line(p_box.get_bottom(), expanded_output_byte.get_top(), color=WHITE)
        self.play(FadeIn(expanded_init_byte),
                  Create(input_line))  
        self.wait(1)  

        pre_output_byte = expanded_init_byte.copy().move_to(expanded_output_byte.get_center())
        self.play(Create(output_line),
                  FadeIn(pre_output_byte))
        self.play(ReplacementTransform(pre_output_byte, expanded_output_byte))
        self.wait(2)

        permutated_byte_group = VGroup(expanded_init_byte, input_line, expanded_output_byte, output_line)
        self.play(FadeOut(permutated_byte_group))

        #---- SECTION MARKER 6 ----#
        # Round Key Addition
        self.next_section(skip_animations=0)

        s_box.shift(UP * 0.75)
        self.play(p_box.animate.shift(DOWN * 0.75),
                  FadeIn(cipher),
                  FadeIn(cipher_extras),
                  FadeIn(s_box),
                  runtime=1)
        self.wait(1)











#---- HELPERS ----#
def initialize_state(rows, cols, state):
    for r in range(rows):
        for c in range(cols):
            state.add_highlighted_cell((r+1, c+1), color=colors[r*cols + c])

def update_state(rows, cols, rnd, og_state, prev_state):
    # create new random color state to replace previous state
    next_state = og_state.copy()
    for r in range(rows):
        for c in range(cols):
            next_state.add_highlighted_cell((r+1, c+1), color=rnd.next())
    
    # create animation to replace old state with new state
    return (next_state, ReplacementTransform(prev_state, next_state))
            
                
