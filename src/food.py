class Food:
    _pos = None
    _alive = False

    def __init__(self, position: list):
        self._pos = position
        self._alive = True

    def __del__(self):
        pass

    def get_pos(self):
        return self._pos

    def kill(self):
        self._alive = False
        self.__del__()
