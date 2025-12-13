from manim import *

class Alter(Scene):
    def construct(self):
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
        text6 = Tex("Even Permutations of 5 elements",font_size=24).move_to(DOWN*1.5)
        text7 = MathTex("n = 5",font_size=24).next_to(text5,DOWN,buff=0.75)
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
        group_node = Circle(color=BLUE, radius=0.6).add(MathTex(r"A_n", font_size=30))
        group_node.move_to(UP*1.5)

        # Trivial groups under each
        trivial_node = Circle(color=GRAY, radius=0.4).add(MathTex("\\{e\\}", font_size=24))
        trivial_node.next_to(group_node, DOWN, buff=1.5)

        # Arrows between them
        arrow = Arrow(start=trivial_node.get_top(), end=group_node.get_bottom(), buff=0.1, color=YELLOW)
        text1=Tex(r"for $n\ge5$",font_size=20).next_to(group_node,UP,buff=0.5)
        # Display nodes
        self.play(LaggedStart(Create(group_node), lag_ratio=0.3),Write(text1))
        self.play(LaggedStart(Create(trivial_node), lag_ratio=0.3))
        self.play(LaggedStart(GrowArrow(arrow), lag_ratio=0.3))
        self.wait(0.5)

        # Add labels
        normal_text = MathTex("\\{e\\} \\triangleleft A_n", font_size=24)
        normal_text.next_to(arrow, LEFT, buff=0.1)
        self.play(LaggedStart(Write(normal_text), lag_ratio=0.2))
        group2 = VGroup(text1,group_node,trivial_node,arrow,normal_text)
        image1 = ImageMobject("vid1-thumbnail.png").set(height=2).move_to(DOWN*1.5)
        self.play(group2.animate.scale(0.75).shift(UP*1.5),FadeIn(image1))
        text8 = Tex("Galois Theory",font_size=24).next_to(image1,DOWN)
        self.play(Write(text8))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
import random
class Alter2(Scene):
    def construct(self):
        title = Tex(r"\bf Geometry",color=BLACK)
        circle = Circle(radius=2, color=BLUE_B, fill_color=BLUE, fill_opacity=0.6).set_stroke(width=0)
        square = Square(side_length=2.5, color=PURPLE_B, fill_color=BLUE, fill_opacity=0.6).set_stroke(width=0)
        triangle = RegularPolygon(3, color=YELLOW_B, fill_color=BLUE, fill_opacity=0.6).set_stroke(width=0)
        circle_rot = circle.copy().set_color(TEAL_A)
        square_rot = square.copy().set_color(GREEN_A)
        triangle_rot = triangle.copy().set_color(ORANGE)

        shapes = VGroup(circle_rot, square_rot, triangle_rot)
        dots = VGroup(*[Dot(radius=0.1, color=random.choice([RED, GOLD, PINK])) for _ in range(10)])
        for i, dot in enumerate(dots):
            dot.move_to(2.2 * RIGHT).rotate(i * TAU / 10, about_point=ORIGIN)
        self.add(dots,shapes)
        self.play(
            Rotate(shapes, angle=PI*0.25, about_point=ORIGIN, run_time=1, rate_func=linear),
            Rotate(dots, angle=PI*0.25, about_point=ORIGIN, run_time=1, rate_func=linear),
        )
        self.play(
            Rotate(shapes, angle=PI*0.75, about_point=ORIGIN, run_time=3, rate_func=linear),
            Rotate(dots, angle=PI*0.75, about_point=ORIGIN, run_time=3, rate_func=linear),
            Write(title,run_time=3)
        )
        self.play(
            Rotate(shapes, angle=PI*0.5, about_point=ORIGIN, run_time=2, rate_func=linear),
            Rotate(dots, angle=PI*0.5, about_point=ORIGIN, run_time=2, rate_func=linear),
        )
        self.play(FadeOut(*self.mobjects))
        text1 = MathTex("A_n").move_to(UP*2)
        self.play(Write(text1))
        image1 = ImageMobject("graph.png").set(height=2)
        self.play(FadeIn(image1),run_time=2)
        text2 = Tex("drawn in 2D as complete graphs",font_size=20).next_to(image1,DOWN)
        self.play(Write(text2))
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        image2 = ImageMobject("bitmap.png").set(height=4).move_to(LEFT)

        # Animate each
        self.play(FadeIn(image2), run_time=1)
        text3 = Tex("Linear Programming",font_size=20).next_to(image2,DOWN).shift(RIGHT)
        self.play(Write(text3))
        text4 = Tex(r"Triangle in 2D",font_size=15).move_to(DOWN*1.2+RIGHT*1)
        arrow = CurvedArrow(text4.get_left(), image2.get_center()+RIGHT*0.5+UP*0.5, angle=-90*DEGREES, stroke_width=1.5, tip_length=0.15 )
        self.play(Create(arrow))
        self.play(Write(text4))
        self.wait(3)


class Alter3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES,zoom=2.75)
        text1 = Tex("Smallest n dimensional shape",font_size=24).move_to(UP*3.2)
        self.add_fixed_in_frame_mobjects(text1)
        self.play(Write(text1))
        line = Line(LEFT, RIGHT)
        self.add_fixed_in_frame_mobjects(line)
        line.set_color(BLUE)
        line.set_stroke(width=5)
        self.play(Create(line))
        self.play(line.animate.shift(UP*2))
        triangle = Triangle(
            color=BLUE
        ).scale(0.75)
        triangle.set_fill(BLUE, opacity=0.5).scale(1.5)
        self.add_fixed_in_frame_mobjects(triangle)
        self.play(Create(triangle))
        vertices = triangle.get_vertices()
        centroid = np.mean(vertices, axis=0)
        self.play(Rotate(triangle,2*PI/3,about_point=centroid))
        self.wait(2)
        tetra = Tetrahedron().move_to(RIGHT).scale(0.8)
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
        text1 = Tex("3D projection of the 4-simplex",font_size=20).move_to(DOWN*2)
        self.add_fixed_in_frame_mobjects(text1)
        self.play(UpdateFromAlphaFunc(simplex, update_simplex),Write(text1), run_time=4, rate_func=linear,)
        
        self.wait()



# Set up the camera to render in 9:16 aspect ratio (for 1080x1920)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 8.0  # Adjust height of the scene for a vertical aspect ratio
config.frame_width = 4.5   # Adjust width to maintain 9:16 ratio


