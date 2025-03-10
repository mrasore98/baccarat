import numpy as np

from .base import Param

class GaussianParam(Param):
    def __init__(self, mean: float, std: float):
        # super().__init__(name)
        self.mean = mean
        self.std = std

    def generate(self, rng: np.random.Generator, num_generated: int) -> np.ndarray:
        return rng.normal(self.mean, self.std, size=num_generated)