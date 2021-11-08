from pathlib import Path
from typed_ast import ast3
from _parser.base_parser import BaseParser
from _parser.labgraph_units_parser import LabGraphUnitsParser
from loader.base_loader import BaseLoader
from loader.python_file_loader import PythonFileLoader
import os



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
        
        last_back_slash_index = python_file.rfind('/')
        last_dot_index = python_file.rfind('.')

        if last_back_slash_index == -1:
            yaml_file = f"{python_file[:last_dot_index]}.yaml"
        else:
            yaml_file =  f"{python_file[last_back_slash_index:last_dot_index]}.yaml"
    

    # check if the file exists
    file = f"{Path(__file__).parent}/outputs/{yaml_file}"


    if os.path.exists(file):
        os.remove(file)

    for cls in lg_units_parser.classes:
        cls.save(yaml_file)

