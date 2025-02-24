import multiprocessing
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Iterable

from .params import SimulationParams, Param


class Simulator(ABC):
    def __init__(self, num_samples: int, params: SimulationParams | Iterable[Param] | None = None, max_workers: int | None = None):
        self.num_samples = num_samples
        self.params = params if isinstance(params, SimulationParams) else SimulationParams(params)
        self.max_workers = max_workers or multiprocessing.cpu_count()  # Assume simulation is CPU-bound
        self.results: list[Any] = []
        
    def __getattr__(self, name: str) -> Any:
        # Delegate parameter access to SimulationParams
        if hasattr(self.params, name):
            return getattr(self.params, name)
        raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")
    
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
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            self.results = list(executor.map(self._simulation_wrapper, range(self.num_samples)))
        return self.compile_results()
        
    def _simulation_wrapper(self, _):
        """Helper for a compatible interface with mapping in the ThreadPoolExecutor of `run`."""
        return self.simulation()
    
    