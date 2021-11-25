from .base_loader import BaseLoader
from .error import PythonFileLoaderError
from typing import List
import os

class PythonFileLoader(BaseLoader):

    def load_from_file(self,abs_path:str) -> List[str]:

        """
        Returns a list of string from .py file

        Args:
            abs_path: The absolute path of .py file 
        """

        
        if not os.path.exists(abs_path):
            raise PythonFileLoaderError(f"{abs_path} file not found")

        if not os.path.isfile(abs_path) or not abs_path.endswith('.py'):
            raise PythonFileLoaderError(f"{abs_path} should be a .py file")


        with open(abs_path, 'r') as file:
            string = file.read()
            assert isinstance(string,str)

            return string
