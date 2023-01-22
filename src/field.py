import random

from src.food import Food
from src.snake import Snake

from config import conf


# create singleton
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Field(metaclass=Singleton):
    _field_dimensions = None
    _food = None
    _snake = None
    _death = True
    _game_speed = 0
    _snake_score = 0

    def __init(self, game_speed_ms: int = conf('settings', 'speed')):
        self._game_speed = game_speed_ms

    def init(self, field_dimensions: list):
        self._field_dimensions = field_dimensions

    def is_death(self):
        return self._death

    def add_score(self):
        self._snake.feed()
        self._snake_score += 1

    def get_score(self):
        return self._snake_score

    def get_dimensions(self):
        return self._field_dimensions

    def get_center(self):
        center = list()
        for i in range(len(self._field_dimensions)):
            center.append(round(self._field_dimensions[i]/2))
        return center

    def add_snake(self, pos: list = None, length: int = conf('snake', 'length')):
        if pos is None:
            pos = self.get_center()
        self._snake = Snake(pos, length)
        self._death = False
        print(f'Snake:{pos}')

    def _get_random_cords(self):
        random_dot = list()
        for coord_max in self._field_dimensions:
            random_dot.append(random.randint(0, coord_max))
        return random_dot

    @staticmethod
    def _is_dot_in_line(pos_dot, pos_line, ignore_edges: bool = False):
        # if one of pos_line coordinates is equal pos_dot, ignore it
        if ignore_edges:
            if pos_dot == pos_line[0] or pos_dot == pos_line[1]:
                return False

        cross_count = 0
        for i in range(len(pos_line)):
            if pos_line[0][i] != pos_line[1][i]:
                if pos_line[0][i] <= pos_line[1][i]:
                    if pos_line[0][i] <= pos_dot[i] <= pos_line[1][i]:
                        cross_count += 1
                else:
                    if pos_line[0][i] >= pos_dot[i] >= pos_line[1][i]:
                        cross_count += 1
        return True if cross_count == 2 else False

    def _is_dot_in_lines(self, pos_dot, pos_lines):
        for line in pos_lines:
            if self._is_dot_in_line(pos_dot, line):
                return True
        return False

    def add_food(self):
        cords = None
        while True:
            cords = self._get_random_cords()
            if not self._is_dot_in_lines(cords, self._snake.get_lines()):
                break
        self._food = Food(cords)
        print(f'Food:{cords}')

    def is_snake_field_contact(self):
        snake_pos = self._snake.get_pos()
        for i in range(len(self._field_dimensions)):
            if snake_pos[i] < 0 or snake_pos[i] > self._field_dimensions[i]:
                return True
        return False

    def is_snake_self_touch(self):
        snake_pos = self._snake.get_pos()
        snake_lines = self._snake.get_lines()
        for snake_line in snake_lines:
            if self._is_dot_in_line(snake_pos, snake_line, ignore_edges=True):
                return True
        return False

    def is_snake_food_contact(self):
        if self._snake.get_pos() == self._food.get_pos():
            return True
        else:
            return False

    def control(self, dimension_id: int, rotate: int):
        if rotate > 0:
            rotate = 1
        else:
            rotate = -1
        self._snake.rotate(dimension_id, rotate)

    def tic(self):
        # check if snake head touch border
        if self.is_snake_field_contact():
            self._death = True
        # check if snake touch itself
        if self.is_snake_self_touch():
            self._death = True
        # check if snake head touch food
        if self.is_snake_food_contact():
            self.add_score()
            self._food = None
            self.add_food()
        # tic snake
        self._snake.tic()
        print(self._snake.get_pos())


# create singleton object
field = Field()
field.init(conf('field'))
