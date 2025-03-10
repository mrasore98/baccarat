# Simulator

`baccarat.simulator.Simulator`

## Overview

The `Simulator` class is the core of the Baccarat framework. It provides the foundation for implementing Monte Carlo simulations with vectorized operations via NumPy.

## Class Definition

```python
class Simulator(ABC):
    def __init__(self, num_samples: int):
        """
        Initialize a simulator for Monte Carlo simulations.
        
        Args:
            num_samples: Number of simulation samples to generate
        """
```

## Methods

### `simulation`

```python
@abstractmethod
def simulation(self):
    """
    Logic for a single simulation.
    
    This method must be implemented by subclasses and contains the core simulation logic.
    The method should return a NumPy array of results.
    
    Returns:
        np.ndarray: Array of simulation results
    """
```

### `compile_results`

```python
def compile_results(self) -> Any:
    """
    Compile the results of the simulations.
    
    Post-processing of the results after all simulations have been completed.
    By default, this method simply returns the results array.
    
    Returns:
        Any: Processed simulation results
    """
```

### `run`

```python
def run(self):
    """
    Main entry point to execute the simulation.
    
    Runs the simulation and compiles the results.
    
    Returns:
        Any: The compiled simulation results
    """
```

## Properties

- `num_samples`: Number of simulation samples
- `results`: NumPy array storing simulation results
- `rng`: NumPy random number generator

## Usage

To create a custom simulation, subclass `Simulator` and implement the `simulation` method:

```python
import numpy as np
from baccarat import Simulator, UniformParam

class PiEstimator(Simulator):
    x = UniformParam(-1.0, 1.0)
    y = UniformParam(-1.0, 1.0)
    
    def simulation(self):
        # Get random points in a square
        x = self.x
        y = self.y
        
        # Check if points are inside the unit circle
        inside_circle = x**2 + y**2 <= 1.0
        
        # Return array of boolean values (inside circle = True)
        return inside_circle
    
    def compile_results(self):
        # Calculate pi estimation: (points inside circle / total points) * 4
        return 4.0 * np.mean(self.results)

# Create and run simulation
simulator = PiEstimator(num_samples=1000000)
pi_estimate = simulator.run()
print(f"Pi estimate: {pi_estimate}")
```