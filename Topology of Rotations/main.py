from manim import * # type: ignore


class SO3(ThreeDScene):
    def construct(self):
        text1 = Tex(r"SO$(3)$",font_size=80)
        self.play(Write(text1))
        text2 = Tex(r"Order: $\infty$",font_size=30).move_to(DOWN*1.5)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2+LEFT*0.2)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2.5+LEFT*0.2)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(text2,text3,tick,text4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=2)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        matrix_general = MathTex(
            "A = \\begin{pmatrix} a_{11} & a_{12} & a_{13} \\\\ a_{21} & a_{22} & a_{23} \\\\ a_{31} & a_{32} & a_{33} \\end{pmatrix}"
        ).scale(0.9)
        text6 = MathTex("a_{ij} \\in \\mathbb{R}, \\quad A^TA = I").scale(0.8)
        self.play(Write(matrix_general),run_time=0.7)
        self.wait(0.5)
        self.play(matrix_general.animate.move_to(UP*2))
        self.play(Write(text6),run_time=0.3)
        text5 = MathTex(r"Det(A) = 1").move_to(DOWN*1.6)
        self.play(Write(text5))
        self.wait(2)
        self.clear()
        axes = ThreeDAxes()
        cube = Cube(side_length=2, fill_opacity=0.3, fill_color=BLUE, stroke_width=1.5)

        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)

        self.add(axes, cube)

        self.play(Rotate(cube, angle=2 * PI, axis=OUT + RIGHT, run_time=5))
        self.wait(0.5)
        sphere = Sphere()
        self.remove(cube)
        self.add(sphere)

        self.play(Rotate(sphere, angle=2 * PI, axis=OUT + RIGHT, run_time=5))
        self.wait(0.5)

class SO32(ThreeDScene):
    def construct(self):
        text1 = Tex("Non-Abelian")
        self.play(Write(text1))
        text2 = Tex("Lie Group")
        self.play(text1.animate.shift(UP*2))
        self.play(Write(text2))
        self.wait(1)
        text3 = MathTex(r"\mathbb{RP}(3)").move_to(DOWN*2)
        self.play(Write(text3))
        self.wait(3)
        self.clear()
        sphere = Sphere(radius=2, fill_opacity=0.1, stroke_color=WHITE, resolution=(24, 48))
        dot = Dot3D(point=[0, 0, 0], color=YELLOW)

        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)
        self.add(sphere, dot)

        # Define motion path — point moves toward boundary, then reappears on opposite side
        path1 = lambda t: [0, 0, 2 * t]     # move along +z to boundary
        path2 = lambda t: [0, 0, -2 * t]    # reappear and move inward from -z

        # Animate the first motion (to boundary)
        self.play(UpdateFromAlphaFunc(dot, lambda m, a: m.move_to(path1(a))), run_time=1)
        # Fade flash to show identification
        flash = Circle(radius=0.3, color=YELLOW).move_to([0, 0, 2])
        self.play(ShowPassingFlash(flash, time_width=0.5, run_time=0.5))
        # Instantly jump dot to opposite side
        dot.move_to([0, 0, -2])
        # Continue inward motion
        self.play(UpdateFromAlphaFunc(dot, lambda m, a: m.move_to(path2(1 - a))), run_time=1)

        self.wait(0.5)
        self.clear()
        circle = Circle(radius=2, stroke_color=WHITE)
        fill = Circle(radius=2, fill_opacity=0.1, fill_color=BLUE, stroke_width=0)
        dot = Dot(point=[0, 0, 0], color=YELLOW)

        self.add(fill, circle, dot)
        # Path of motion: move from center to boundary along +x
        path1 = lambda t: [2 * t, 0, 0]
        path2 = lambda t: [-2 * t, 0, 0]

        # Move dot to boundary
        self.play(UpdateFromAlphaFunc(dot, lambda m, a: m.move_to(path1(a))), run_time=1)
        self.move_camera(
            phi=0 * DEGREES,
            theta=30 * DEGREES,
            run_time=0.5
        )
        # Flash to show boundary identification
        flash = Circle(radius=0.2, color=YELLOW).move_to([2, 0, 0])
        self.play(ShowPassingFlash(flash, time_width=0.5, run_time=0.5))

        # Jump to antipodal point and move back inward
        dot.move_to([-2, 0, 0])
        self.play(UpdateFromAlphaFunc(dot, lambda m, a: m.move_to(path2(1 - a))), run_time=1)

        self.wait(0.5)
        self.clear()
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)

        # 3D Axes for context
        axes = ThreeDAxes()
        self.add(axes)

        # Some arbitrary directions (not too aligned)
        directions = [
            normalize(np.array([1,  0,    0])),
            normalize(np.array([1,  0.2,  0.1])),
            normalize(np.array([1, -0.3,  0.4])),
            normalize(np.array([1,  0.4, -0.2])),
            normalize(np.array([0.8, 0.6,  0.1])),
            normalize(np.array([0.8, -0.6,  0.1])),
            normalize(np.array([0.9, 0.2,  0.3])),
            normalize(np.array([0.9, -0.2,  0.3])),
            normalize(np.array([0.7, 0.5,  0.5])),
            normalize(np.array([0.7, -0.5,  0.5])),
            normalize(np.array([0.7, 0.5, -0.5])),
            normalize(np.array([0.6, -0.5, -0.6])),
            normalize(np.array([0.6, 0.5, -0.6])),
            normalize(np.array([0.6, -0.6, 0.5])),
            normalize(np.array([0.5, 0.3, 0.8])),
            normalize(np.array([0.5, -0.3, 0.8])),
            normalize(np.array([0.5, 0.3, -0.8])),
            normalize(np.array([0.4, 0.9, 0.1])),
            normalize(np.array([0.4, -0.9, 0.1])),
            normalize(np.array([0.4, 0.1, 0.9])),
            normalize(np.array([0.4, -0.1, 0.9])),
            normalize(np.array([0.4, 0.1, -0.9])),
            normalize(np.array([0.3, 0.8, 0.5])),
            normalize(np.array([0.3, -0.8, 0.5])),
            normalize(np.array([0.3, 0.8, -0.5])),
            normalize(np.array([0.3, -0.8, -0.5])),
            normalize(np.array([0.2, 0.6, 0.8])),
            normalize(np.array([0.2, -0.6, 0.8])),
            normalize(np.array([0.2, 0.6, -0.8])),
            normalize(np.array([0.2, -0.6, -0.8])),
            normalize(np.array([0.9, 0.1, 0.2])),
            normalize(np.array([0.9, -0.1, 0.2])),
            normalize(np.array([0.9, 0.1, -0.2])),
            normalize(np.array([0.9, -0.1, -0.2])),
            normalize(np.array([0.95, 0.2, 0.05])),
            normalize(np.array([0.95, -0.2, 0.05])),
            normalize(np.array([0.95, 0.05, -0.2])),
            normalize(np.array([0.95, -0.05, -0.2])),
            normalize(np.array([0.7, 0.2, 0.7])),
            normalize(np.array([0.7, -0.2, 0.7])),
            normalize(np.array([0.7, 0.2, -0.7])),
            normalize(np.array([0.7, -0.2, -0.7])),
            normalize(np.array([0.6, 0.4, 0.7])),
            normalize(np.array([0.6, -0.4, 0.7])),
            normalize(np.array([0.6, 0.4, -0.7])),
            normalize(np.array([0.6, -0.4, -0.7])),
            normalize(np.array([0.8, 0.1, 0.6])),
            normalize(np.array([0.8, -0.1, 0.6])),
            normalize(np.array([0.8, 0.1, -0.6])),
            normalize(np.array([0.8, -0.1, -0.6]))
        ]

        # Create long lines through origin (scalar multiples)
        lines = VGroup()
        for d in directions:
            line = Line3D(
                start=-3*d,
                end=3*d,
                color=YELLOW,
                stroke_width=2
            )
            lines.add(line)

        self.add(lines)

        # Animate camera slowly orbiting
        self.begin_ambient_camera_rotation(rate=PI/16)

        # Animate lines shrinking toward radius = 1 sphere
        self.play(
            *[
                line.animate.become(Dot3D(d,radius=0.04, color=YELLOW))
                for d, line in zip(directions, lines)
            ],
            run_time=4,
            rate_func=smooth
        )

        hemisphere = Surface(
            lambda u, v: np.array([
                np.cos(u) * np.sin(v),
                np.sin(u) * np.sin(v),
                np.cos(v)
            ]),
            u_range=(-PI/2, PI/2),
            v_range=(0, PI),
            resolution=(32, 16),
            fill_color=BLUE,
            fill_opacity=0.3,
            stroke_color=WHITE,
            stroke_opacity=0.2
        )

        # Appear as combination of points
        self.play(FadeIn(hemisphere, run_time=2))
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.wait(1)
        self.remove(lines,axes)
        self.move_camera(phi=90*DEGREES,theta=0*DEGREES)
        circle = Surface(
            lambda u, v: np.array([
                0,
                1.5*np.sin(u) * np.sin(v),
                1.5*np.cos(v)
            ]),
            u_range=(-PI/2, PI/2),
            v_range=(0, PI),
            resolution=(32, 16),
            fill_color=BLUE,
            fill_opacity=0.3,
            stroke_color=WHITE,
            stroke_opacity=0.2
        )
        self.play(Transform(hemisphere,circle))
        self.wait(2)
