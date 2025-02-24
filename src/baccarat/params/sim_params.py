from collections.abc import Iterable

from .base import Param


# TODO: figure out how to use the descriptor to make class creation more ergonomic
# class ParamDescriptor:
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         # Access the actual Param object from instance.__dict__
#         param = instance.__dict__.get(self.name)
#         if isinstance(param, Param):
#             return param.generate()
#         return None
        
#     # def __set__(self, instance, value):
#     #     instance.__dict__[self.name] = value
        
#     def __set_name__(self, owner, name):
#         self.name = name

class SimulationParams:
    def __init__(self, params: Iterable[Param] | None = None):
        self._params = {}
        if params is not None:
            self._params.update({param.name: param for param in params if isinstance(param, Param)})
    
    def __getattr__(self, name):
        if name in self._params:
            return self._params[name].generate()
            
    def add_param(self, param: Param):
        self._params[param.name] = param