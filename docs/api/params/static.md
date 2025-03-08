# Static Parameter

`baccarat.params.StaticParam`

## Overview

The `StaticParam` class provides a fixed, constant value as an array. It is a concrete implementation of the [`Param`](base.md) abstract base class.

## Class Definition

```python
class StaticParam(Param):
    def __init__(self, value):
        """
        Initialize a static parameter.
        
        Args:
            value: The fixed value to use for all elements
        """
        self.value = value

    def generate(self, rng: np.random.Generator, num_generated: int) -> np.ndarray:
        """
        Generate an array filled with the constant value.
        
        Args:
            rng: The NumPy random number generator (not used)
            num_generated: Number of elements in the array
            
        Returns:
            np.ndarray: Array filled with the constant value
        """
        return self.value * np.ones(num_generated)
```

## Usage

```python
from baccarat import Simulator, UniformParam, StaticParam

class GravitySimulator(Simulator):
    # Random initial height (0-100 meters)
    height = UniformParam(0.0, 100.0)
    
    # Constant gravitational acceleration (9.81 m/s²)
    gravity = StaticParam(9.81)
    
    def simulation(self):
        # Calculate time to hit ground: t = sqrt(2h/g)
        heights = self.height
        g = self.gravity
        
        # Return array of fall times
        return np.sqrt(2 * heights / g)
```

## Notes

- The `StaticParam` creates an array where every element has the same value
- Unlike other parameter types, it does not use the random number generator
- Useful for physical constants or other fixed values in simulations