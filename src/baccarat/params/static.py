from .base import Param

class StaticParam(Param):
    def __init__(self, value):
        self.value = value

    def generate(self):
        return self.value