from .base_model import BaseModel
from typing import List, Any

class ClassModel(BaseModel):
    """
    Stores data related to a python class
    """
    def __init__(self,name:str, base: str) -> None:
        self.__name: str = name
        self.__members: List[Any] = list()
        self.__methods: List[Any] = list()
        self.__base: str = base


    
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
    def base(self): 
        return self.__base