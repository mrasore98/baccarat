# Base Parameter

`baccarat.params.Param`

## Overview

The `Param` class is an abstract base class that defines the interface for all parameter types. It implements Python's descriptor protocol to automatically generate new random values when accessed within a `Simulator` instance.

## Class Definition

```python
class Param(ABC):
    def __get__(self, instance, owner):
        # Generate a new value each time the parameter is accessed
        return self.generate(rng=instance.rng, num_generated=instance.num_samples)

    @abstractmethod
    def generate(self, rng: np.random.Generator, num_generated: int) -> np.ndarray:
        """
        Generate random values using the given random number generator.
        
        Args:
            rng: The NumPy random number generator to use
            num_generated: Number of values to generate
            
        Returns:
            np.ndarray: Array of generated values
        """
```

## Descriptor Protocol

The `Param` class uses Python's descriptor protocol to provide dynamic behavior when parameters are accessed as instance attributes in a `Simulator` subclass:

1. When a parameter is accessed (e.g., `self.x` in a `Simulator` subclass), Python calls the `__get__` method
2. The `__get__` method calls the `generate` method with the simulator's random number generator and sample count
3. The `generate` method returns an array of random values according to the parameter's specific distribution

## Custom Parameter Types

To create a custom parameter type, subclass `Param` and implement the `generate` method:

```python
import numpy as np
from baccarat.params import Param

class ExponentialParam(Param):
    def __init__(self, scale=1.0):
        self.scale = scale
        
    def generate(self, rng: np.random.Generator, num_generated: int) -> np.ndarray:
        return rng.exponential(scale=self.scale, size=num_generated)
```