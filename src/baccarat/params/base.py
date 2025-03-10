from abc import ABC, abstractmethod
import numpy as np

class Param(ABC):
        
    def __get__(self, instance, owner):
        # Generate a new value each time the parameter is accessed
        return self.generate(rng=instance.rng, num_generated=instance.num_samples)

    @abstractmethod
    def generate(self, rng: np.random.Generator, num_generated: int) -> np.ndarray:
        raise NotImplementedError("Subclasses must implement generate method")