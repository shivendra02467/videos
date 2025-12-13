from manim import * # type: ignore
class Start(Scene):
    def construct(self):
        title = Tex(
            "The Classification of"
        ).scale(1.5).shift(LEFT*1.5)
        title2 = Tex("Finite Simple Groups").scale(1.5).shift(LEFT*1.5+DOWN)
        self.play(Write(title), run_time=1.5)
        self.play(Write(title2), run_time=1.5)
        self.wait(2)

class Start2(Scene):
    def construct(self):
        bg_image = ImageMobject("blobid1668114319182.png")
        small_brain = ImageMobject("image0.png")
        bg_image.scale_to_fit_height(config.frame_height)
        bg_image.move_to(ORIGIN)
        self.add(bg_image)

        image_paths = [
            "bitmap.png",  # Replace with your image file paths
            "vid2-thumbnail.png",
            "wallpaper.jpg",
            "rect20.png",
            "rect35.png",
            "image1.png",
            "sl2z.png",
        ]
        
        # Define the positions where the images will pop up
        positions = [
            UP + LEFT,
            DOWN + RIGHT,
            ORIGIN,
            UP + RIGHT,
            DOWN + LEFT,
            ORIGIN,
            UP + LEFT,
        ]
        
        # Create ImageMobjects for each image and place them at the given positions
        image_objects = [
            ImageMobject(image_path).set_height(2).move_to(position)
            for image_path, position in zip(image_paths, positions)
        ]
        
        # Add images one by one
        for image_object in image_objects:
            self.play(FadeIn(image_object),run_time=0.5)
            self.play(FadeOut(image_object),run_time=0.5)

        self.play(FadeIn(small_brain))
        self.wait(1)

        target_pos = UP * 10 + RIGHT * 10

        def spin_and_move(mob, alpha):
            # alpha goes from 0 → 1 during the animation
            start = ORIGIN
            end = target_pos
            mob.move_to(start + (end - start) * alpha)
            mob.rotate(-PI * 4 / 60)  # small rotation each frame

        # Wrap that into an UpdateFromAlphaFunc (real animation object)
        self.play(UpdateFromAlphaFunc(small_brain, spin_and_move),rate_func=linear, run_time=2)


class Trivial(Scene):
    def construct(self):
        text1 = MathTex(r"\{e\}",font_size=100)
        self.play(Write(text1))
        self.wait(2)

        text2 = Tex(r"Order: 1",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(text2,text3,tick,text4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=4)
        self.play(FadeOut(*self.mobjects))

        colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
        positions = [RIGHT*3+LEFT*1.5, RIGHT*3+LEFT*0.75,RIGHT*3 + ORIGIN,RIGHT*3+ RIGHT*0.75,RIGHT*3+ RIGHT*1.5]
        dots = VGroup(*[
            Dot(pos, color=colors[i],radius=0.25)
            for i, pos in enumerate(positions)
        ])
        triangle = Triangle(
            color=BLUE
        )
        triangle.set_fill(BLUE, opacity=0.5).scale(1.5).move_to(LEFT*3)
        text5 = Tex("The Zero Rotation in Rotations",font_size=18).move_to(DOWN*2+LEFT*3)
        text6 = Tex("The Identity Permutation in Permutations",font_size=18).move_to(DOWN*2+RIGHT*3)
        self.play(FadeIn(dots),Create(triangle),Write(text5),Write(text6))

        permutations = {
            "(1 2)": [1, 0, 2, 3, 4],
            "(1 2 3)": [1, 2, 0, 3, 4],
            "(1 5)(2 4)": [4, 3, 2, 1, 0],
        }
        vertices = triangle.get_vertices()   # returns an array of vertex coordinates
        centroid = np.mean(vertices, axis=0)
        # Show each permutation by moving dots to new positions
        for name, perm in permutations.items():
            # Compute new positions for dots according to perm
            new_positions = [positions[perm[i]] for i in range(5)]

            # Animate the dots moving
            self.play(*[
                dots[i].animate.move_to(new_positions[i])
                for i in range(5)
            ],Rotate(triangle,2*PI/3,about_point=centroid), run_time=1)

            # Move dots back to original positions except for last permutation
            if name != "(1 5)(2 4)":
                self.play(*[
                    dots[i].animate.move_to(positions[i])
                    for i in range(5)
                ], run_time=1)

class Tetra(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=38 * DEGREES,zoom=2)
        
        tetra = Tetrahedron(edge_length=2)

        colors = [RED, YELLOW,PURPLE ,BLUE]
        for i, face in enumerate(tetra.faces):
            face.set_fill(colors[i % len(colors)], opacity=0.6)

        self.add(tetra)


class Klein(Scene):
    def construct(self):
        text1 = MathTex(r"V_4",font_size=100)
        self.play(Write(text1))
        self.wait(1)

        text2 = Tex(r"Order: 4",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(text2,text3,tick,text4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=4)
        self.play(FadeOut(*self.mobjects))
        rect = Rectangle(width=4, height=2, color=BLUE, fill_color=BLUE, fill_opacity=0.6)

        rect.move_to(ORIGIN)

        self.play(Create(rect))
        self.wait(2)
        text1 = Tex(r"or Rotating zero degrees",font_size=20).move_to(DOWN*2)
        self.play(Write(text1))
        self.play(FadeOut(text1))
        def action_a():
            return rect.copy().flip(axis=UP)
        def action_b():
            return rect.copy().flip(axis=RIGHT)
        self.play(Rotate(rect,PI))
        self.wait(1)
        rect_b = action_b()
        self.play(Transform(rect, rect_b))
        self.wait(1)
        rect_a = action_a()
        self.play(Transform(rect, rect_a))
        self.wait(1)
        self.play(FadeOut(rect))
        image1 = ImageMobject("pexels-pixabay-276517.jpg").set(height=2.5).move_to(ORIGIN+LEFT*3)
        cross1 = Text("✗", color=YELLOW, font_size=60)
        cross1.scale(5).move_to(ORIGIN+LEFT*3)
        self.play(FadeIn(image1),Write(cross1))
        table_data = [
            ["Element", "Order"],
            ["$e$", "$1$"],
            ["$a$", "$2$"],
            ["$b$", "$2$"],
            ["$ab$", "$2$"]
        ]

        # Create the table
        table = Table(
            table_data,
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": WHITE},
            element_to_mobject=lambda x: Tex(x).scale(1)
        )
        table.move_to(ORIGIN+RIGHT*3).scale(0.5)
        self.wait(1)
        self.play(Create(table))
        self.wait(1)
        for i in range(2, len(table_data)):
            row = table.get_rows()[i]
            self.play(row.animate.set_fill(YELLOW, opacity=0.3), run_time=0.3)
            self.play(row.animate.set_fill(opacity=1), run_time=0.3)

        self.wait(2)

class Xor(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        elements = [0, 1, 2, 3]

        positions = {
            0: LEFT*2 + DOWN*2,
            1: LEFT*2 + UP*2,
            2: RIGHT*2 + DOWN*2,
            3: RIGHT*2 + UP*2
        }

        vertices = {x: Dot(positions[x], color=BLUE, radius=0.5) for x in elements}
        labels = {
            x: MathTex(bin(x)[2:], font_size=60, color=BLACK).next_to(vertices[x], 0.3 * OUT)
            for x in elements
        }

        for x in elements:
            self.play(Create(vertices[x]), FadeIn(labels[x]),run_time=0.6)

        # XOR connections
        generator_1_edges = [(x, x ^ 1) for x in elements if x < (x ^ 1)]
        temp = [(x ^ 1, x) for x in elements if x < (x ^ 1)]
        generator_1_edges = generator_1_edges+temp
        generator_2_edges = [(x, x ^ 2) for x in elements if x < (x ^ 2)]
        temp = [(x ^ 2, x) for x in elements if x < (x ^ 2)]
        generator_2_edges = generator_2_edges+temp
        generator_3_edges = [(x, x ^ 3) for x in elements if x < (x ^ 3)]
        temp = [(x ^ 3, x) for x in elements if x < (x ^ 3)]
        generator_3_edges = generator_3_edges+temp
        # Create arrows for generator 1 (⊕1)
        edges_gen1 = [
            Arrow(
                vertices[a].get_center() + 0.2 * (vertices[b].get_center() - vertices[a].get_center()),
                vertices[b].get_center() - 0.2 * (vertices[b].get_center() - vertices[a].get_center()),
                color=RED,
                buff=0,
                max_tip_length_to_length_ratio=0.2,
                stroke_width=3
            )
            for a, b in generator_1_edges
        ]

        # Create arrows for generator 2 (⊕2)
        edges_gen2 = [
            Arrow(
                vertices[a].get_center() + 0.2 * (vertices[b].get_center() - vertices[a].get_center()),
                vertices[b].get_center() - 0.2 * (vertices[b].get_center() - vertices[a].get_center()),
                color=YELLOW,
                buff=0,
                max_tip_length_to_length_ratio=0.2,
                stroke_width=3
            )
            for a, b in generator_2_edges
        ]

        edges_gen3 = [
            Arrow(
                vertices[a].get_center() + 0.2 * (vertices[b].get_center() - vertices[a].get_center()),
                vertices[b].get_center() - 0.2 * (vertices[b].get_center() - vertices[a].get_center()),
                color=BLUE,
                buff=0,
                max_tip_length_to_length_ratio=0.2,
                stroke_width=3
            )
            for a, b in generator_3_edges
        ]
        # Animate
        self.play(
            *[Create(edge) for edge in edges_gen1],
            *[Create(edge) for edge in edges_gen2],
            *[Create(edge) for edge in edges_gen3],
            run_time=2
        )
        self.wait(2)

class Rubik(Scene):
    def construct(self):
        text1 = Tex(r"Rubik's Group",font_size=80)
        self.play(Write(text1))
        self.wait(1)

        text2 = Tex(r"Order $\approx4\times10^{19}$",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(text2,text3,tick,text4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=4)
        self.play(FadeOut(*self.mobjects))

class Rubik2(Scene):
    def construct(self):
        text1 = MathTex(r"|G| = 43{,}252{,}003{,}274{,}489{,}856{,}000")
        formula = MathTex(
            r"|G| = \frac{8! \times 3^7 \times 12! \times 2^{11}}{2}"
        )
        self.play(Write(text1))
        self.wait(1)
        self.play(Transform(text1, formula))
        self.wait(1)
        corners_perm = MathTex("8!", "\\text{ (corner permutations)}",font_size=20).next_to(formula, DOWN,buff=0.5)
        edges_perm = MathTex("12!", "\\text{ (edge permutations)}",font_size=20).next_to(corners_perm, DOWN)
        corners_orient = MathTex("3^7", "\\text{ (corner orientations)}",font_size=20).next_to(edges_perm, DOWN)
        edges_orient = MathTex("2^{11}", "\\text{ (edge orientations)}",font_size=20).next_to(corners_orient, DOWN)
        parity = MathTex("\\div 2", "\\text{ (even permutation constraint)}",font_size=20).next_to(edges_orient, DOWN)
        group1 = VGroup(corners_perm, edges_perm, corners_orient, edges_orient, parity)
        self.play(Write(group1),run_time=2)
        self.wait(2)

class Numphile(Scene):
    def construct(self):
        tn1, tn2, tn3, tn4 = [
            ImageMobject("cubetn.jpg"),
            ImageMobject("cubetn2.jpg"),
            ImageMobject("cubetn3.jpg"),
            ImageMobject("cubetn4.jpg")
        ]

        # Position and initial scaling
        tn1.scale(0.1)
        tn2.move_to(DOWN*2.5+LEFT*2.5).scale(0.1)
        tn3.move_to(DOWN*2.5).scale(0.1)
        tn4.move_to(DOWN*2.5+RIGHT*2.5).scale(0.1)

        # Animate each
        self.play(tn1.animate.set(height=3), run_time=1)
        self.play(tn2.animate.set(height=1), run_time=1)
        self.play(tn3.animate.set(height=1), run_time=1)
        self.play(tn4.animate.set(height=1), run_time=1)

        self.wait(2)

class Cyclic(Scene):
    def construct(self):
        text1 = Tex(r"Cyclic Groups",font_size=80)
        texttemp = MathTex(r"(C_2, C_3, C_4, ...)").scale(0.75).next_to(text1,DOWN)
        self.play(Write(text1))
        text2 = Tex(r"Order: n",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        texttemp2 = Tex(r"for prime n").scale(0.4).next_to(text4,DOWN,buff=0.1)
        tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        cross = Text("✓", color=YELLOW, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(texttemp,text2,text3,tick,text4,texttemp2,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=3)
        self.play(FadeOut(*self.mobjects))

        text5 = MathTex(r"C_n")
        texttemp = MathTex(r"C_6").move_to(LEFT*4)
        self.wait(1)
        self.play(Write(text5))
        self.play(text5.animate.move_to(UP*2))
        image1=ImageMobject("cyclic (1).png").scale(2)
        self.play(FadeIn(image1))
        self.wait(1)
        self.play(FadeOut(image1))
        hexagon = RegularPolygon(n=6, start_angle=PI/6, fill_color=BLUE, fill_opacity=0.6)
        hexagon.scale(2).set_stroke(BLUE, width=6)
        self.play(Create(hexagon),Transform(text5,texttemp))
        self.wait(0.6)

        center = hexagon.get_center()
        rotations = [1, 2, 3, 4, 5]
        rotations_vis = [MathTex(f"{int(0)}^\\circ",font_size=30).move_to(RIGHT*4+UP*1.5),
                         MathTex(f"{int(60)}^\\circ",font_size=30).move_to(RIGHT*4+UP*1),
                         MathTex(f"{int(120)}^\\circ",font_size=30).move_to(RIGHT*4+UP*0.5),
                         MathTex(f"{int(180)}^\\circ",font_size=30).move_to(RIGHT*4),
                         MathTex(f"{int(240)}^\\circ",font_size=30).move_to(RIGHT*4+DOWN*0.5),
                         MathTex(f"{int(300)}^\\circ",font_size=30).move_to(RIGHT*4+DOWN*1)
                        ]
        self.play(Write(rotations_vis[0]))
        for k in rotations:
            angle = k * 60 * DEGREES
            radius = 2.6
            start_angle = 90*DEGREES 
            start_point = radius * np.array([np.cos(start_angle), np.sin(start_angle), 0])
            end_point = radius * np.array([np.cos(start_angle - angle), np.sin(start_angle - angle), 0])

            arrow = CurvedArrow(
                start_point=start_point,
                end_point=end_point,
                angle=-angle,
                color=YELLOW,
                stroke_width=4,
                tip_length=0.25
            )
            angle_label = MathTex(f"{int(k * 60)}^\\circ",font_size=30)
            mid_point = (
                radius * np.array([np.cos(start_angle - angle / 2), np.sin(start_angle - angle / 2), 0])
            )
            
            angle_label.move_to(mid_point * 0.9)
            angle_label.set_color(YELLOW)
            self.play(Create(arrow), FadeIn(angle_label), run_time=0.4)
            self.play(Rotate(hexagon, angle=-angle, about_point=center), run_time=0.6)
            self.play(Transform(angle_label,rotations_vis[k]))
            self.play(FadeOut(arrow), run_time=0.2)
            self.wait(0.3)

        self.play(FadeOut(*self.mobjects))
        self.wait(0.5)

        image1 = ImageMobject("pexels-pixabay-276517.jpg").set(height=2.5).move_to(ORIGIN+LEFT*3)
        cross1 = Text("✓", color=YELLOW, font_size=70)
        cross1.scale(5).move_to(ORIGIN+LEFT*3)
        self.play(FadeIn(image1),Write(cross1))
        table_data = [
            ["Element", "Order"],
            ["$e$", "$1$"],
            ["$g$", "$6$"],
            ["$g^2$", "$3$"],
            ["$g^3$", "$2$"],
            ["$g^4$", "$3$"],
            ["$g^5$", "$6$"]
        ]

        # Create the table
        table = Table(
            table_data,
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": WHITE},
            element_to_mobject=lambda x: Tex(x).scale(1)
        )
        table.move_to(ORIGIN+RIGHT*3).scale(0.5)
        self.wait(1)
        self.play(Create(table))
        self.wait(1)
        row = table.get_rows()[2]
        self.play(row.animate.set_fill(YELLOW, opacity=0.3), run_time=0.5)
        self.play(row.animate.set_fill(opacity=1), run_time=0.5)
        row = table.get_rows()[6]
        self.play(row.animate.set_fill(YELLOW, opacity=0.3), run_time=0.5)
        self.play(row.animate.set_fill(opacity=1), run_time=0.5)

        self.wait(3)
        
class Dihedral(Scene):
    def construct(self):
        text1 = Tex(r"Dihedral Groups",font_size=80)
        texttemp = MathTex(r"(D_1, D_2, D_3, ...)").scale(0.75).next_to(text1,DOWN)
        self.play(Write(text1))
        text2 = Tex(r"Order: 2n",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        texttemp2 = Tex(r"for $n\ge3$").scale(0.4).next_to(text3,DOWN,buff=0.1)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        texttemp3 = Tex(r"for $n\ge2$").scale(0.4).next_to(text4,DOWN,buff=0.1)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(texttemp,text2,text3,texttemp2,tick,text4,texttemp3,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=3)
        self.play(FadeOut(*self.mobjects))
        text5 = MathTex(r"D_n = C_n \times C_2")
        self.play(Write(text5))
        self.wait(1)
        self.play(FadeOut(text5))
        hexagon = RegularPolygon(n=6, start_angle=PI/6, fill_color=BLUE, fill_opacity=0.6)
        hexagon.scale(2).set_stroke(BLUE, width=6)
        self.play(Create(hexagon))
        self.wait(1)

        center = hexagon.get_center()
        angle = 60 * DEGREES
        radius = 2.6
        start_angle = 90*DEGREES 
        start_point = radius * np.array([np.cos(start_angle), np.sin(start_angle), 0])
        end_point = radius * np.array([np.cos(start_angle - angle), np.sin(start_angle - angle), 0])

        arrow = CurvedArrow(
            start_point=start_point,
            end_point=end_point,
            angle=-angle,
            color=YELLOW,
            stroke_width=4,
            tip_length=0.25
        )

        group1 = VGroup(MathTex(f"{int(0)}^\\circ",font_size=30).move_to(RIGHT*4+UP*1.5),
                         MathTex(f"{int(60)}^\\circ",font_size=30).move_to(RIGHT*4+UP*1),
                         MathTex(f"{int(120)}^\\circ",font_size=30).move_to(RIGHT*4+UP*0.5),
                         MathTex(f"{int(180)}^\\circ",font_size=30).move_to(RIGHT*4),
                         MathTex(f"{int(240)}^\\circ",font_size=30).move_to(RIGHT*4+DOWN*0.5),
                         MathTex(f"{int(300)}^\\circ",font_size=30).move_to(RIGHT*4+DOWN*1)
        )
        group2 = VGroup(MathTex(f"{int(0)}^\\circ\\text{{axis}}",font_size=30).move_to(RIGHT*5.5+UP*1.5),
                         MathTex(f"{int(30)}^\\circ\\text{{axis}}",font_size=30).move_to(RIGHT*5.5+UP*1),
                         MathTex(f"{int(60)}^\\circ\\text{{axis}}",font_size=30).move_to(RIGHT*5.5+UP*0.5),
                         MathTex(f"{int(90)}^\\circ\\text{{axis}}",font_size=30).move_to(RIGHT*5.5),
                         MathTex(f"{int(120)}^\\circ\\text{{axis}}",font_size=30).move_to(RIGHT*5.5+DOWN*0.5),
                         MathTex(f"{int(150)}^\\circ\\text{{axis}}",font_size=30).move_to(RIGHT*5.5+DOWN*1)
        )
        self.play(Write(group1),Rotate(hexagon, angle=-angle, about_point=center),Create(arrow))
        self.play(FadeOut(arrow), run_time=0.2)
        self.wait(1)
        angle_label = MathTex(f"{int(90)}^\\circ\\text{{axis}}",font_size=30)
        axis_line = Line(
            start=[-3, 0, 0],
            end=[3, 0, 0],
            color=YELLOW
        )
        angle_label.set_color(YELLOW).next_to(axis_line,UP)
        angle_label.shift(RIGHT*2.5)
        reflected_hexagon = hexagon.copy()
        reflected_hexagon.flip(axis=RIGHT, about_point=center)
        self.play(Write(group2),Create(axis_line),Write(angle_label),Transform(hexagon, reflected_hexagon))
        text6 = MathTex(r"2n \text{ elements}",font_size=30).move_to(RIGHT*4.5+DOWN*2)
        self.play(Write(text6))
        self.wait(4)
        self.play(FadeOut(*self.mobjects))
        
class Alter(Scene):
    def construct(self):
        text1 = Tex(r"Alternating Groups",font_size=80)
        texttemp = MathTex(r"(A_2, A_3, A_4, ...)").scale(0.75).next_to(text1,DOWN)
        self.play(Write(text1))
        text2 = Tex(r"Order: n!/2",font_size=30).move_to(LEFT*3.5+DOWN*2)
        texttemp2 = Tex(r"for $n\ge2$").scale(0.4).next_to(text2,DOWN,buff=0.1)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        texttemp3 = Tex(r"for $n\ge4$").scale(0.4).next_to(text3,DOWN,buff=0.1)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        texttemp4 = Tex(r"for $n\ge5$").scale(0.4).next_to(text4,DOWN,buff=0.1)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✓", color=YELLOW, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(texttemp,text2,texttemp2,text3,texttemp3,tick,text4,texttemp4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=3)
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.wait(5)
        text5 = MathTex("A_n")
        self.play(Write(text5))
        self.play(text5.animate.move_to(UP*2))
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
        positions = [LEFT*1.5,LEFT*0.75,ORIGIN,RIGHT*0.75,RIGHT*1.5]
        dots = VGroup(*[
            Dot(pos, color=colors[i],radius=0.25)
            for i, pos in enumerate(positions)
        ])
        # triangle = Triangle(
        #     color=BLUE
        # )
        # triangle.set_fill(BLUE, opacity=0.5).scale(1.5).move_to(LEFT*3)
        # text5 = Text("The Zero Rotation in Rotations",font_size=18).move_to(DOWN*2+LEFT*3)
        text6 = Tex("Even Permutations of 5 elements",font_size=18).move_to(DOWN*1.5)
        text7 = MathTex("A_5\\space \\cong").move_to(LEFT*3)
        self.play(FadeIn(dots),Write(text7),run_time=1)
        permutations = {
            "(1 2)(3 4)": [1, 0, 3, 2, 4],
            "(1 2 3 4 5)": [1, 2, 3, 4, 0],
        }
        flag = True
        for name, perm in permutations.items():
            new_positions = [positions[perm[i]] for i in range(5)]
            self.play(*[
                dots[i].animate.move_to(new_positions[i])
                for i in range(5)
            ], run_time=0.6)
            if flag:
                flag = False
                self.play(Write(text6),run_time=0.5)
            if name != "(1 5)(2 4)":
                self.play(*[
                    dots[i].animate.move_to(positions[i])
                    for i in range(5)
                ], run_time=0.6)
        self.wait(1)
        self.play(FadeOut(*self.mobjects),run_time=0.5)
        groups = ["A_5", "A_6", "A_7"]
        group_nodes = VGroup(*[Circle(color=BLUE, radius=0.6).add(MathTex(g, font_size=30)) for g in groups])
        group_nodes.arrange(RIGHT, buff=2)
        group_nodes.move_to(UP*1.5)

        # Trivial groups under each
        trivial_nodes = VGroup(*[Circle(color=GRAY, radius=0.4).add(MathTex("\\{e\\}", font_size=24)) for _ in groups])
        trivial_nodes.arrange(RIGHT, buff=2)
        trivial_nodes.next_to(group_nodes, DOWN, buff=1.5)

        # Arrows between them
        arrows = VGroup(*[
            Arrow(start=t.get_top(), end=g.get_bottom(), buff=0.1, color=YELLOW)
            for t, g in zip(trivial_nodes, group_nodes)
        ])

        # Display nodes
        self.play(LaggedStart(*[Create(g) for g in group_nodes], lag_ratio=0.3))
        self.play(LaggedStart(*[Create(t) for t in trivial_nodes], lag_ratio=0.3))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.3))
        self.wait(0.5)

        # Add labels
        normal_texts = [
            MathTex("\\{e\\} \\triangleleft A_5", font_size=24),
            MathTex("\\{e\\} \\triangleleft A_6", font_size=24),
            MathTex("\\{e\\} \\triangleleft A_7", font_size=24),
        ]
        for t, a in zip(normal_texts, arrows):
            t.next_to(a, LEFT, buff=0.1)
        self.play(LaggedStart(*[Write(t) for t in normal_texts], lag_ratio=0.2))
        group2 = VGroup(group_nodes,trivial_nodes,arrows,normal_texts)
        image1 = ImageMobject("vid1-thumbnail.png").set(height=2.5).move_to(RIGHT*3)
        self.play(group2.animate.scale(0.75).move_to(LEFT*3),FadeIn(image1))
        text8 = Tex("Galois Theory",font_size=24).next_to(image1,DOWN)
        self.play(Write(text8))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

import random
class Alter2(Scene):
    def construct(self):
        title = Tex(r"\bf Geometry",color=BLACK).scale(1.5)
        title.scale(1.2)
        circle = Circle(radius=2.5, color=BLUE_B, fill_color=BLUE, fill_opacity=0.6).set_stroke(width=4)
        square = Square(side_length=3.5, color=PURPLE_B, fill_color=BLUE, fill_opacity=0.6).set_stroke(width=3)
        triangle = RegularPolygon(3, color=YELLOW_B, fill_color=BLUE, fill_opacity=0.6).set_stroke(width=3)
        circle_rot = circle.copy().set_color(TEAL_A)
        square_rot = square.copy().set_color(GREEN_A)
        triangle_rot = triangle.copy().set_color(ORANGE)

        shapes = VGroup(circle_rot, square_rot, triangle_rot)
        dots = VGroup(*[Dot(radius=0.1, color=random.choice([RED, GOLD, PINK])) for _ in range(10)])
        for i, dot in enumerate(dots):
            dot.move_to(2.8 * RIGHT).rotate(i * TAU / 10, about_point=ORIGIN)

        self.add(dots,shapes)
        self.play(
            Rotate(shapes, angle=PI*0.375, about_point=ORIGIN, run_time=1, rate_func=linear),
            Rotate(dots, angle=PI*0.375, about_point=ORIGIN, run_time=1, rate_func=linear),
        )
        self.play(
            Rotate(shapes, angle=PI*0.75, about_point=ORIGIN, run_time=3, rate_func=linear),
            Rotate(dots, angle=PI*0.75, about_point=ORIGIN, run_time=3, rate_func=linear),
            Write(title)
        )
        self.play(FadeOut(*self.mobjects))
        text1 = MathTex("A_n").move_to(UP*2)
        self.play(Write(text1))
        image1 = ImageMobject("image-1.png").set(height=2.5)
        self.play(FadeIn(image1),run_time=2)
        text2 = Tex("drawn in 2D as complete graphs",font_size=20).next_to(image1,DOWN)
        self.play(Write(text2))
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        image2 = ImageMobject("simplex1.png")
        image3 = ImageMobject("simplex-illustration.jpg")

        image2.move_to(RIGHT * 2).scale(0.3)
        image3.move_to(LEFT * 2).scale(0.3)

        # Animate each
        self.play(image2.animate.set(height=2), run_time=1)
        self.play(image3.animate.set(height=2), run_time=1)
        text3 = Tex("Linear Programming",font_size=20).next_to(image2,DOWN)
        text3.shift(LEFT*2)
        self.play(Write(text3))
        self.wait(1)

class Alter3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES,zoom=2.75)
        text1 = Tex("Smallest n dimensional shape").move_to(UP*2.5)
        self.add_fixed_in_frame_mobjects(text1)
        self.play(Write(text1))
        line = Line(LEFT, RIGHT)
        self.add_fixed_in_frame_mobjects(line)
        line.set_color(BLUE)
        line.set_stroke(width=5)
        self.play(Create(line))
        self.wait(2)
        self.play(line.animate.shift(LEFT*3))
        triangle = Triangle(
            color=BLUE
        )
        triangle.set_fill(BLUE, opacity=0.5).scale(1.5)
        self.add_fixed_in_frame_mobjects(triangle)
        self.play(Create(triangle))
        vertices = triangle.get_vertices()
        centroid = np.mean(vertices, axis=0)
        self.play(Rotate(triangle,2*PI/3,about_point=centroid))
        self.wait(1)
        tetra = Tetrahedron().move_to(UP*1.5)
        axis = [1, 1, 1]
        self.play(Rotate(tetra, angle=120 * DEGREES, axis=axis), run_time=2)
        self.wait(1)
        axis = [0, 1, 0]
        self.play(Rotate(tetra, angle=180 * DEGREES, axis=axis), run_time=2)
        self.wait(1)

class FourD(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)
        k = 3  # perspective factor

        # Define 4-simplex vertices in 4D
        verts4D = np.array([
            [1, 1, 1, -1/np.sqrt(5)],
            [1, -1, -1, -1/np.sqrt(5)],
            [-1, 1, -1, -1/np.sqrt(5)],
            [-1, -1, 1, -1/np.sqrt(5)],
            [0, 0, 0, 4/np.sqrt(5)],
        ])

        # Projection function 4D -> 3D
        def project(v):
            w = v[3]
            return v[:3] / (k - w)

        # Draw all edges
        edges = []
        for i in range(len(verts4D)):
            for j in range(i + 1, len(verts4D)):
                start = 3*project(verts4D[i])
                end = 3*project(verts4D[j])
                edges.append(Line3D(start, end, color=BLUE))

        simplex = VGroup(*edges)
        self.add(simplex)

        # Define 4D rotation matrix in X-W plane
        def rotate4D(points, theta):
            R = np.eye(4)
            c, s = np.cos(theta), np.sin(theta)
            # rotation in X-W plane
            R[0, 0] = c
            R[0, 3] = -s
            R[3, 0] = s
            R[3, 3] = c
            return points @ R.T

        # Animate the 4D rotation projected to 3D
        def update_simplex(mob, alpha):
            theta = alpha * 2 * np.pi  # full 360° 4D rotation
            rotated = rotate4D(verts4D, theta)
            for (i, line) in enumerate(edges):
                a, b = divmod(i, len(verts4D))
            lines = []
            idx = 0
            for i in range(len(verts4D)):
                for j in range(i + 1, len(verts4D)):
                    start = 3*project(rotated[i])
                    end = 3*project(rotated[j])
                    lines.append(Line3D(start, end, color=BLUE))
                    idx += 1
            mob.become(VGroup(*lines))
        text1 = Tex("3D projection of the 4-simplex",font_size=20).move_to(DOWN*3)
        self.add_fixed_in_frame_mobjects(text1)
        self.play(UpdateFromAlphaFunc(simplex, update_simplex),Write(text1), run_time=4, rate_func=linear,)
        
        self.wait()

class Symmetry(ThreeDScene):
    def construct(self):
        text1 = Tex(r"Symmetric Groups",font_size=80)
        texttemp = MathTex(r"(S_2, S_3, S_4, ...)").scale(0.75).next_to(text1,DOWN)
        self.play(Write(text1))
        text2 = Tex("Order: n!",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        texttemp2 = Tex(r"for $n\ge3$").scale(0.4).next_to(text3,DOWN,buff=0.1)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        texttemp3 = Tex(r"for $n\ge3$").scale(0.4).next_to(text4,DOWN,buff=0.1)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(texttemp,text2,text3,texttemp2,tick,text4,texttemp3,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=2)
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.set_camera_orientation(phi=20 * DEGREES, theta=0 * DEGREES,zoom=2.75)
        text1 = Tex("Rotaions and Reflections",font_size=30).move_to(UP*2.5)
        self.add_fixed_in_frame_mobjects(text1)
        line = Line(LEFT, RIGHT).move_to(LEFT*3)
        self.add_fixed_in_frame_mobjects(line)
        line.set_color(BLUE)
        line.set_stroke(width=5)
        triangle = Triangle(
            color=BLUE
        )
        triangle.set_fill(BLUE, opacity=0.5).scale(1.5)
        self.add_fixed_in_frame_mobjects(triangle)
        self.play(Create(triangle),Create(line),Write(text1))
        vertices = triangle.get_vertices()
        centroid = np.mean(vertices, axis=0)
        tetra = Tetrahedron().move_to(UP*1.5)
        axis = [1, 1, 1]
        self.play(Rotate(tetra, angle=120 * DEGREES, axis=axis),Rotate(triangle,2*PI/3,about_point=centroid), run_time=2)
        plane = Polygon(
            [0.5, 0.5, -1.5]+UP*1.5,
            [0.5, 0.5, 1.5]+UP*1.5,
            [-0.5, -0.5, 1.5]+UP*1.5,
            [-0.5, -0.5, -1.5]+UP*1.5,
            color=YELLOW,
            fill_opacity=0.25,
            stroke_opacity=0.25
        )
        line2 = Line(UP*1.8,DOWN*1.5,color=YELLOW,stroke_opacity=0.25)
        self.add_fixed_in_frame_mobjects(line2)
        self.add(plane,line2)
        self.wait(1)
        def reflect_x_y(mob: Mobject):
            mob_copy = mob.copy()
            for submob in mob_copy.family_members_with_points():
                pts = submob.get_points()
                if pts.size == 0:
                    continue
                reflected = np.copy(pts)
                reflected[:, [0, 1]] = reflected[:, [1, 0]]  # swap x and y
                submob.set_points(reflected)
            mob_copy.move_to(UP*1.5)
            return mob_copy

        self.play(ApplyFunction(reflect_x_y, tetra),triangle.animate.flip(), run_time=2)
        self.wait(1)

class Symmetry2(Scene):
    def construct(self):
        image1 = ImageMobject("Tetrahedral_group_2.png") 
        self.play(FadeIn(image1),run_time=2)
        self.wait(2)
        self.play(FadeOut(image1),run_time=1)
        text1 = MathTex(r"A_n \triangleleft S_n")
        self.play(Write(text1))
        self.wait(2)

import math
class Units(Scene):
    def construct(self):
        text1 = MathTex(r"(\mathbb{Z}/n\mathbb{Z})^\times",font_size=80)
        texttemp = MathTex(r"(\mathbb{Z}_2^\times, \mathbb{Z}_3^\times, \mathbb{Z}_4^\times, ...)").scale(0.5).next_to(text1,DOWN)
        self.play(Write(text1))
        text2 = Tex(r"Order: $\phi(n)$",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex("Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex("Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        texttemp3 = Tex(r"if $n\notin\{3,4,6\}$").scale(0.4).next_to(text4,DOWN,buff=0.1)
        tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(texttemp,text2,text3,tick,text4,texttemp3,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=2)
        self.wait(3)
        self.play(FadeOut(text1,texttemp,text3,text4,tick,cross,texttemp3))
        texttemp = MathTex(r"\phi(n)",font_size=80)
        self.play(Transform(text2,texttemp))
        text5 = Text("Euler's Totient Function",font_size=20).move_to(DOWN*1.5)
        self.play(Write(text5))
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        groups = [
            (r"\mathbb{Z}^*_p"),
            (r"\mathbb{Z}^*_n"),
            (r"\mathbb{F}^*_q"),
            (r"G_1"),
            (r"G_T"),
            (r"G_2"),
            (r"C_{26}"),
            (r"C_{256}")
        ]
        colors = [BLUE, GREEN, YELLOW, ORANGE, PURPLE, TEAL, RED, PINK]

        texts = []

        # === Define geometric layout ===
        outer_radius = 3   # For the big triangle
        inner_radius = 1.5   # For the inner pentagon

        # 3 vertices of an upright triangle
        triangle_points = [
            [0,  -outer_radius, 0],
            [-outer_radius * math.cos(PI / 6), outer_radius / 2, 0],
            [ outer_radius * math.cos(PI / 6), outer_radius / 2, 0],
        ]

        # 5 vertices of a pentagon (rotated a bit for symmetry)
        pentagon_points = [
            [inner_radius * math.cos(2 * PI * i / 5 + PI / 2),
             inner_radius * math.sin(2 * PI * i / 5 + PI / 2),
             0]
            for i in range(5)
        ]

        # Combine triangle (3) + pentagon (5)
        positions = pentagon_points + triangle_points

        # === Create MathTex objects ===
        for i, name in enumerate(groups):
            color = colors[i % len(colors)]
            pos = positions[i]
            title = MathTex(name, color=color).move_to(pos)
            texts.append(title)
        animations = []
        for g in texts:
            animations.append(FadeIn(g, scale=0.5,run_time=0.5))

        self.play(LaggedStart(*animations, lag_ratio=0.4, run_time=2))
        self.wait(1)

class Abelian(Scene):
    def construct(self):
        text1 = Text("Abelian").move_to(UP)
        self.play(Write(text1))
        text2 = MathTex(r"ab = ba").move_to(DOWN)
        self.play(Write(text2))
        text3 = MathTex(r"\text{for all }\mathbb{Z}^*_n",font_size=25).move_to(DOWN*2)
        self.play(Write(text3))
        self.wait(2)

from manim import *
from math import gcd

def group_elements(n):
    """Return list of elements coprime to n."""
    return [a for a in range(1, n) if gcd(a, n) == 1]

def group_type(n):
    """Return simple classification."""
    if n in [3, 4, 5, 7, 9, 10, 11]:
        return "Cyclic"
    elif n in [8, 12]:
        return "Klein 4-group"
    else:
        return "Trivial"

class Units2(Scene):
    def construct(self):
        ns = [3, 4, 5, 7, 8, 9, 10, 12]
        groups = VGroup()

        for n in ns:
            elems = group_elements(n)
            m = len(elems)
            circle = Circle(radius=0.8, color=WHITE)

            pts, labs = VGroup(), VGroup()
            for i, a in enumerate(elems):
                angle = 2 * PI * i / m
                pt = Dot(circle.point_at_angle(angle), color=RED, radius=0.15)
                lab = MathTex(str(a), font_size=20,color=BLACK).next_to(pt, OUT, buff=0.12)
                pts.add(pt)
                labs.add(lab)

            group_viz = VGroup(circle, pts, labs)

            n_label = Tex(f"n = {n}", font_size=22).next_to(circle, DOWN, buff=0.05).shift(DOWN*0.5)
            type_label = Tex(group_type(n), font_size=20).next_to(n_label, DOWN, buff=0.05)
            if group_type(n)=="Klein 4-group":
                group_viz[0].set_color(BLACK)
            group_box = VGroup(group_viz, n_label, type_label)
            groups.add(group_box)

        # Arrange neatly in 2x4 grid
        groups.arrange_in_grid(rows=2, buff=1.2)
        self.play(FadeIn(groups))
        self.wait(0.5)

        # Animate each briefly
        for i, n in enumerate(ns):
            grp = groups[i][0]  # the circle+points+labels
            kind = group_type(n)
            if "Cyclic" in kind:
                self.play(Rotate(grp, angle=2*PI/len(group_elements(n)), run_time=1.5))
            elif "Klein" in kind:
                pts = grp[1]
                elements = [0, 1, 2, 3]
                generator_1_edges = [(x, x ^ 1) for x in elements if x < (x ^ 1)]
                temp = [(x ^ 1, x) for x in elements if x < (x ^ 1)]
                generator_1_edges = generator_1_edges+temp
                generator_2_edges = [(x, x ^ 2) for x in elements if x < (x ^ 2)]
                temp = [(x ^ 2, x) for x in elements if x < (x ^ 2)]
                generator_2_edges = generator_2_edges+temp
                generator_3_edges = [(x, x ^ 3) for x in elements if x < (x ^ 3)]
                temp = [(x ^ 3, x) for x in elements if x < (x ^ 3)]
                generator_3_edges = generator_3_edges+temp
                # Create arrows for generator 1 (⊕1)
                edges_gen1 = [
                    Arrow(
                        pts[a].get_center() + 0.2 * (pts[b].get_center() - pts[a].get_center()),
                        pts[b].get_center() - 0.2 * (pts[b].get_center() - pts[a].get_center()),
                        buff=0,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2
                    )
                    for a, b in generator_1_edges
                ]

                # Create arrows for generator 2 (⊕2)
                edges_gen2 = [
                    Arrow(
                        pts[a].get_center() + 0.2 * (pts[b].get_center() - pts[a].get_center()),
                        pts[b].get_center() - 0.2 * (pts[b].get_center() - pts[a].get_center()),
                        color=RED,
                        buff=0,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2
                    )
                    for a, b in generator_2_edges
                ]

                edges_gen3 = [
                    Arrow(
                        pts[a].get_center() + 0.2 * (pts[b].get_center() - pts[a].get_center()),
                        pts[b].get_center() - 0.2 * (pts[b].get_center() - pts[a].get_center()),
                        color=BLUE,
                        buff=0,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2
                    )
                    for a, b in generator_3_edges
                ]

                # Animate
                
                self.play(
                    *[Create(edge) for edge in edges_gen1],
                    *[Create(edge) for edge in edges_gen2],
                    *[Create(edge) for edge in edges_gen3],
                    run_time=1.5
                )
            else:
                self.play(Wiggle(grp, scale_value=1.05))
            self.wait(0.3)

        self.wait(3)

class Modular(Scene):
    def construct(self):
        text1 = Tex(r"SL$(2, \mathbb{Z})$",font_size=80)
        self.play(Write(text1))
        text2 = Tex(r"Order: $\infty$",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex("Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex("Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(text2,text3,tick,text4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(*self.mobjects),run_time=0.5)
        matrix_general = MathTex(
            "A = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}, \\quad a,b,c,d \\in \\mathbb{Z}, \\quad ad - bc = 1"
        ).scale(0.9)
        self.play(Write(matrix_general))
        self.wait(1.5)
        self.play(matrix_general.animate.move_to(UP*2))
        text5 = MathTex(r"z \mapsto \frac{az+b}{cz+d}")
        self.play(Write(text5))
        self.wait(2)

class SO3(ThreeDScene):
    def construct(self):
        text1 = Tex(r"SO$(3)$",font_size=80)
        self.play(Write(text1))
        text2 = Tex(r"Order: $\infty$",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(text2,text3,tick,text4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=2)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        matrix_general = MathTex(
            "A = \\begin{pmatrix} a_{11} & a_{12} & a_{13} \\\\ a_{21} & a_{22} & a_{23} \\\\ a_{31} & a_{32} & a_{33} \\end{pmatrix}, \\quad a_{ij} \\in \\mathbb{R}, \\quad A^TA = I"
        ).scale(0.9)
        self.play(Write(matrix_general))
        self.wait(0.5)
        self.play(matrix_general.animate.move_to(UP*2))
        text5 = MathTex(r"Det(A) = 1")
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


class SU2(ThreeDScene):
    def construct(self):
        text1 = Tex(r"SU$(2)$",font_size=80)
        self.play(Write(text1))
        text2 = Tex(r"Order: $\infty$",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(text2,text3,tick,text4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=2)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        matrix_general = MathTex(
            "A = \\begin{pmatrix} a_{11} & a_{12} \\\\ a_{21} & a_{22} \\end{pmatrix}, \\quad a_{ij} \\in \\mathbb{C}, \\quad A^\\dagger A = I"
        ).scale(0.9)
        self.play(Write(matrix_general))
        self.play(matrix_general.animate.move_to(UP*2),run_time=0.5)
        text5 = MathTex(r"Det(A) = 1")
        self.play(Write(text5))
        self.wait(2)
        self.clear()  
        title = MathTex(r"\text{Pauli matrices }(\sigma_x, \sigma_y, \sigma_z)",font_size=32)
        title.move_to(UP*2)
        self.play(Write(title))

        sigma_x = MathTex(
            "\\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}"
        ).scale(0.9)
        sigma_y =  MathTex(
            "\\begin{pmatrix} 0 & -i \\\\ i & 0 \\end{pmatrix}"
        ).scale(0.9)
        sigma_z =  MathTex(
            "\\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}"
        ).scale(0.9)

        group = VGroup(sigma_x, sigma_y, sigma_z).arrange(RIGHT, buff=1.2).scale(0.8)
        group.next_to(title, DOWN,buff=1.5)
        labels = VGroup(MathTex(r"\sigma_x"), MathTex(r"\sigma_y"), MathTex(r"\sigma_z")).arrange(RIGHT, buff=1.75).next_to(group, DOWN)

        self.play(Write(group), Write(labels))
        self.wait(0.8)

        # show commutation / anticommutation facts
        facts = VGroup(
            MathTex(r"\{\sigma_i, \sigma_j\} = 2\delta_{ij} I"),
            MathTex(r"[\sigma_i, \sigma_j] = 2 i \epsilon_{ijk} \sigma_k")
        ).arrange(DOWN).scale(0.6).next_to(labels,DOWN,buff=1.5)
        self.play(AnimationGroup(Write(facts), lag_ratio=0.2))
        self.wait(1.6)
        self.clear()

class SU22(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=90 * DEGREES)


        # Two overlapping spheres to represent S^3 as two 3-balls with boundary identification
        sphere1 = Sphere(radius=2, fill_opacity=0.08, stroke_color=BLUE, resolution=(24, 48))
        sphere1.shift(LEFT*2)
        sphere2 = Sphere(radius=2, fill_opacity=0.08, stroke_color=GREEN, resolution=(24, 48))
        sphere2.shift(RIGHT * 2)


        self.add(sphere1, sphere2)


        # Dot representing a point moving through the manifold
        dot = Dot3D(point=[-2, 0, 0], color=YELLOW)
        self.add(dot)


        # Define paths inside each ball
        path1 = lambda t: np.array([-2, 0, 2 * t]) # inside Ball 1 toward +z boundary
        path2 = lambda t: np.array([2, 0, -2 + 4 * t]) # inside Ball 2 from -z boundary inward


        # Animate dot moving to boundary of first sphere
        self.play(UpdateFromAlphaFunc(dot, lambda m, a: m.move_to(path1(a))), run_time=1.5)


        # Flash at boundary to indicate transition to other ball
        flash1 = Circle(radius=0.3, color=YELLOW).move_to([-2, 0, 2])
        self.play(ShowPassingFlash(flash1, time_width=0.5, run_time=0.5))

        flash2 = Circle(radius=0.3, color=YELLOW).move_to([2, 0, -2])
        self.play(ShowPassingFlash(flash2, time_width=0.5, run_time=0.5))
        # Instantly move to boundary of second sphere (identified boundary)
        dot.move_to([2, 0, -2])


        # Continue motion into the second sphere
        self.play(UpdateFromAlphaFunc(dot, lambda m, a: m.move_to(path2(a))), run_time=3)


        # Flash to indicate re-entry to first sphere (back through identified boundary)
        flash2 = Circle(radius=0.3, color=YELLOW).move_to([2, 0, 2])
        self.play(ShowPassingFlash(flash2, time_width=0.5, run_time=0.5))

        flash2 = Circle(radius=0.3, color=YELLOW).move_to([-2, 0, -2])
        self.play(ShowPassingFlash(flash2, time_width=0.5, run_time=0.5))
        # Return back to first sphere
        dot.move_to([-2, 0, 2])
        self.play(UpdateFromAlphaFunc(dot, lambda m, a: m.move_to(path1(a)+[0,0,-2])), run_time=1.5)
        self.wait(2)

class SU23(Scene):
    def construct(self):
        gauge_group = Tex(
            r"SU$(3)$", r"$\times$", r"SU$(2)$", r"$\times$", r"U$(1)$"
        )

        self.play(Write(gauge_group))
        self.wait(0.5)

        # Extract SU(2)_L part
        su2_part = gauge_group[2]

        # Create an underline just below SU(2)_L
        underline = Line(
            start=su2_part.get_bottom() + DOWN * 0.1+LEFT*su2_part.width/2,
            end=su2_part.get_bottom() + DOWN * 0.1 + RIGHT * su2_part.width/2,
            color=YELLOW,
            stroke_width=6
        )

        # Animate the underline and highlight the text
        self.play(Create(underline))
        self.play(su2_part.animate.set_color(YELLOW))
        self.wait(1)

        # Fade everything out
        self.play(FadeOut(gauge_group), FadeOut(underline))

class SM(Scene):
    def construct(self):
        text1 = Tex(r"SU$(3)$", r"$\times$", r"SU$(2)$", r"$\times$", r"U$(1)$",font_size=80)
        self.play(Write(text1))
        text2 = Tex(r"Order: $\infty$",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(text2,text3,tick,text4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=2)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))

class SM2(Scene):
    def construct(self):
        formula = MathTex(r"Q = T_3 + \frac{Y}{2}", font_size=80)
        formula.move_to(ORIGIN)
        self.play(Write(formula))
        self.wait(0.5)
        text1 = Text("Hypercharge",font_size=32).move_to(UP*2.5+RIGHT*3.5)
        arrow = CurvedArrow(text1.get_bottom(),formula.get_top()+RIGHT*2.5,angle=-90*DEGREES)
        self.play(Write(text1),Create(arrow))
        self.wait(2)

class E8(Scene):
    def construct(self):
        text1 = MathTex(r"E_8",font_size=80)
        self.play(Write(text1))
        text2 = Tex(r"Order: $\infty$",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✓", color=YELLOW, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(text2,text3,tick,text4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=2)
        self.wait(0.5)
        self.play(FadeOut(*self.mobjects),run_time=0.5)
        text5 = Tex("248 dimensional",font_size=32).move_to(RIGHT*4+UP*1)
        self.play(Write(text5))
        self.wait(1.5)
        
        g2_label = Tex("$G_2$").move_to(LEFT*2+DOWN*2)
        f4_label = Tex("$F_4$").move_to(LEFT+DOWN*2)
        e6_label = Tex("$E_6$").move_to(DOWN*2)
        e7_label = Tex("$E_7$").move_to(RIGHT+DOWN*2)
        e8_label = Tex("$E_8$").move_to(RIGHT*2+DOWN*2)
        group1 = VGroup(g2_label,f4_label,e6_label,e7_label,e8_label)
        text6 = Tex("Exceptional simple lie groups",font_size=24).next_to(group1,DOWN,buff=0.5)
        
        e8_circle = Circle(radius=0.5, color=YELLOW)
        e8_circle.move_to(e8_label.get_center())
        
        self.play(Write(group1),Write(text6),run_time=0.5)
        self.play(Create(e8_circle),run_time=0.5)
        self.wait(2)

class E82(Scene):
    def construct(self):
        # Load the images you want to use (provide the correct filenames and paths)
        img1 = ImageMobject("1.png-1.png").scale(0.3)
        img2 = ImageMobject("2.png-1.png").scale(0.3)
        img3 = ImageMobject("3.png-1.png").scale(0.3)
        img4 = ImageMobject("4.png-1.png").scale(0.3)
        img5 = ImageMobject("5.png-1.png").scale(0.3)

        # Set initial positions for the images (off-screen)
        img1.move_to(RIGHT*9)
        img2.move_to(RIGHT*9)
        img3.move_to(RIGHT*9)
        img4.move_to(RIGHT*9)
        img5.move_to(RIGHT*9)
        
        self.play(
            img1.animate.move_to(ORIGIN + LEFT * 4),
            run_time=1,
            rate_func=smooth
        )
        self.play(
            img2.animate.move_to(ORIGIN + LEFT * 2),
            run_time=1,
            rate_func=smooth
        )
        self.play(
            img3.animate.move_to(ORIGIN),
            run_time=1,
            rate_func=smooth
        )
        self.play(
            img4.animate.move_to(ORIGIN + RIGHT * 2),
            run_time=1,
            rate_func=smooth
        )
        self.play(
            img5.animate.move_to(ORIGIN + RIGHT * 4),
            run_time=1,
            rate_func=smooth
        )

        self.wait(6)
        self.clear()
        text1 = Tex("• Densest sphere packing in 8 dimensions",font_size=28).move_to(UP*2+LEFT)

        # Images related to each fact
        img1 = ImageMobject("399px-close_packings.png").scale(0.1)  # Adjust image path and scale

        # Position images next to each fact
        img1.next_to(text1, RIGHT, buff=1)
        self.play(Write(text1))
        self.play(
            img1.animate.scale(5) # Scale and shift the image 2 to its position
        )
        self.wait(3)
        text2 = Tex("• Used in algebraic geometry",font_size=28).shift(UP*1.2+LEFT*1.75)
        self.play((Write(text2)))
        # Optionally, you can add a "pop" effect by adjusting the scale factor
        self.wait(1)


class Monster(Scene):
    def construct(self):
        text1 = Tex(r"Monster Group",font_size=80)
        self.play(Write(text1))
        text2 = Tex(r"Order $\approx8\times10^{53}$",font_size=30).move_to(LEFT*3.5+DOWN*2)
        text3 = Tex(r"Abelian:",font_size=30).move_to(DOWN*2)
        text4 = Tex(r"Simple:",font_size=30).move_to(DOWN*2+RIGHT*3.5)
        tick = Text("✗", color=RED, font_size=60).next_to(text3,RIGHT)
        cross = Text("✓", color=YELLOW, font_size=60).next_to(text4,RIGHT)
        group1 = VGroup(text2,text3,tick,text4,cross)
        # tick = Text("✓", color=YELLOW, font_size=60).next_to(text3,RIGHT)
        # cross = Text("✗", color=RED, font_size=60).next_to(text4,RIGHT)
        self.play(Write(group1),run_time=1.5)
        self.wait(1)
        self.play(FadeOut(*self.mobjects),run_time=0.5)

class Monster2(Scene):
    def construct(self):
        text1 = MathTex(r"|\mathbb{M}| = 8080174247945128758864599049")
        text2 = MathTex(r"61710757005754368000000000").next_to(text1,DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
class Monster3(Scene):
    def construct(self):
        text1 = MathTex(r"\text{Aut}(V^\natural) = \mathbb{M}")
        text2 = MathTex(r"\text{Tr}_{V^\natural}(q^{L_0 - 1}) = j(q) - 744")
        self.play(Write(text1))
        self.play(text1.animate.move_to(UP*2))
        self.play(Write(text2))
        self.wait(2)