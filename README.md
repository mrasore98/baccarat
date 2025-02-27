# `baccarat`

Monte Carlo simulation framework in Python, with a focus on ease of use and flexibility.

## Motivation

I wanted to create a framework that would allow users to easily create Monte Carlo simulations without having to worry about boilerplate or optimization.
The goal of baccarat is to provide a simple and intuitive interface for building simulations

## Getting Started

### Installation

To get started with baccarat, you can install it using pip (or uv or poetry or your package manager of choice):

```bash
pip install baccarat
```

### Usage

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
    1. The `simulation` method defines the logic for a single iteration of the simulation. The return value will be appended to a list of results on the class instance.
    1. Optionally, the `compile_results` method can be implemented to process the results of the simulation once all iterations are complete.
1. Parameters are defined as class attributes.
    1. Parameters can be either static or dynamic. Static parameters are fixed values, while dynamic parameters are generated randomly according to a distribution.
    1. Distributions are specified using the concrete implementations of the `Param` class, such as `UniformParam` and `GaussianParam`.
    1. Custom distributions can be created by subclassing the `Param` class and implementing the `generate` method.
1. The number of iterations used in the simulation are specified when creating an instance of the `Simulator` subclass.

## Examples

For more examples, see the [examples](examples) folder.

## About the name

Baccarat is a popular card game in casinos around the world. I first learned about baccarat
when reading Ian Fleming's *Casino Royale*, the first novel in the James Bond series.
