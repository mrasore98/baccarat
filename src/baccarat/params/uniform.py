import numpy as np

from .base import Param

class UniformParam(Param):
    def __init__(self, low: float = 0.0, high: float = 1.0):
        self.low = low
        self.high = high

    def generate(self, rng: np.random.Generator, num_generated: int) -> np.ndarray:
        return rng.uniform(self.low, self.high, size=num_generated)