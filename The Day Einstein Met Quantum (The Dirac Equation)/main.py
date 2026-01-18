from manim import *


class DiracAntimatter(Scene):
    def construct(self):
        try:
            photo = ImageMobject("media/Paul_Dirac,_1933.jpg")
        except FileNotFoundError:

            photo = Text("Image 'dirac.jpg' not found!", color=RED)
            print(
                "\nERROR: Please ensure 'dirac.jpg' is in the same folder as this script.\n"
            )

        photo.scale_to_fit_height(4)

        name = Tex("Paul Dirac", font_size=60)

        group = Group(photo, name)

        group.arrange(DOWN, buff=0.5)

        group.move_to(ORIGIN)

        self.wait(0.5)

        self.play(FadeIn(photo), run_time=2)

        self.play(Write(name))
        self.wait(3)

        equation = (
            MathTex(
                "i",
                "\\gamma^\\mu",
                "\\partial_\\mu",
                "\\psi",
                "-",
                "m",
                "\\psi",
                "=",
                "0",
                font_size=72,
            )
            .scale(0.7)
            .to_edge(UP)
        )
        self.play(FadeOut(photo, name))

        mirror_line = Line(DOWN * 2.5, UP * 1.5, color=GREY_B, stroke_width=4)

        matter_particle = Dot(point=LEFT * 2, color=GOLD, radius=0.2)
        matter_label = Tex("Matter", font_size=24).next_to(matter_particle, DOWN)

        antimatter_particle = Dot(point=RIGHT * 2, color=BLUE, radius=0.2)
        antimatter_label = Tex("Antimatter", font_size=24).next_to(
            antimatter_particle, DOWN
        )

        self.play(
            FadeIn(matter_particle),
            Write(matter_label),
            FadeIn(equation),
            Create(mirror_line),
        )

        self.play(
            TransformFromCopy(matter_particle, antimatter_particle),
            Write(antimatter_label),
            run_time=2,
            path_arc=-PI / 2,
        )

        self.play(FadeOut(Group(*self.mobjects)))


class DiracQuantumChaos(Scene):
    def construct(self):
        text1 = Tex("Negative Probabilities", font_size=60).shift(UP)
        text2 = Tex("infinite energies", font_size=60).shift(DOWN)
        self.play(Write(text1), run_time=2)
        self.play(Write(text2), run_time=2)
        self.wait(2)


class DiracQuote(Scene):
    def construct(self):
        text1 = Tex("Beauty", font_size=72)
        self.play(Write(text1), run_time=2.5)
        self.wait(0.5)
        self.play(FadeOut(text1))
        quote = Tex(
            r"``The underlying physical laws of nature should be expressed \\",
            r"in terms of equations of great ",
            "power",
            " and ",
            "beauty",
            ".''",
            font_size=38,
        ).to_edge(UP, buff=1.2)

        quote.set_color_by_tex("power", BLUE)
        quote.set_color_by_tex("beauty", GOLD)

        summary = Tex(
            "If the math was elegant, the physics must be right.",
            font_size=36,
            color=GOLD_A,
        ).shift(DOWN)

        implies = MathTex(r"\Downarrow", font_size=80).next_to(quote, DOWN, buff=0.5)

        self.play(Write(quote, run_time=6, rate_func=linear))
        self.wait(0.5)

        self.play(FadeIn(implies))

        self.play(Write(summary))

        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
        equation = MathTex(
            "i",
            "\\gamma^\\mu",
            "\\partial_\\mu",
            "\\psi",
            "-",
            "m",
            "\\psi",
            "=",
            "0",
            font_size=72,
        )
        text2 = Tex("The Equation", font_size=60).next_to(equation, UP)
        self.play(Write(text2), run_time=1.5)
        self.wait(2.5)
        self.play(Write(equation), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(Group(*self.mobjects)))

        einstein = MathTex(r"E^2 = (pc)^2 + (mc^2)^2", font_size=48).to_edge(UP, buff=1)

        self.play(Write(einstein), run_time=3)
        self.wait(1)

        sub_logic = Tex(
            r"Substitute: $E \rightarrow i\hbar \frac{\partial}{\partial t}$ and $p \rightarrow -i\hbar \nabla$",
            font_size=34,
            color=BLUE_A,
        ).next_to(einstein, DOWN, buff=0.5)

        self.play(FadeIn(sub_logic, shift=UP))
        self.wait(2)

        kg_eq = (
            MathTex(
                r"\frac{1}{c^2}\frac{\partial^2\psi}{\partial t^2} - \nabla^2\psi + \frac{m^2c^2}{\hbar^2}\psi = 0",
                font_size=42,
            )
            .move_to(ORIGIN)
            .shift(UP * 0.75)
        )

        self.play(Write(kg_eq), FadeOut(sub_logic), run_time=2)
        self.wait(3)

        time_derivative = kg_eq[0][4:10]

        flaw_box = SurroundingRectangle(time_derivative, color=RED, buff=0.2)
        flaw_text = Tex(
            r"Second-order in time ($\partial^2 / \partial t^2$)",
            color=RED,
            font_size=30,
        ).next_to(flaw_box, DOWN, buff=0.3)

        self.play(Create(flaw_box))
        self.play(Write(flaw_text))
        self.wait(2)

        catastrophe = MathTex(r"\rho < 0 \text{ ???}", color=RED, font_size=50).next_to(
            flaw_text, DOWN, buff=0.25
        )

        prob_label = Tex(
            r"Negative Probability Density", font_size=30, color=RED_B
        ).next_to(catastrophe, RIGHT, buff=0.5)

        self.play(Write(catastrophe))
        self.play(Indicate(catastrophe), Write(prob_label))

        cross = Cross(kg_eq, stroke_width=10, color=RED)
        unsuitable = Tex("Unsuitable for a single particle", font_size=40).shift(
            DOWN * 2
        )

        self.play(Create(cross))
        self.play(Write(unsuitable))

        self.wait(4)


class DiracSynthesis(Scene):
    def construct(self):

        e_squared = MathTex(r"E^2 = (pc)^2 + (mc^2)^2", font_size=50).to_edge(
            UP, buff=1
        )
        cross = Cross(e_squared, stroke_width=8, color=RED)

        requirement = Tex(
            r"Linear Equation: First-order in $\partial/\partial t$ and $\nabla$",
            font_size=30,
            color=GREY_B,
        ).next_to(e_squared, DOWN, buff=1)

        self.play(Write(e_squared))
        self.wait(1)
        self.play(Create(cross))
        self.play(Write(requirement))
        self.wait(3)

        schrodinger_hint = MathTex(
            r"i\hbar \frac{\partial\psi}{\partial t} = \hat{H}\psi",
            font_size=40,
            color=GREY_B,
        ).next_to(requirement, DOWN)
        self.play(Write(schrodinger_hint))
        self.wait(2)
        self.play(FadeOut(schrodinger_hint))
        sqrt_logic = MathTex(r"E = \sqrt{(pc)^2 + (mc^2)^2}", font_size=55)

        self.play(FadeOut(e_squared, cross, requirement), Write(sqrt_logic))
        self.wait(2)

        linear_ansatz = MathTex(r"E = \alpha p c + \beta m c^2", font_size=60).move_to(
            ORIGIN
        )

        self.play(Transform(sqrt_logic, linear_ansatz))
        self.wait(1)

        step1 = MathTex(
            r"i\hbar \frac{\partial \psi}{\partial t} = (-i\hbar c \alpha \nabla + \beta mc^2) \psi",
            font_size=50,
        ).move_to(ORIGIN)

        self.play(Transform(sqrt_logic, step1))
        self.wait(1.5)

        step2 = MathTex(
            r"i\hbar \frac{\partial \psi}{\partial t} + i\hbar c \alpha \nabla \psi - \beta mc^2 \psi = 0",
            font_size=45,
        ).move_to(ORIGIN)

        self.play(Transform(sqrt_logic, step2))
        self.wait(1.5)

        step3 = MathTex(
            r"i\hbar \gamma^0 \partial_0 \psi + i\hbar c \gamma^{\text{i}} \partial_{\text{i}} \psi - mc^2 \psi = 0",
            font_size=45,
        ).move_to(ORIGIN)

        self.play(Transform(sqrt_logic, step3))
        self.wait(1.5)

        final_dirac = MathTex(
            r"(i\hbar c \gamma^\mu \partial_\mu - mc^2) \psi = 0", font_size=45
        ).move_to(ORIGIN)

        self.play(Transform(sqrt_logic, final_dirac))
        self.wait(5)

        self.play(sqrt_logic.animate.scale(1.5))

        description = Tex(
            "Stunningly Simple. Linear. Relativistic.", font_size=40, color=BLUE_A
        ).next_to(sqrt_logic, DOWN, buff=1)
        self.play(Write(description), run_time=3)
        self.wait(5)


class DiracMystery(Scene):
    def construct(self):

        dirac_eq = MathTex(
            r"(i \gamma^\mu \partial_\mu - m) \psi = 0", font_size=48
        ).to_edge(UP, buff=1)
        self.play(Write(dirac_eq))
        self.wait(4)

        spinor = MathTex(
            r"\psi = \begin{pmatrix} \psi_1 \\ \psi_2 \\ \psi_3 \\ \psi_4 \end{pmatrix}",
            font_size=60,
        )

        spinor_label = Tex("4-Component Spinor", font_size=30, color=GRAY_B).next_to(
            spinor, DOWN
        )

        self.play(Write(spinor))
        self.play(Write(spinor_label))
        self.wait(2)

        self.play(spinor.animate.shift(LEFT * 3), spinor_label.animate.shift(LEFT * 3))
        self.wait(2)

        try:
            spin_img = ImageMobject("spin_viz.png").scale(1.5).shift(RIGHT * 3)
        except:
            spin_img = Rectangle(height=3, width=2, color=GREY).shift(RIGHT * 3)
            print("Placeholder: spin_viz.png not found")

        spin_text = (
            VGroup(
                Tex("Two-valued Spin", color=GRAY_B, font_size=30),
                Tex("Inherent \& Relativistic", color=GRAY_B, font_size=30),
            )
            .arrange(DOWN)
            .next_to(spin_img, DOWN)
        )

        self.play(FadeIn(spin_img, shift=LEFT))
        self.play(Write(spin_text))

        self.wait(3)

        self.play(
            FadeOut(spin_img),
            FadeOut(spin_text),
            FadeOut(spinor),
            FadeOut(spinor_label),
        )
