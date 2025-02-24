from abc import ABC, abstractmethod
from typing import Any  

class Param(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def generate(self) -> Any:
        raise NotImplementedError("Subclasses must implement generate method")