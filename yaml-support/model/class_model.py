from .base_model import BaseModel
from typing import List, Any

class ClassModel(BaseModel):
    """
    Stores data related to a python class
    """
    def __init__(self,name:str, bases:List[Any]) -> None:
        self.__name: str = name
        self.__members: List[Any] = list()
        self.__methods: List[Any] = list()
        self.__bases: List[Any] = bases


    
    @property
    def name(self): 
        return self.__name

    @property
    def members(self): 
        return self.__members

    @property
    def methods(self): 
        return self.__methods

    @property
    def bases(self): 
        return self.__bases