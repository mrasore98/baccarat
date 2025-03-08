# Parameters

`baccarat.params`

## Overview

The `params` module provides parameter descriptor classes for use with the `Simulator` class. These parameters automatically generate random values according to specific distributions when accessed within a simulation.

## Base Class

All parameter types inherit from the [`Param`](base.md) abstract base class, which defines the common interface.

## Parameter Types

| Class | Description |
|-------|-------------|
| [`GaussianParam`](gaussian.md) | Generates random values from a Gaussian (normal) distribution |
| [`UniformParam`](uniform.md) | Generates random values from a uniform distribution |
| [`StaticParam`](static.md) | Provides a fixed, constant value |

## Usage

Parameters are defined as class variables in a `Simulator` subclass:

```python
from baccarat import Simulator, GaussianParam, UniformParam, StaticParam

class MySimulator(Simulator):
    # Parameters are defined as class variables
    x = UniformParam(0.0, 10.0)
    y = GaussianParam(mean=5.0, std=2.0)
    z = StaticParam(3.14159)
    
    def simulation(self):
        # Access parameters to get arrays of random values
        x_values = self.x  # Array of uniform random values
        y_values = self.y  # Array of gaussian random values
        z_values = self.z  # Array filled with the constant value
        
        # Perform calculations with these arrays
        result = x_values * y_values + z_values
        return result
```

The parameters use Python's descriptor protocol to generate new random values each time they are accessed.