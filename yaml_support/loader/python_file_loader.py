from .base_loader import BaseLoader
from .error import PythonFileLoaderError
from typing import List
from pathlib import Path
import os

class PythonFileLoader(BaseLoader):

    def load_from_file(self,path:str) -> List[str]:

        """
        Returns a list of string from .py file

        Args:
            file_path: The path of .py file 
        """

        _path = f"{Path(__file__).parent.parent}/{path}"
        
        if not os.path.exists(_path):
            raise PythonFileLoaderError(f"{_path} file not found")

        if not os.path.isfile(_path) or not _path.endswith('.py'):
            raise PythonFileLoaderError(f"{_path} should be a .py file")


        with open(_path, 'r') as file:
            string = file.read()
            assert isinstance(string,str)

            return string
