from abc import ABC, abstractmethod
from typing import Any  

class Param(ABC):
        
    def __get__(self, instance, owner):
        # Generate a new value each time the parameter is accessed
        return self.generate()

    @abstractmethod
    def generate(self) -> Any:
        raise NotImplementedError("Subclasses must implement generate method")