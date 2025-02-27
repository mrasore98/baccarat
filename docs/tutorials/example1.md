# Tutorial 1 - Approximating Pi

## Introduction

This tutorial will guide you through the process of approximating the value of pi using a Monte Carlo simulation with the help of the `baccarat` library.

The approximation we use is based on the ratio of the area of a circle to the area of a square that circumscribes it. 
If we generate random points within the square and count how many fall inside the circle, we can estimate the ratio of the areas and thus the value of pi!


## Step 1: Create a Simulator

To begin, import the `Simulator` class from the `baccarat` module.

```python
from baccarat import Simulator
```

The `Simulator` class is an abstract base class that provides the logic for running your Monte Carlo simulation. There are three primary methods that you need to know,
but only one is an abstract method that you need to implement in your own simulator. 

The important methods are:

- `simulation` (abstract)
- `compile_results`
- `run`

More details about these methods will follow as we complete the tutorial.

## Step 3: Implement the Simulator

Since `Simulator` is an abstract base class, you need to create a subclass that inherits from `Simulator` where you will provide the implementation
for the abstract method `simulation`. Let's call this class `PiSimulator`. When defining the class, we'll also define the parameters used in the simulation.

To define the parameters, we'll add class attributes that are concrete instances of the the `Param` class. 
These concrete instances are actually decorators that also define a custom `generate` method. 
Accessing a parameter attribute on `PiSimulator` will return the value of that parameter's `generate` method. 
Since this will typically be a random value, it is recommended to *assign values at the beginning of the `simulation` method*.

```python
from baccarat import Simulator

class PiSimulator(Simulator):
    radius = 1  # Not a parameter
    x = UniformParam(-radius, radius)
    y = UniformParam(-radius, radius)
    # This is a parameter, but could also be a constant value
    r = StaticParam(radius)
    
    def simulation(self):
        """This is where we implement the logic for a single iteration of the simulation."""
        # Get values from the parameters of the simulator
        x, y, r = self.x, self.y, self.r
        # Check if point falls inside the circle
        return x**2 + y**2 <= r**2

```

The return value of the `simulation` method is appended to a list: `PiSimulator.results`. By default, this list is returned when the simulation completes,
at the end of the `run` method.

## Step 4: Implementing the `compile_results` Method

Returning a list of results is all well and good, but if we're using the simulation to approximate pi, it seems like this would fall short of our goal 
and leave us with more work to do! Luckily, we can specify a custom implementation of the `compile_results` method to do some postprocessing to modify 
the return value appropriately.

```python
from baccarat import Simulator, UniformParam, StaticParam

class PiSimulator(Simulator):
    radius = 1  # Not a parameter
    x = UniformParam(-radius, radius)
    y = UniformParam(-radius, radius)
    # This is a parameter, but could also be a constant value
    r = StaticParam(radius)
    
    def simulation(self):
        """This is where we implement the logic for a single iteration of the simulation."""
        # Get values from the parameters of the simulator
        x, y, r = self.x, self.y, self.r
        # Check if point falls inside the circle
        return x**2 + y**2 <= r**2
    
    def compile_results(self):
        """Do work on the collection of simulation results to compute the approximation of pi."""
            # Apply the formula to compare the number of points inside the circle to the total number of points 
            # and return the approximation of pi
            # Pi = 4 * A_circle / A_square
            return 4 * len([res for res in self.results if res]) / len(self.results)

if __name__ == "__main__":
    num_sims = 1_000_000
    simulator = PiSimulator(num_sims)
    result = simulator.run()  # Will now return an approximation of pi!
    print(result)
```

## Conclusion

In a handful of lines of code, we have a complete implementation of a Monte Carlo simulation to approximate the value of pi!
The `baccarat` interface allowed us to separate the concerns of simulation logic and postprocessing and build our simulation incrementally.
