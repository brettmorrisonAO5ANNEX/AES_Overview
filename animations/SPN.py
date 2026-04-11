from manim import *

class SPN_Scene(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait(1)

