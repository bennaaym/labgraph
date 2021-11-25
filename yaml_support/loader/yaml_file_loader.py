from pathlib import Path
from .base_loader import BaseLoader
from .error import YamlFileLoaderError
from typing import Dict,Any
import yaml
import os


class YamlFileLoader(BaseLoader):

    def load_from_file(self,file_path:str) -> Dict[str,Any]:

        """
        Returns a dict from .yaml file

        Args:
            file_path: The path of .yaml file 
        """

        _path = file_path

        if not os.path.exists(_path):
            raise YamlFileLoaderError(f"{_path} file not found")

        if not os.path.isfile(_path) or not _path.endswith('.yaml'):
            raise YamlFileLoaderError(f"{_path} should be a .yaml file")

        
        with open(_path, 'r') as file:
            _dict = yaml.load(file, Loader=yaml.SafeLoader)
            return _dict
