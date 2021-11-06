from .base_loader import BaseLoader
from .error import PythonFileLoaderError
from typing import List
import os

class PythonFileLoader(BaseLoader):

    def load_from_file(self,path:str) -> List[str]:

        """
        Returns a list of string from .py file

        Args:
            file_path: The path of .py file 
        """

        if not os.path.exists(path):
            raise PythonFileLoaderError(f"{path} file not found")

        if not os.path.isfile(path) or not path.endswith('.py'):
            raise PythonFileLoaderError(f"{path} should be a .py file")

        
        with open(path, 'r') as file:
            string = file.read()
            assert isinstance(string,str)

            return string
