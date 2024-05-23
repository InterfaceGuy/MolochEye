import importlib
import pydeation.imports
importlib.reload(pydeation.imports)
from pydeation.imports import *


class MolochEye(CustomObject):

    def specify_parts(self):
        self.upper_eyelid = Arc(
            start_angle=PI / 6, end_angle=5 * PI / 6, radius=200, y=-100, color=WHITE)
        self.lower_eyelid = Arc(
            start_angle=7 * PI / 6, end_angle=11 * PI / 6, radius=200, y=100, color=WHITE)
        self.iris = Circle(radius=100, color=WHITE)
        self.cube_pupil_outer = Square(creation=True, size=90, color=BLUE)
        self.cube_pupil_inner = Square(creation=True, size=60, color=BLUE)
        self.cube_pupil_line_top_right = Line(
            (self.cube_pupil_outer.size / 2, self.cube_pupil_outer.size / 2), (self.cube_pupil_inner.size / 2, self.cube_pupil_inner.size / 2), color=BLUE)
        self.cube_pupil_line_bottom_right = Line(
            (self.cube_pupil_outer.size / 2, -self.cube_pupil_outer.size / 2), (self.cube_pupil_inner.size / 2, -self.cube_pupil_inner.size / 2), color=BLUE)
        self.cube_pupil_line_top_left = Line(
            (-self.cube_pupil_outer.size / 2, self.cube_pupil_outer.size / 2), (-self.cube_pupil_inner.size / 2, self.cube_pupil_inner.size / 2), color=BLUE)
        self.cube_pupil_line_bottom_left = Line(
            (-self.cube_pupil_outer.size / 2, -self.cube_pupil_outer.size / 2), (-self.cube_pupil_inner.size / 2, -self.cube_pupil_inner.size / 2), color=BLUE)
        self.parts += [self.upper_eyelid, self.lower_eyelid,
                       self.iris, self.cube_pupil_outer, self.cube_pupil_inner, self.cube_pupil_line_top_right, self.cube_pupil_line_bottom_right, self.cube_pupil_line_top_left, self.cube_pupil_line_bottom_left]

    def specify_creation(self):
        self.inherit_creation()


if __name__ == "__main__":
    moloch_eye = MolochEye(creation=True)
