# create singleton
"""
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
"""


class Curve:
    _pos = None
    _snake_length_left = None
    _prev_mov_direction = None
    _prev_mov_k = None

    def __init__(self, snake_length: int, position: list, _prev_mov_direction: int, prev_mov_k: int):
        self._snake_length_left = snake_length
        self._pos = position
        self._prev_mov_direction = _prev_mov_direction
        self._prev_mov_k = prev_mov_k

    def __del__(self):
        pass

    def kill(self):
        self.__del__()

    def get_pos(self):
        return self._pos

    def get_tail_pos(self):
        tmp_pos = self._pos.copy()
        tmp_pos[self._prev_mov_direction] -= self._prev_mov_k*self._snake_length_left
        return tmp_pos

    def tic(self):
        self._snake_length_left -= 1
        if self._snake_length_left <= 0:
            self.kill()


class Snake:  # (metaclass=Singleton):
    _pos = None
    _length = None
    _curves = list()
    _dimension = 0
    _alive = False
    _mov_direction = 0
    _mov_k = 1

    def __init__(self, position: list, length: int = 3):
        self._length = length
        self._pos = position
        self._dimension = len(position)
        self._alive = True

    def __del__(self):
        pass

    def kill(self):
        self._alive = False
        self.__del__()

    def add_curve(self, position: list, _prev_mov_direction: int, prev_mov_k: int):
        self._curves.append(Curve(self._length, position.copy(), _prev_mov_direction, prev_mov_k))

    def _sneak(self):
        self._pos[self._mov_direction] += self._mov_k

    def feed(self):
        self._length += 1

    def tic(self):
        self._sneak()
        for curve in self._curves:
            curve.tic()

    def get_lines(self):
        lines = list()
        tmp_pos = self._pos
        for curve in self._curves:
            lines.append([tmp_pos, curve.get_pos()])
            tmp_pos = curve.get_pos()
        if len(self._curves) > 0:
            lines.append([tmp_pos, self._curves[-1].get_tail_pos()])
        else:
            tail_pos = tmp_pos.copy()
            tail_pos[self._mov_direction] -= self._mov_k * self._length
            lines.append([tail_pos, tmp_pos])
        return lines

    def get_pos(self):
        return self._pos

    def get_direction(self):
        if self._mov_direction == 0:
            return 10 * self._mov_k
        return self._mov_direction * 10 * self._mov_k

    def set_direction(self, coord_id: int, polarity: int):
        if coord_id > self._dimension:
            raise ValueError
        self._mov_direction = coord_id
        self._mov_k = polarity

    def rotate(self, coord_id: int, polarity: int):
        if self._mov_direction == coord_id and self._mov_k == polarity:
            return None

        self.add_curve(self._pos, self._mov_direction, self._mov_k)
        self.set_direction(coord_id, polarity)


# create singleton object
# snake = Snake()
