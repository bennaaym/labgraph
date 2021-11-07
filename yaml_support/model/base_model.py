from abc import ABCMeta, abstractmethod



class BaseModel(metaclass=ABCMeta):
    """
    An abstraction for models. A model is a class that store data  related to a python object
    """
    
    @abstractmethod
    def save(self):
        pass