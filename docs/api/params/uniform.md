# Uniform Parameter

`baccarat.params.UniformParam`

## Overview

The `UniformParam` class generates random values from a uniform distribution. It is a concrete implementation of the [`Param`](base.md) abstract base class.

## Class Definition

```python
class UniformParam(Param):
    def __init__(self, low: float = 0.0, high: float = 1.0):
        """
        Initialize a uniform parameter.
        
        Args:
            low: Lower bound of the distribution (inclusive)
            high: Upper bound of the distribution (exclusive)
        """
        self.low = low
        self.high = high

    def generate(self, rng: np.random.Generator, num_generated: int) -> np.ndarray:
        """
        Generate random values from a uniform distribution.
        
        Args:
            rng: The NumPy random number generator to use
            num_generated: Number of values to generate
            
        Returns:
            np.ndarray: Array of random values from the uniform distribution
        """
        return rng.uniform(self.low, self.high, size=num_generated)
```

## Usage

```python
from baccarat import Simulator, UniformParam

class DiceRollSimulator(Simulator):
    # Create a uniform parameter for dice rolls (1-6)
    # Note: We use 0.5 to 6.5 to get a uniform distribution over integers 1-6
    roll = UniformParam(low=0.5, high=6.5)
    
    def simulation(self):
        # Get array of random dice rolls
        rolls = self.roll
        
        # Convert to integers (1-6)
        return np.floor(rolls).astype(int)
```