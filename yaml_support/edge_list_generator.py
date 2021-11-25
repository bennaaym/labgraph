import os
from typing import Any, Dict, List
from yaml_support.loader.yaml_file_loader import YamlFileLoader
from yaml_support.loader.base_loader import BaseLoader
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
                        {v:lg_units[v]})if v in lg_units else v\
                        for k,v in lg_units[key]["connections"].items()]]  


    # substitute message, config, and status class
    if not labels_only:
        for edge_1,_ in edge_list:

            for key,value in edge_1.items():
                for _key, _value in value.items():
                    if _key in ('state','config'):
                        edge_1[key][_key] = {_value:lg_units[_value]["fields"]}

                    if _key == 'inputs':
                        inputs:List[Dict[str,Any]] = []
                        for _input in _value:
                            inputs.append({_input:lg_units[_input]["fields"]})

                        edge_1[key][_key] = inputs


                    if _key == 'outputs':
                        outputs:List[Dict[str,Any]] = []
                        for _output in _value:
                            outputs.append({_output:lg_units[_output]["fields"]})

                        edge_1[key][_key] = outputs


   


           
                    

                 
                  
    return edge_list