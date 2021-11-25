from pathlib import Path
from typed_ast import ast3
from yaml_support._parser.base_parser import BaseParser
from yaml_support._parser.labgraph_units_parser import LabGraphUnitsParser
from yaml_support.loader.base_loader import BaseLoader
from yaml_support.loader.python_file_loader import PythonFileLoader
import os
import ntpath



def yamlify(python_file:str,yaml_file:str = ""):
    """
    Takes .py file and parse it to .yaml file 
    
    Args:
        python_file : The .py file path
        yml_file: The name of the YAML file to be created, 
                  in case nothing is passed the output file will have the same name as the input file
    """

    loader:BaseLoader = PythonFileLoader()
    lg_units_parser:BaseParser = LabGraphUnitsParser()

    code_string = loader.load_from_file(python_file)
    ast = ast3.parse(code_string)
    lg_units_parser.parse(ast)


    if not yaml_file:
        yaml_file = f"{ntpath.basename(python_file)}"


    # check if the file exists
    file = f'{os.path.abspath(f"yaml_outputs/{yaml_file}")[:-3]}.yaml'

    if os.path.exists(file):
        os.remove(file)

    for cls in lg_units_parser.classes:
        cls.save(file)


    return file
