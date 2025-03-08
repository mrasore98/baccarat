# Gaussian Parameter

`baccarat.params.GaussianParam`

## Overview

The `GaussianParam` class generates random values from a Gaussian (normal) distribution. It is a concrete implementation of the [`Param`](base.md) abstract base class.

## Class Definition

```python
class GaussianParam(Param):
    def __init__(self, mean: float, std: float):
        """
        Initialize a Gaussian parameter.
        
        Args:
            mean: The mean (average) of the distribution
            std: The standard deviation of the distribution
        """
        self.mean = mean
        self.std = std

    def generate(self, rng: np.random.Generator, num_generated: int) -> np.ndarray:
        """
        Generate random values from a Gaussian distribution.
        
        Args:
            rng: The NumPy random number generator to use
            num_generated: Number of values to generate
            
        Returns:
            np.ndarray: Array of random values from the Gaussian distribution
        """
        return rng.normal(self.mean, self.std, size=num_generated)
```

## Usage

```python
from baccarat import Simulator, GaussianParam

class MySimulator(Simulator):
    # Create a Gaussian parameter with mean 0 and standard deviation 1
    x = GaussianParam(mean=0.0, std=1.0)
    
    def simulation(self):
        # Access the parameter to get an array of gaussian random values
        values = self.x
        
        # Perform calculations with these values
        return values ** 2
```