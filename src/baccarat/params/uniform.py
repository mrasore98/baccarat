import random

from .base import Param

class UniformParam(Param):
    def __init__(self, name: str, low: float, high: float):
        super().__init__(name)
        self.low = low
        self.high = high

    def generate(self) -> float:
        return random.uniform(self.low, self.high)