from manim import *
from random import random

def alg(n):
    k = 0
    for _ in range(n):
        x = random()*2 - 1
        y = random()*2 - 1
        if x**2 + y**2 <= 1:
            k+=1
    return 4*k/n

class PiScene1(Scene):
    def construct(self):
        k = 0
        n = 20
        result = 4*k

        pi_approx = DecimalNumber(
            1,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=False
        ).to_corner(UP+RIGHT)
        pi_approx.add_updater(lambda d: d.set_value(result))
        
        pi = MathTex("\\pi = ").next_to(pi_approx, LEFT)
        
        _radius = 4
        circ = Circle(radius=_radius, color=RED)
        
        self.add(pi_approx, pi, circ)

        for i in range(n):
            x = random()*2 - 1
            y = random()*2 - 1
            if x**2 + y**2 <= 1:
                k+=1
                self.play(FadeIn(Dot(radius=0.02).move_to([x*_radius,y*_radius,0])))
            result = 4*k/(i+1)

        self.wait()


class PiScene2(Scene):
    def construct(self):
        k = 0
        n = 1000
        result = 4*k

        pi_approx = DecimalNumber(
            1,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=False
        ).to_corner(UP+RIGHT)
        pi_approx.add_updater(lambda d: d.set_value(result))
        
        pi = MathTex("\\pi = ").next_to(pi_approx, LEFT)
        
        _radius = 4
        # circ = Circle(radius=_radius, color=RED)
        # self.add(pi_approx, pi, circ)
        self.add(pi_approx, pi)
        points = []

        for i in range(n):
            x = random()*2 - 1
            y = random()*2 - 1
            if x**2 + y**2 <= 1:
                k+=1
                points.append(Dot(radius=0.02, color=GREEN).move_to([x*_radius,y*_radius,0]))
            else:
                points.append(Dot(radius=0.02, color=RED).move_to([x*_radius,y*_radius,0]))
            result = 4*k/(i+1)
        
        self.play(
            AnimationGroup(
                *[
                    FadeIn(p)
                    for p in points
                ],
                lag_ratio=.5,
                run_time=5,
                rate_func=rate_functions.wiggle
            ),
       )

        self.wait(3)
 

