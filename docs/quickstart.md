# Quick Start Guide

## Installation

To get started with baccarat, you can install it using pip (or uv or poetry or your package manager of choice):

```bash
pip install baccarat_sim
```

## Usage

A simple example using `baccarat` to approximate pi:

```python
from baccarat import Simulator, UniformParam, StaticParam

class PiSimulator(Simulator):
    radius = 1
    # These parameters are descriptors, used to generate random values when accessed
    x = UniformParam(-radius, radius)
    y = UniformParam(-radius, radius)
    # Strictly speaking, this could be a constant, but we use a Param for consistency
    r = StaticParam(radius)  
    
    def simulation(self):
        # Use assignments since attribute access will generate the random value
        x, y, r = self.x, self.y, self.r
        # Check to see if the random point is inside the circle
        return x**2 + y**2 <= r**2
    
    def compile_results(self):
        return 4 * len([res for res in self.results if res]) / len(self.results)

approx_pi = PiSimulator(1_000_000).run()
```

Notes: 

1. All user simulations start with a class that inherits from `Simulator` and implements the `simulation` method.
    1. The `simulation` method defines the vectorized logic for the simulation. It should return a NumPy array of results.
    1. Optionally, the `compile_results` method can be implemented to process the results array once the simulation is complete.
1. Parameters are defined as class attributes.
    1. Distributions for generating random values are specified using the concrete implementations of the `Param` class, such as `UniformParam` and `GaussianParam`.
    1. When accessed, parameters return NumPy arrays containing the random values, enabling efficient vectorized operations.
    1. Custom distributions can be created by subclassing the `Param` class and implementing the `generate` method to return a NumPy array.
1. The number of samples used in the simulation are specified when creating an instance of the `Simulator` subclass.

## Examples

For more examples, see the [examples](https://github.com/mrasore98/baccarat/tree/main/examples) on GitHub.