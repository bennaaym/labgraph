from .base_model import BaseModel
from typing import List, Dict, Any
from serializer.yaml_serializer import YamlSerializer
import os

class ClassModel(BaseModel):
    """
    Stores data related to a python class
    """
    def __init__(self,name:str, base: str) -> None:
        self.__name: str = name
        self.__members: Dict[str,str] = {}
        self.__methods: Dict[str,Dict[Any]] = {}
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


    def save(self,file):
        """
        serialize the current class model and save it as YAML file
        """

        if self.base in ("Message","Config","State"):
            self.__save_message(file)

        elif  self.base in ("Node","Group","Graph"):
            self.__save_module(file)


    
    def __save_message(self,file):
        YamlSerializer.serialize({
            f"{self.name}":
            {
                "type":self.base,
                "fields":self.members
            }
        },file)

    
    def __save_module(self,file):
      
        obj:Dict[str,Dict[Any]] = {

            f"{self.name}":{
                "type":self.base
            }
        }
        
        if "state" in self.members:
            obj[self.name]["state"] = self.members["state"]

        if "config" in self.members:
            obj[self.name]["config"] = self.members["config"]

        # inputs and outputs
        inputs = set()
        outputs = set()

        for method in self.methods:
            for subscriber in self.methods[method]["subscribers"]:
                inputs.add(self.members[subscriber])
            
            for publisher in self.methods[method]["publishers"]:
                outputs.add(self.members[publisher])

        obj[self.name]["inputs"] = list(inputs)
        obj[self.name]["outputs"] = list(outputs)

        # case of a Group/Graph
        if self.base in ("Group","Graph"):
            
            if "OUTPUT" in self.members:
                obj[self.name]["outputs"] = [self.members["OUTPUT"]]
            
            if "connections" in self.methods:
                connections:Dict[str,str] = \
                { 
                    self.members[k]:(self.members[v] if v!=self.name else v)  for\
                    k,v in self.methods["connections"]["return"]["connections_dict"].items()
                }

                obj[self.name]["connections"] = connections
            
         

        YamlSerializer.serialize(obj,file)


   
