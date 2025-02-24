from .base import Param

class StaticParam(Param):
    def __init__(self, name: str, value):
        super().__init__(name)
        self.value = value

    def generate(self):
        return self.value