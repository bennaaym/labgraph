from .base_loader import BaseLoader
from .error import YamlFileLoaderError
from typing import Dict,Any
import yaml
import os


class YamlFileLoader(BaseLoader):

    def load_from_file(self,path:str) -> Dict[str,Any]:

        """
        Returns a dict from .yaml file

        Args:
            file_path: The path of .yaml file 
        """

        if not os.path.exists(path):
            raise YamlFileLoaderError(f"{path} file not found")

        if not os.path.isfile(path) or not path.endswith('.yaml'):
            raise YamlFileLoaderError(f"{path} should be a .yaml file")

        
        with open(path, 'r') as file:
            _dict = yaml.load(file, Loader=yaml.SafeLoader)
            return _dict
