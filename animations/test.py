from manim import *

class textex(Scene):
    def construct(self):
        Tex.set_default(font_size=30)
        t0 = Tex(r"This is default plain text mode\\ in two centered lines.").to_edge(UP, buff=0)
        self.add(t0)
        t1 = Tex(
            r"This is plain text mode\\ in two left justified lines.",
            tex_environment="flushleft"
        ).next_to(t0,DOWN)
        self.add(t1)
        t2 = Tex(
            r"This is a longer text block in a so-called minipage environment allowing for justified margins. And just because I can I also throw in some math $E=mc^2$.",
            tex_environment="minipage}{25em}"
        ).set_color(YELLOW).next_to(t1,DOWN)
        t3 = Tex(
            r"\raggedright This is a longer text block in a so-called minipage environment allowing for justified margins. And just because I can I also throw in some math $E=mc^2$.",
            tex_environment="minipage}{25em}"
        ).set_color(YELLOW).next_to(t2,DOWN)
        t4 = Tex(
            r"\raggedleft This is a longer text block in a so-called minipage environment allowing for justified margins. And just because I can I also throw in some math $E=mc^2$.",
            tex_environment="minipage}{25em}"
        ).set_color(YELLOW).next_to(t3,DOWN)
        t5 = Tex(
            r"\centering This is a longer text block in a so-called minipage environment allowing for justified margins. And just because I can I also throw in some math $E=mc^2$.",
            tex_environment="minipage}{25em}"
        ).set_color(YELLOW).next_to(t4,DOWN)
        self.add(t2,t3,t4,t5)
        t6 = MathTex(
            r"Q = \sum\limits_{i=1}^{n}i = \frac{n\left(n-1\right)}{2} \quad\text{C.\ F.\ Gauss}",
            font_size=30
        ).set_color(RED).next_to(t5,DOWN)
        self.add(t6)

        self.wait(2)