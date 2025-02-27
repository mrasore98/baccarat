import random

from .base import Param

class UniformParam(Param):
    def __init__(self, low: float = 0.0, high: float = 1.0):
        self.low = low
        self.high = high

    def generate(self) -> float:
        return random.uniform(self.low, self.high)