from typing import Any, Dict, List
from loader.yaml_file_loader import YamlFileLoader
from loader.base_loader import BaseLoader
from typing import Dict, Any

def edge_list_generator(yaml_file:str, labels_only = False) -> List[Any]:
    """
    Takes a YAML representation of a LabGraph graph and generate an edge list representation of it

    Args:
        yaml_file : the path of .yaml file that contain the Graph representation
    """

    loader:BaseLoader = YamlFileLoader()
    lg_units:Dict[str,Any] = loader.load_from_file(yaml_file)
    edge_list:List[Any] = []

    for key in lg_units:
        if lg_units[key]["type"] in ("Group","Graph"):
            if labels_only : 
                edge_list = [*edge_list,*[(k,v) for k,v in lg_units[key]["connections"].items()]]  

            else:
                edge_list = [*edge_list,*[(\
                        {k:lg_units[k]} if k in lg_units else k,\
                        {k:lg_units[v]})if v in lg_units else v\
                        for k,v in lg_units[key]["connections"].items()]]   
                 
                  
    return edge_list