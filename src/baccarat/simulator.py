from abc import ABC, abstractmethod
from typing import Any

import numpy as np

class Simulator(ABC):
    def __init__(self, num_samples: int):
        self.num_samples = num_samples
        self.results: np.ndarray = np.empty(num_samples)
        self.rng = np.random.default_rng()
        
    @abstractmethod
    def simulation(self):
        """Logic for a single simulation. The return value will be appended to the results list."""
        raise NotImplementedError("Subclasses must implement the simulation method")
    
    def compile_results(self) -> Any:
        """
        Compile the results of the simulations. 
        
        Post-processing of the results after all simulations have been completed.
        By default, this method simply returns the results list.
        """
        return self.results
    
    def run(self):
        """Main entry point to execute the simulation."""
        self.results = self.simulation()
        return self.compile_results()
    