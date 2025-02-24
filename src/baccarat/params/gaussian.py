import random

from .base import Param

class GaussianParam(Param):
    def __init__(self, name: str, mean: float, std: float):
        super().__init__(name)
        self.mean = mean
        self.std = std

    def generate(self) -> float:
        return random.gauss(self.mean, self.std)