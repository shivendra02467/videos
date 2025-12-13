from manim import *

text = MathTex(r"\textbf{Duicer}",color=WHITE)

class Hyperboloid(ThreeDScene):
    def construct(self):

        a = np.sqrt(2)
        c =1.4

        def hyperboloid(u, v):
            # u in [0, 2pi]
            # v in [-v_max, v_max], controls height/stretch
            x = a * np.cosh(v) * np.cos(u)
            y = a * np.cosh(v) * np.sin(u)
            z = c * np.sinh(v)
            return np.array([x, y, z])

        surface = Surface(
            hyperboloid,
            u_range=[0, TAU],
            v_range=[-10, 1],  # adjust for height/depth
            resolution=(30, 60),
            fill_opacity=1.0,
            stroke_color="#ffde59",
            stroke_width=2,
            checkerboard_colors=["#000000", "#000000"],
        )

        self.set_camera_orientation(phi=60 * DEGREES, theta=0 * DEGREES)
        self.camera.set_zoom(0.5)
        self.add(surface)
