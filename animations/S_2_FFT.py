from manim import *
from extras import custom_colors

config.background_color = custom_colors.BACKGROUND_1
class FFT_Scene(Scene):
    def construct(self):

        #----------- SECTION 1 -----------#
        # intro to fields
        self.next_section(skip_animations=1)
        #---------------------------------#

        spn_text = Text("1. Substitution Permutation Networks", font_size=32, color=YELLOW)
        finite_field_text = Text("2. Finite Field Theory", font_size=32, color=YELLOW).next_to(spn_text, DOWN).align_to(spn_text, LEFT)
        text_group = VGroup(spn_text, finite_field_text).move_to(ORIGIN)
        finite_field_text.scale(0.75).to_edge(UP + LEFT, buff=0.75)
        self.add(finite_field_text)

        standard_field_circle = Circle(radius=2, color=custom_colors.TURQUOISE, fill_opacity=0.5)
        sub_elem_labels = ['1', '2', '3', '4', '5', '6', '...']
        center = standard_field_circle.get_center()
        sub_elem_points = [(center),
                           (center + LEFT * 0.5 + UP),
                           (center + RIGHT * 1.5 + UP * 0.4),
                           (center + UP * 1.3),
                           (center + LEFT * 0.8 + DOWN * 0.7),
                           (center + RIGHT * 0.6 + DOWN),
                           (center + LEFT * 1.3 + UP * 0.1)]
        sub_elems = VGroup()
        for i in range(7):
            p = Dot(sub_elem_points[i], color=custom_colors.TURQUOISE)
            p_t = MathTex(f"{sub_elem_labels[i]}").scale(0.75).move_to(p.get_bottom() + DOWN * 0.2)
            elem = VGroup(p, p_t)
            sub_elems.add(elem)
        standard_field = VGroup(standard_field_circle, sub_elems)

        standard_field_def = MathTex(r"F = \mathbb{Z}").move_to(
            standard_field.get_bottom() + DOWN * 0.5)
        standard_field.add(standard_field_def)

        self.play(FadeIn(standard_field_circle))
        for i in range(7):
            self.play(FadeIn(sub_elems[i]), run_time=0.25)
        self.play(FadeIn(standard_field_def))
        self.play(standard_field.animate.shift(LEFT * 4))

        extended_def = MathTex(r"F = \mathbb{Z},\left\{ +, * \right\}").move_to(
            standard_field_def.get_center()
        )
        self.play(ReplacementTransform(standard_field_def, extended_def))

        axioms_rect = RoundedRectangle(corner_radius=0.25, height=6.75, width=7.5, 
                                      color=custom_colors.FOREGROUND_1, fill_opacity=0.25).shift(RIGHT * 2.5)
        axioms_label = MathTex(r"For \ \left\{ +, * \right\} \ over \ F").scale(0.75)
        axioms_line = Line(axioms_rect.get_left(), 
                           axioms_rect.get_right(),
                           stroke_width=2,
                           buff=0.5).next_to(axioms_label, DOWN, buff=0.2)
        axioms_title = VGroup(axioms_label, axioms_line).move_to(axioms_rect.get_top() + DOWN * 0.5)
        axioms_box = VGroup(axioms_title, axioms_rect, axioms_label)
    
        self.play(FadeIn(axioms_box))

        #----------- SECTION 2 -----------#
        # field axioms
        self.next_section(skip_animations=1)
        #---------------------------------#

        scale_factor = 0.6

        add_associative = MathTex(r"a+(b+c)=(a+b)+c").scale(scale_factor).next_to(axioms_title, DOWN, buff=0.25).shift(RIGHT * 1.5)
        mult_associative = MathTex(r"a \cdot(b \cdot c)=(a \cdot b) \cdot c").scale(scale_factor).next_to(add_associative, DOWN, buff=0.25).align_to(add_associative, LEFT)
        associative_group = VGroup(add_associative, mult_associative)
        assoc_brace = Brace(associative_group, LEFT)
        assoc_text = MathTex(r"Associative").scale(0.75).next_to(assoc_brace, LEFT, buff=0.25)
        assoc_extras = VGroup(assoc_brace, assoc_text)

        add_comm = MathTex(r"a+b=b+a").scale(scale_factor).next_to(mult_associative, DOWN, buff=0.5).align_to(mult_associative, LEFT)
        mult_comm = MathTex(r"a \cdot b=b \cdot a").scale(scale_factor).next_to(add_comm, DOWN, buff=0.25).align_to(add_comm, LEFT)
        commutative_group = VGroup(add_comm, mult_comm)
        comm_brace = Brace(commutative_group, LEFT)
        comm_text = MathTex(r"Commutative").scale(0.75).next_to(comm_brace, LEFT, buff=0.25)
        comm_extras = VGroup(comm_brace, comm_text)

        distributivity = MathTex(r"a \cdot (b+c)=(a \cdot b)+(a \cdot c)").scale(scale_factor).next_to(mult_comm, DOWN, buff=0.5).align_to(mult_comm, LEFT)
        dist_brace = Brace(distributivity, LEFT)
        dist_text = MathTex(r"Distributive").scale(0.75).next_to(dist_brace, LEFT, buff=0.25)
        dist_extras = VGroup(dist_brace, dist_text)

        add_inv = MathTex(r"a+(-a)=0").scale(scale_factor).next_to(distributivity, DOWN, buff=0.5).align_to(distributivity, LEFT)
        mult_inv = MathTex(r"a \cdot a^{-1}=1").scale(scale_factor).next_to(add_inv, DOWN, buff=0.25).align_to(add_inv, LEFT)
        inv_group = VGroup(add_inv, mult_inv)
        inv_brace = Brace(inv_group, LEFT)
        inv_text = MathTex(r"Inverses").scale(0.75).next_to(inv_brace, LEFT, buff=0.25)
        inv_extras = VGroup(inv_brace, inv_text)
        inv_group.add(inv_extras)

        add_id = MathTex(r"a+0=a").scale(scale_factor).next_to(mult_inv, DOWN, buff=0.5).align_to(mult_inv, LEFT)
        mult_id = MathTex(r"a \cdot 1=a").scale(scale_factor).next_to(add_id, DOWN, buff=0.25).align_to(add_id, LEFT)
        id_group = VGroup(add_id, mult_id)
        id_brace = Brace(id_group, LEFT)
        id_text = MathTex(r"Identity").scale(0.75).next_to(id_brace, LEFT, buff=0.25)
        id_extras = VGroup(id_brace, id_text)

        self.play(FadeIn(assoc_extras, associative_group))
        self.play(FadeIn(comm_extras, commutative_group))
        self.play(FadeIn(dist_extras, distributivity))
        self.play(FadeIn(inv_extras, inv_group))
        self.play(FadeIn(id_extras, id_group))
        self.play(inv_group.animate.set_color(YELLOW))

        #----------- SECTION 2 -----------#
        # Galois Fields
        self.next_section(skip_animations=0)
        #---------------------------------#
        
        finite_field_def = MathTex(r"F = S\subset_{fin} \mathbb{Z},\left\{ +,* \right\}").move_to(standard_field_def.get_center())
        galois_field_label = MathTex(r"Finite \ (Galois) \ Fields").move_to(axioms_label.get_center()).scale(0.75)
    
        self.play(ReplacementTransform(extended_def, finite_field_def),
                  FadeOut(sub_elems[-1]))
        self.wait(1)
        self.play(FadeOut(assoc_extras, associative_group),
                  FadeOut(comm_extras, commutative_group),
                  FadeOut(dist_extras, distributivity),
                  FadeOut(inv_extras, inv_group),
                  FadeOut(id_extras, id_group),
                  ReplacementTransform(axioms_label, galois_field_label))
        
        galois_field_def = MathTex(r"GF = A_{fin},\left\{ +,* \right\}").move_to(standard_field_def.get_center())
        self.play(ReplacementTransform(finite_field_def, galois_field_def))

        galois_field_representation = MathTex(r"GF(p^m) \ | \ p \in \mathbb{P}, m\in\mathbb{Z^+}").next_to(
            axioms_line, DOWN, buff=0.5).align_to(axioms_line, LEFT)
        galois_field_elements = MathTex(r"S=\left\{ 0, \ 1, \ ..., \ p^m-1 \right\}").next_to(
            galois_field_representation, DOWN, buff=0.5).align_to(axioms_line, LEFT)
        galois_field_order = MathTex(r"\left| S \right|=p^m").next_to(
            galois_field_elements, DOWN, buff=0.5).align_to(axioms_line, LEFT)
        
        self.play(FadeIn(galois_field_representation),
                  FadeIn(galois_field_elements),
                  FadeIn(galois_field_order))
        
        


