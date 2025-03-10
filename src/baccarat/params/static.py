import numpy as np

from .base import Param

class StaticParam(Param):
    def __init__(self, value):
        self.value = value

    def generate(self, rng: np.random.Generator, num_generated: int) -> np.ndarray:
        return self.value * np.ones(num_generated)