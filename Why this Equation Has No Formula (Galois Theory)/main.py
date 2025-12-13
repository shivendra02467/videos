from manim import *
import numpy as np

class QuadraticTransform(Scene):
    def construct(self):
        # Step 1: Write the quadratic formula (large size)
        quadratic_formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=72
        )

        self.play(Write(quadratic_formula))
        self.wait(2)

        # Step 2: Define the general quadratic equation
        quadratic_equation = MathTex(
            r"ax^2 + bx + c = 0",
            font_size=72
        )

        # Step 3: Transform formula to equation
        self.play(Transform(quadratic_formula, quadratic_equation))
        self.wait(4)
        self.play(
            quadratic_formula.animate.shift(UP*3)
        )
        self.wait(1)
        cubic_equation = MathTex(
            r"ax^3 + bx^2 + cx + d = 0",
            font_size=72
        )

        quartic_equation = MathTex(
            r"ax^4 + bx^3 + cx^2 + dx + e = 0",
            font_size=72
        )

        self.play(Write(cubic_equation))
        self.wait(2)

        self.play(
            cubic_equation.animate.shift(UP * 1.5)
        )
        
        quartic_equation.next_to(cubic_equation, DOWN, buff=1.0)

        self.play(Write(quartic_equation))
        self.wait(3)

class NoQuintic(Scene):
    def construct(self):
        eq1 = MathTex(r"ax^2 + bx + c = 0 \implies x_i = \operatorname{f_2}()", font_size=40)
        eq2 = MathTex(r"ax^3 + bx^2 + cx + d = 0 \implies x_i = \operatorname{f_3}()", font_size=40)
        eq3 = MathTex(r"ax^4 + bx^3 + cx^2 + dx + e = 0 \implies x_i = \operatorname{f_4}()", font_size=40)
        eq4 = MathTex(r"ax^5 + bx^4 + cx^3 + dx^2 + ex + f = 0 \implies \times", font_size=40)
        box = SurroundingRectangle(eq4, color=YELLOW, buff=MED_LARGE_BUFF)
        # Center each line horizontally
        for eq in [eq1, eq2, eq3, eq4]:
            eq.move_to(ORIGIN)  # This centers each equation around the origin

        # Now stack them vertically, each already centered
        equations = VGroup(eq1, eq2, eq3, VGroup(eq4,box)).arrange(DOWN, buff=0.5)
        equations.move_to(ORIGIN)  # Center the whole group vertically

        self.play(Write(equations), run_time=8)
        self.wait(1)

class Formula(Scene):
    def construct(self):
        x_vars = VGroup(*[MathTex(f"x_{{{i}}}",font_size=80) for i in range(1, 6)])
        x_vars.arrange(RIGHT, buff=0.7)
        self.play(Write(x_vars))
        self.wait(1)

        # Step 2: Transform x_1,...x_5 into a single general indexed variable x_i
        x_i = MathTex("x_i",font_size=80).move_to(x_vars.get_center())
        self.play(Transform(x_vars, x_i))
        self.wait(1)

        # Step 3: Transform x_i into F()
        F = MathTex("\operatorname{f}()",font_size=80).move_to(x_i.get_center())
        self.play(Transform(x_vars, F))
        self.wait(2)
        text1 = MathTex(
            r"\operatorname{f}()",
            font_size=40
        )
        text2 = MathTex(
            r"\text{should consist of finite sequences of}",
            font_size=40
        )
        text = VGroup(text1,text2).arrange(DOWN,buff=0.5)
        text.move_to(UP*3)
        self.play(Transform(x_vars,text1))
        addition = MathTex(
            r"+",
            font_size=100
        )
        subtraction = MathTex(
            r"-",
            font_size=100
        )
        multi = MathTex(
            r"\times",
            font_size=100
        )
        div = MathTex(
            r"\div",
            font_size=100
        )
        root = MathTex(
            r"\sqrt[n]{}",
            font_size=100
        )
        eq4 = MathTex(r"ax^5 + bx^4 + cx^3 + dx^2 + ex + f = 0", font_size=50)

        self.play(Write(text2),run_time=4)
        self.play(Write(addition),run_time=0.5)
        self.play(addition.animate.shift(LEFT*4+UP*1.5),run_time=0.5)
        self.play(Write(subtraction),run_time=0.5)
        self.play(subtraction.animate.shift(LEFT*2+UP*1.5),run_time=0.5)
        self.play(Write(multi),run_time=0.5)
        self.play(multi.animate.shift(RIGHT*0+UP*1.5),run_time=0.5)
        self.play(Write(div),run_time=0.5)
        self.play(div.animate.shift(RIGHT*2+UP*1.5),run_time=0.5)
        self.play(Write(root),run_time=0.5)
        self.play(root.animate.shift(RIGHT*4+UP*1.5),run_time=0.5)
        self.play(Write(eq4))

class DeriveFormula(Scene):
    def construct(self):
        eq = MathTex("ax^2", "+", "bx", "+", "c", "=", "0").scale(1.3)
        self.play(Write(eq))
        self.wait(1.5)

        # Step 2
        new_eq = MathTex("x^2", "+", "\\frac{b}{a}x", "+", "\\frac{c}{a}", "=", "0").scale(1.3)
        self.play(Transform(eq, new_eq))
        self.wait(1.5)

        # Step 3
        new_eq = MathTex("x^2", "+", "\\frac{b}{a}x", "=", "-\\frac{c}{a}").scale(1.3)
        self.play(Transform(eq, new_eq))
        self.wait(1.5)

        # Step 4
        new_eq = MathTex(
            "x^2", "+", "\\frac{b}{a}x", "+", "\\left(\\frac{b}{2a}\\right)^2",
            "=", "-\\frac{c}{a}", "+", "\\left(\\frac{b}{2a}\\right)^2"
        ).scale(1.1)
        self.play(Transform(eq, new_eq))
        self.wait(2)

        # Step 5
        new_eq = MathTex(
            "\\left(x + \\frac{b}{2a}\\right)^2",
            "=",
            "-\\frac{c}{a}", "+", "\\frac{b^2}{4a^2}"
        ).scale(1.1)
        self.play(Transform(eq, new_eq))
        self.wait(2)

        # Step 6
        new_eq = MathTex(
            "\\left(x + \\frac{b}{2a}\\right)^2",
            "=",
            "\\frac{b^2 - 4ac}{4a^2}"
        ).scale(1.2)
        self.play(Transform(eq, new_eq))
        self.wait(2)

        # Step 7
        new_eq = MathTex(
            "x + \\frac{b}{2a}",
            "=",
            "\\pm\\frac{\\sqrt{b^2 - 4ac}}{2a}"
        ).scale(1.3)
        self.play(Transform(eq, new_eq))
        self.wait(2)

        # Step 8
        new_eq = MathTex(
            "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"
        ).scale(1.4)
        self.play(Transform(eq, new_eq))
        self.wait(3)

class DeriveFormula2(Scene):
    def construct(self):
        # Title
        title1 = Text("Cardano's Cubic Formula", font_size=30)
        title2 = Text("Ferrari's symbolic Quartic Formula", font_size=30)
        # Full cubic formula (Cardano's)
        cubic_formula = MathTex(
            r"x = \sqrt[3]{-\frac{q}{2} + \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}}"
            r"+ \sqrt[3]{-\frac{q}{2} - \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}}"
        ).scale(0.8)

        # Full quartic formula (Ferrari's) — symbolic and condensed
        quartic_formula = MathTex(
            r"x = -\frac{b}{4a} + \frac{1}{2} \sqrt{y_1} \pm \frac{1}{2} \sqrt{ -y_1 + \frac{2c}{a} \pm \frac{2b^2 - 8ac + 16ae}{4a \sqrt{y_1}} }"
        ).scale(0.75)

        # Arrange vertically
        formulas = VGroup(title1,cubic_formula,title2, quartic_formula).arrange(DOWN, buff=1).move_to(DOWN * 0.5)
        formulas.move_to(ORIGIN)
        # Animate writing each
        self.play(Write(title1))
        self.play(Write(cubic_formula))
        self.wait(0.5)
        self.play(Write(title2))
        self.play(Write(quartic_formula))
        self.wait(1)

class DeriveStep1(Scene):
    def construct(self):
        # Original equation
        eq1 = MathTex("a x^2", "+", "b x", "+", "c", "=", "0", font_size=50)
        eq1.move_to(ORIGIN)
        self.play(Write(eq1))
        self.wait(1)

        # Modified equation after subtracting c from both sides
        eq2 = MathTex("a x^2", "+", "b x", "=", "-c", font_size=50)
        eq2.move_to(ORIGIN)

        # Draw curved arrow from "+ c" to "-c"
        start = eq1[2].get_top()
        end = eq1[5].get_top()

        curved_arrow = CurvedArrow(start+UP*0.6, end+UP*0.6, angle=-PI,tip_length=0.2)
        move_label_t = MathTex("-", font_size=50).next_to(curved_arrow, UP)
        ops_box = create_math_operations_box()
        ops_box.move_to(UL*2.5)
        move_label =create_math_operations_box()
        move_label.move_to(UL*2.5)
        # Show the subtraction and arrow
        self.play(Transform(eq1, eq2))
        self.play(Create(curved_arrow),Transform(move_label,move_label_t),FadeIn(ops_box))
        self.wait(2)
        eq3 = MathTex("x^2","+","\\frac{b}{a}x","=","\\frac{c}{a}",font_size=50)
        start = eq1[2].get_top()
        end = eq1[5].get_top()
        curved_arrow2 = CurvedArrow(start+LEFT,end+1.6*LEFT+DOWN,angle=3*PI/2,tip_length=0.2)
        move_label2_t = MathTex("\\div", font_size=50).next_to(curved_arrow2, LEFT)
        move_label2 =create_math_operations_box()
        move_label2.move_to(UL*2.5)
        self.play(Transform(eq1,eq3))
        self.play(Create(curved_arrow2),Transform(move_label2,move_label2_t))
        self.wait(2)
        group = VGroup(eq1,curved_arrow,curved_arrow2,move_label,move_label2,ops_box)
        self.play(
            group.animate.scale(0.8).shift(LEFT * 2.75 + DOWN * 0.6),
            run_time=1
        )
        arrow = MathTex(r"\implies",font_size=100)
        self.play(Write(arrow))
        rubik_image = ImageMobject("rubiks-cube-3347244_1280.png")
        galois_image = ImageMobject("Evariste_galois.jpg")
        rubik_image.scale(0.4)
        galois_image.scale(0.4)
        galois_image.move_to(UP*2.5)
        rubik_image.move_to(RIGHT*4)
        self.play(FadeIn(rubik_image))
        self.wait(1.5)
        tick = Text("✓", color=YELLOW, font_size=60)
        cross = Text("✗", color=RED, font_size=60)

        # Position tick and cross below shapes
        tick.next_to(rubik_image, DOWN)
        cross.next_to(group, DOWN)
        self.play(FadeIn(galois_image))
        self.wait(2)
        self.play(Write(cross))
        self.play(Write(tick))
        self.wait(2)
        

def create_math_operations_box():
    symbols = VGroup(VGroup(MathTex(r"+",font_size=50),MathTex(r"-",font_size=50),MathTex(r"\times",font_size=50)).arrange(RIGHT,buff=0.4),VGroup(MathTex(r"\div",font_size=50),MathTex(r"\sqrt[n]{}",font_size=50)).arrange(RIGHT,buff=0.4))
    symbols.arrange(DOWN, buff=0.4)
    box = RoundedRectangle(corner_radius=0.2, width=symbols.width+1, height=symbols.height + 1)
    box.move_to(symbols)
    return VGroup(box, symbols)

class Theory(Scene):
    def construct(self):
        text = MathTex(r"F",font_size=72)
        self.play(Write(text))

        ops_box = create_math_operations_box()
        
        formula = MathTex(r"\operatorname{f}\left(F\right)",font_size=72)
        operations = VGroup(MathTex(r"x_i = \operatorname{f}\left( F ,",font_size=72),ops_box,MathTex(r"\right)",font_size=72)).arrange(RIGHT,buff=0.5)
        self.play(Transform(text,formula))
        self.wait(2)
        self.play(Transform(text,operations))
        self.wait(1.5)
        self.play(text.animate.scale(0.7).shift(LEFT*4),run_time=1)
        self.play(Write(MathTex(r"\implies",font_size=100)),run_time=0.5)
        # Circle to place dots on
        circle = Circle(radius=1)
        circle.move_to(RIGHT*3.5)
        # Positions of 3 dots on the circle at 0°, 120°, 240°
        angles = [0, 120, 240]
        points = [circle.point_at_angle(np.deg2rad(angle)) for angle in angles]

        dots = VGroup(*[
            Dot(point=pt, radius=0.15)
            for i, pt in enumerate(points)
        ])

        circle2 = Circle(radius=1)
        circle2.move_to(RIGHT*3.5+UP*2.5)
        # Positions of 3 dots on the circle at 0°, 120°, 240°
        angles2 = [0, 120, 240]
        points2 = [circle2.point_at_angle(np.deg2rad(angle)) for angle in angles2]
        dots2 = VGroup(*[
            Dot(point=pt, radius=0.15)
            for i, pt in enumerate(points2)
        ])

        circle3 = Circle(radius=1)
        circle3.move_to(RIGHT*3.5+DOWN*2.5)
        # Positions of 3 dots on the circle at 0°, 120°, 240°
        angles3 = [0, 180]
        points3 = [circle3.point_at_angle(np.deg2rad(angle)) for angle in angles3]

        dots3 = VGroup(*[
            Dot(point=pt, radius=0.15)
            for i, pt in enumerate(points3)
        ])

        field = MathTex(r"F",font_size=50).move_to(circle.get_center())
        field2 = MathTex(r"F",font_size=50).move_to(circle2.get_center())
        field3 = MathTex(r"F",font_size=50).move_to(circle3.get_center())

        self.play(Create(circle),Create(circle2),Create(circle3),run_time=0.5)
        self.play(FadeIn(dots),FadeIn(dots2),FadeIn(dots3),FadeIn(field),FadeIn(field2),FadeIn(field3),run_time=0.5)
        def animate_symmetry(new_order,new_order2,new_order3, run_time=1.5):
            new_positions = [dots[i].get_center() for i in new_order]
            new_positions2 = [dots2[i].get_center() for i in new_order2]
            new_positions3 = [dots3[i].get_center() for i in new_order3]
            animations = (
                [dots[i].animate.move_to(new_positions[i]) for i in range(3)] +
                [dots2[i].animate.move_to(new_positions2[i]) for i in range(3)] +
                [dots3[i].animate.move_to(new_positions3[i]) for i in range(2)]
            )
            self.play(*animations, run_time=run_time)

        label = MathTex(r"\text{Group } S_3",font_size=30).move_to(circle.get_right()+RIGHT)
        label2 = MathTex(r"\text{Group } C_3",font_size=30).move_to(circle2.get_right()+RIGHT)
        label3 = MathTex(r"\text{Group } C_2",font_size=30).move_to(circle3.get_right()+RIGHT)

        # Rotation 120° clockwise (A,B,C) → (B,C,A)
        animate_symmetry([1, 2, 0],[1, 2, 0],[1,0])

        # Rotation 240° clockwise (A,B,C) → (C,A,B)
        animate_symmetry([2, 0, 1],[2, 0, 1],[1,0])
        self.play(Write(label),Write(label2),Write(label3),run_time=0.2)
        # Reflection swapping B and C (A,B,C) → (A,C,B)
        animate_symmetry([1, 0, 2],[1, 2, 0],[1,0])
        animate_symmetry([1, 2, 0],[2, 0, 1],[1,0])
        # Rotation 240° clockwise (A,B,C) → (C,A,B)
        animate_symmetry([2, 0, 1],[1, 2, 0],[1,0])
        # Reflection swapping B and C (A,B,C) → (A,C,B)
        animate_symmetry([0, 2, 1],[2, 0, 1],[1,0])
        animate_symmetry([1, 2, 0],[1, 2, 0],[1,0])

        # Rotation 240° clockwise (A,B,C) → (C,A,B)
        animate_symmetry([2, 0, 1],[2, 0, 1],[1,0])

        # Reflection swapping B and C (A,B,C) → (A,C,B)
        animate_symmetry([2, 1, 0],[1, 2, 0],[1,0])
        animate_symmetry([1, 2, 0],[1, 2, 0],[1,0])

        # Rotation 240° clockwise (A,B,C) → (C,A,B)
        animate_symmetry([2, 0, 1],[2, 0, 1],[1,0])

        # Reflection swapping B and C (A,B,C) → (A,C,B)
        animate_symmetry([2, 1, 0],[1, 2, 0],[1,0])
        animate_symmetry([1, 2, 0],[1, 2, 0],[1,0])

        # Rotation 240° clockwise (A,B,C) → (C,A,B)
        animate_symmetry([2, 0, 1],[2, 0, 1],[1,0])

        # Reflection swapping B and C (A,B,C) → (A,C,B)
        animate_symmetry([2, 1, 0],[1, 2, 0],[1,0])
        animate_symmetry([1, 2, 0],[1, 2, 0],[1,0])

        # Rotation 240° clockwise (A,B,C) → (C,A,B)
        animate_symmetry([2, 0, 1],[2, 0, 1],[1,0])

        # Reflection swapping B and C (A,B,C) → (A,C,B)
        animate_symmetry([2, 1, 0],[1, 2, 0],[1,0])
        animate_symmetry([1, 2, 0],[1, 2, 0],[1,0])

        # Rotation 240° clockwise (A,B,C) → (C,A,B)
        animate_symmetry([2, 0, 1],[2, 0, 1],[1,0])

        # Reflection swapping B and C (A,B,C) → (A,C,B)
        animate_symmetry([2, 1, 0],[1, 2, 0],[1,0])

class DodeSymmetry(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        
        dode = Dodecahedron()

        eq1 = MathTex(r"\text{Group } A_5 \cong").move_to(LEFT*3.5)
        text = MathTex(r"\text{Rotational Symmetries of Dodecahedron}",font_size=40).move_to(UP*3)

        # Color faces to make symmetry visible
        colors = [BLUE, GREEN, RED, ORANGE, PURPLE, YELLOW]
        for i, face in enumerate(dode.faces):
            face.set_fill(colors[i % len(colors)], opacity=0.6)

        self.add(dode)
        self.add_fixed_in_frame_mobjects(eq1,text)
        self.play(Write(eq1),Write(text))

        # Use correct 5-fold symmetry axis (through opposite pentagon face centers)
        axis = [0, 0.8507, 0.5257]  # Approximate correct symmetry axis
        self.play(Rotate(dode, angle=72 * DEGREES, axis=axis), run_time=3)
        ops_box = create_math_operations_box()
        cross = Cross(ops_box)
        not_possible = VGroup(ops_box,cross)
        self.add_fixed_in_frame_mobjects(not_possible)
        not_possible.move_to(RIGHT*4)
        self.play(FadeIn(not_possible))
        self.play(Rotate(dode, angle=72 * DEGREES, axis=axis), run_time=3)
        self.wait(1)
        self.play(Rotate(dode, angle=72 * DEGREES, axis=axis), run_time=3)
        
class Theory2(Scene):
    def construct(self):
        text1 = MathTex(
            r"F := \mathbb{Q}",
            font_size=50
        ).move_to([-3.5,3,0])
        text2 = MathTex(
            r"K := \mathbb{Q}(x_1, x_2, ..,x_n)",
            font_size=50
        ).move_to([-2,2,0])
        self.play(Write(text1),run_time=2)
        self.wait(2)
        self.play(Write(text2),run_time=5)
        self.wait(2)
        circle = Circle(radius=1)
        circle.move_to(RIGHT*3.5)
        # Positions of 3 dots on the circle at 0°, 120°, 240°
        angles = [0, 120, 240]
        points = [circle.point_at_angle(np.deg2rad(angle)) for angle in angles]

        dots = VGroup(*[
            Dot(point=pt, radius=0.15)
            for i, pt in enumerate(points)
        ])
        base_field = MathTex(r"x_2 \in \mathbb{Q}",font_size=30).move_to(dots[2].get_left()+LEFT*0.6)
        x_1 =MathTex(r"x_1",font_size=30).move_to(dots[0].get_right()+RIGHT*0.3)
        x_3 =MathTex(r"x_3",font_size=30).move_to(dots[1].get_right()+RIGHT*0.3+UP*0.4)
        self.play(Create(circle))
        self.play(FadeIn(dots))
        def animate_symmetry(new_order, run_time=1.5):
            new_positions = [dots[i].get_center() for i in new_order]
            animations =(
                [dots[i].animate.move_to(new_positions[i]) for i in range(3)]+
                [x_1.animate.move_to(x_3),x_3.animate.move_to(x_1)]
            )
            self.play(*animations, run_time=run_time)
        animate_symmetry([1,0,2])
        animate_symmetry([1,0,2])
        self.play(FadeIn(base_field),FadeIn(x_1),FadeIn(x_3),run_time=0.3)
        animate_symmetry([1,0,2])
        text3 = MathTex(r"\operatorname{Gal}(K/F) := ",font_size=50).move_to([-2.8,0,0])
        text4 = MathTex(r"\operatorname{Aut}_{\mathbb{Q}}(\mathbb{Q}(...))",font_size=50).move_to([0.2,0,0])
        self.play(Write(text4))
        self.wait(2)
        self.play(Write(text3))
        self.wait(2)
        animate_symmetry([1,0,2])
        animate_symmetry([1,0,2])
        eq4 = MathTex(r"ax^5 + bx^4 + cx^3 + dx^2 + ex + f = 0 ", font_size=40)
        box = SurroundingRectangle(eq4, color=YELLOW, buff=MED_LARGE_BUFF)
        algeb = VGroup(eq4,box)
        algeb.move_to(DOWN*3)
        curved_arrow = CurvedArrow(circle.get_bottom()+DOWN*0.4+RIGHT*0.4, algeb.get_right()+RIGHT*0.2, angle=-3*PI/4,tip_length=0.2)
        self.play(Create(curved_arrow),run_time=1)
        self.play(Write(eq4))
        self.wait(1)
        self.play(Write(box))
        self.wait(3)

class GroupTheory(Scene):
    def construct(self):
        text1 = MathTex(r"\text{Group Theory}",font_size=72).move_to(UP*3)
        self.play(Write(text1))
        self.wait(2)
        img1 = ImageMobject("Untitled design.png").scale(0.3).move_to(LEFT*4.5)
        img2 = Group(ImageMobject("6.jpg").scale(0.4),Text("youtube.com/@RichBehiel",font_size=20)).arrange(DOWN).move_to(LEFT*0.5)
        img3 = ImageMobject("7.jpg").scale(0.2).move_to(RIGHT*4 +UP*0.25)
        self.play(FadeIn(img1))
        self.play(FadeIn(img2))
        self.play(FadeIn(img3))
        self.wait(2)

class Example1(Scene):
    def construct(self):
        text1 = MathTex(r"ax^2+bx+c=0 \text{ over } \mathbb{Q}",font_size=40).move_to(UP*3)
        self.play(Write(text1))
        self.wait(2)
        text2 = MathTex(r"\operatorname{Gal}(K/F) = C_2",font_size=40).move_to(UP*2)
        self.play(Write(text2))
        circle = Circle(radius=1)
        angles = [0, 180]
        points = [circle.point_at_angle(np.deg2rad(angle)) for angle in angles]

        dots = VGroup(*[
            Dot(point=pt, radius=0.15)
            for i, pt in enumerate(points)
        ])
        self.play(Create(circle),run_time=0.4)
        self.play(FadeIn(dots),run_time=0.4)
        def animate_symmetry(new_order, run_time=1):
            new_positions = [dots[i].get_center() for i in new_order]
            animations =[dots[i].animate.move_to(new_positions[i]) for i in range(2)]
            self.play(*animations, run_time=run_time)
        animate_symmetry([1,0])
        animate_symmetry([1,0])
        animate_symmetry([1,0])
        quadratic_formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=40
        ).move_to(DOWN*2.5)
        self.play(Write(quadratic_formula))


class Example2(Scene):
    def construct(self):
        text1 = MathTex(r"ax^3+bx^2+cx+d=0 \text{ over } \mathbb{Q}",font_size=40).move_to(UP*3)
        self.play(Write(text1))
        self.wait(2)
        text2 = MathTex(r"\operatorname{Gal}(K/F) = S_3",font_size=40).move_to(UP*2)
        self.play(Write(text2))
        circle = Circle(radius=1)
        angles = [0, 120, 240]
        points = [circle.point_at_angle(np.deg2rad(angle)) for angle in angles]

        dots = VGroup(*[
            Dot(point=pt, radius=0.15)
            for i, pt in enumerate(points)
        ])
        self.play(Create(circle),run_time=0.4)
        self.play(FadeIn(dots),run_time=0.4)
        def animate_symmetry(new_order, run_time=1):
            new_positions = [dots[i].get_center() for i in new_order]
            animations =[dots[i].animate.move_to(new_positions[i]) for i in range(3)]
            self.play(*animations, run_time=run_time)
        animate_symmetry([2,0,1])
        animate_symmetry([1,2,0])
        animate_symmetry([1,0,2])
        cubic_formula = MathTex(
            r"x = \sqrt[3]{-\frac{q}{2} + \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}}"
            r"+ \sqrt[3]{-\frac{q}{2} - \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}}"
        ).scale(0.5).move_to(DOWN*2.5)
        self.wait(1)
        self.play(Write(cubic_formula))
        self.wait(2)

class Example3(Scene):
    def construct(self):
        text1 = MathTex(r"ax^4+bx^3+cx^2+dx+e=0 \text{ over } \mathbb{Q}",font_size=40).move_to(UP*3)
        self.play(Write(text1))
        self.wait(5)
        quintic = MathTex(r"x^5+bx^4+cx^3+dx^2+ex+f=0 \text{ over } \mathbb{Q}",font_size=40).move_to(UP*3)
        self.play(Transform(text1,quintic))
        self.wait(2)
        text2 = MathTex(r"\operatorname{Gal}(K/F) = S_5",font_size=40).move_to(UP*2)
        self.play(Write(text2))
        



        colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
        positions = [LEFT*2, LEFT, ORIGIN, RIGHT, RIGHT*2]
        dots = VGroup(*[
            Dot(pos, color=colors[i],radius=0.3)
            for i, pos in enumerate(positions)
        ])

        self.play(FadeIn(dots),run_time=0.3)

        permutations = {
            "Identity": [0, 1, 2, 3, 4],
            "(1 2)": [1, 0, 2, 3, 4],
            "(1 2 3)": [1, 2, 0, 3, 4],
            "(1 5)(2 4)": [4, 3, 2, 1, 0],
        }

        # Show each permutation by moving dots to new positions
        for name, perm in permutations.items():
            # Compute new positions for dots according to perm
            new_positions = [positions[perm[i]] for i in range(5)]

            # Animate the dots moving
            self.play(*[
                dots[i].animate.move_to(new_positions[i])
                for i in range(5)
            ], run_time=1)

            # Move dots back to original positions except for last permutation
            if name != "(1 5)(2 4)":
                self.play(*[
                    dots[i].animate.move_to(positions[i])
                    for i in range(5)
                ], run_time=1)





        formula = MathTex(
            r"\text{No Formula in radicals}").scale(0.8).move_to(DOWN*1.5)
        self.wait(1)
        self.play(Write(formula))
        self.wait(2)

        for name, perm in permutations.items():
            # Compute new positions for dots according to perm
            new_positions = [positions[perm[i]] for i in range(5)]

            # Animate the dots moving
            self.play(*[
                dots[i].animate.move_to(new_positions[i])
                for i in range(5)
            ], run_time=1)

            # Move dots back to original positions except for last permutation
            if name != "(1 5)(2 4)":
                self.play(*[
                    dots[i].animate.move_to(positions[i])
                    for i in range(5)
                ], run_time=1)

        self.wait(2.5)
        self.clear()
        elliptic = Text("Elliptic Modular Functions").scale(0.6).move_to(UP*3)
        img1 = ImageMobject("kleinj.png").scale(1.7).move_to(LEFT*3.5)
        img2 = ImageMobject("KleinInvariantJ.jpg").move_to(RIGHT*3.5)
        self.play(Write(elliptic),run_time=2)
        self.play(FadeIn(img1),FadeIn(img2),run_time=3)
        self.wait(2)
        self.play(Write(MathTex(r"A_5",font_size=72)))
        self.wait(2)


class Example4(Scene):
    def construct(self):
        text1 = MathTex(r"x^5+bx^4+cx^3+dx^2+ex+f=0 \text{ over } \mathbb{R}",font_size=40).move_to(UP*3)
        self.play(Write(text1),run_time=1)
        self.wait(1)
        text2 = MathTex(r"\operatorname{Gal}(K/F) = C_2",font_size=40).move_to(UP*2)
        self.play(Write(text2))
        circle = Circle(radius=1)
        angles = [0, 180]
        points = [circle.point_at_angle(np.deg2rad(angle)) for angle in angles]

        dots = VGroup(*[
            Dot(point=pt, radius=0.15)
            for i, pt in enumerate(points)
        ])
        self.play(Create(circle),run_time=0.2)
        self.play(FadeIn(dots),run_time=0.2)
        def animate_symmetry(new_order, run_time=1):
            new_positions = [dots[i].get_center() for i in new_order]
            animations =[dots[i].animate.move_to(new_positions[i]) for i in range(2)]
            self.play(*animations, run_time=run_time)
        animate_symmetry([1,0])
        animate_symmetry([1,0])
        animate_symmetry([1,0])
        ops_box = create_math_operations_box().scale(0.6)
        x_i = MathTex(r"\text{All } x_i \text{ can be expressed with }")
        reals = MathTex(r"\text{over } \mathbb{R}")
        group = VGroup(x_i,ops_box,reals).arrange(RIGHT).scale(0.6).move_to(DOWN*2.2+LEFT*3)
        formula = MathTex(
            r"\text{No Formula}",
            font_size=30
        ).move_to(DOWN*2.2+RIGHT*3)
        self.play(Write(x_i),Write(reals),FadeIn(ops_box))
        self.wait(6)

        tick = Text("✓", color=YELLOW, font_size=60)
        cross = Text("✗", color=RED, font_size=60)

        # Position tick and cross below shapes
        tick.next_to(group, DOWN)
        cross.next_to(formula, DOWN)
        self.play(Write(formula))
        self.play(Write(cross))
        self.wait(1)
        self.play(Write(tick))
        self.wait(4)

class TheoryO(Scene):
    def construct(self):
        ops_box = create_math_operations_box()
        text = VGroup(MathTex(r"x_i = \operatorname{f}\left( F ,",font_size=72),ops_box,MathTex(r"\right)",font_size=72)).arrange(RIGHT,buff=0.5)
        text.scale(0.7).shift(LEFT*4)
        self.play(FadeIn(text))
        self.play(Write(MathTex(r"\iff",font_size=100)),FadeIn(Cross()))
        # Circle to place dots on
        circle = Circle(radius=1)
        circle.move_to(RIGHT*3.5)
        # Positions of 3 dots on the circle at 0°, 120°, 240°
        angles = [0, 120, 240]
        points = [circle.point_at_angle(np.deg2rad(angle)) for angle in angles]

        dots = VGroup(*[
            Dot(point=pt, radius=0.15)
            for i, pt in enumerate(points)
        ])

        circle2 = Circle(radius=1)
        circle2.move_to(RIGHT*3.5+UP*2.5)
        # Positions of 3 dots on the circle at 0°, 120°, 240°
        angles2 = [0, 120, 240]
        points2 = [circle2.point_at_angle(np.deg2rad(angle)) for angle in angles2]
        dots2 = VGroup(*[
            Dot(point=pt, radius=0.15)
            for i, pt in enumerate(points2)
        ])

        circle3 = Circle(radius=1)
        circle3.move_to(RIGHT*3.5+DOWN*2.5)
        # Positions of 3 dots on the circle at 0°, 120°, 240°
        angles3 = [0, 180]
        points3 = [circle3.point_at_angle(np.deg2rad(angle)) for angle in angles3]

        dots3 = VGroup(*[
            Dot(point=pt, radius=0.15)
            for i, pt in enumerate(points3)
        ])

        field = MathTex(r"F",font_size=50).move_to(circle.get_center())
        field2 = MathTex(r"F",font_size=50).move_to(circle2.get_center())
        field3 = MathTex(r"F",font_size=50).move_to(circle3.get_center())

        self.play(Create(circle),Create(circle2),Create(circle3),run_time=0.5)
        self.play(FadeIn(dots),FadeIn(dots2),FadeIn(dots3),FadeIn(field),FadeIn(field2),FadeIn(field3),run_time=0.5)
        def animate_symmetry(new_order,new_order2,new_order3, run_time=1.5):
            new_positions = [dots[i].get_center() for i in new_order]
            new_positions2 = [dots2[i].get_center() for i in new_order2]
            new_positions3 = [dots3[i].get_center() for i in new_order3]
            animations = (
                [dots[i].animate.move_to(new_positions[i]) for i in range(3)] +
                [dots2[i].animate.move_to(new_positions2[i]) for i in range(3)] +
                [dots3[i].animate.move_to(new_positions3[i]) for i in range(2)]
            )
            self.play(*animations, run_time=run_time)

        label = MathTex(r"\text{Group } S_3",font_size=30).move_to(circle.get_right()+RIGHT)
        label2 = MathTex(r"\text{Group } C_3",font_size=30).move_to(circle2.get_right()+RIGHT)
        label3 = MathTex(r"\text{Group } C_2",font_size=30).move_to(circle3.get_right()+RIGHT)

        # Rotation 120° clockwise (A,B,C) → (B,C,A)
        animate_symmetry([1, 2, 0],[1, 2, 0],[1,0])

        # Rotation 240° clockwise (A,B,C) → (C,A,B)
        animate_symmetry([2, 0, 1],[2, 0, 1],[1,0])
        self.play(Write(label),Write(label2),Write(label3),run_time=0.2)
        # Reflection swapping B and C (A,B,C) → (A,C,B)
        animate_symmetry([1, 0, 2],[1, 2, 0],[1,0])
        animate_symmetry([1, 2, 0],[2, 0, 1],[1,0])
        # Rotation 240° clockwise (A,B,C) → (C,A,B)
        animate_symmetry([2, 0, 1],[1, 2, 0],[1,0])
        # Reflection swapping B and C (A,B,C) → (A,C,B)
        animate_symmetry([0, 2, 1],[2, 0, 1],[1,0])

class Solve(Scene):
    def construct(self):
        text = MathTex(r"\text{Let's solve}",font_size=60)
        self.play(Write(text),run_time=2)
        self.wait(2)

something = MathTex(r"\text{No Formula}")