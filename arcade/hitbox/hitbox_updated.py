from math import radians, cos, sin, pi
from pyglet.math import Vec2, Vec3, Mat3

class HitBox:

    def __init__(self) -> None:
        self._position: Vec2 = Vec2()
        self._angle: float = 0.0
        self._size: Vec2 = Vec2()

    def get_model_matrix(self) -> Mat3:
        """
        | s_x  0   0 |   |  cos(t) sin(t) 0 |   | 1  0  p_x |
        |  0  s_y  0 | @ | -sin(t) cos(t) 0 | @ | 0  1  p_y |
        |  0   0   1 |   |    0      0    1 |   | 0  0   1  |
        """
        t = radians(self._angle)
        c, s = cos(t), sin(t)
        s_x, s_y = self._size
        p_x, p_y = self._position
        return Mat3((
             s_x * c, s_x * s, 0.0,
            s_y * -s, s_y * c, 0.0,
                 p_x,     p_y, 1.0,
        ))

    def get_inverse_matrix(self) -> Mat3:
        raise NotImplementedError("requires the next version of pyglet")
        # return ~self.get_model_matrix()
