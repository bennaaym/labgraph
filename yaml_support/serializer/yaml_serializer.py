from yaml.tokens import AnchorToken
from .base_serializer import BaseSerializer
from pathlib import Path
import yaml
import os


class YamlSerializer(BaseSerializer):
    """
    Serialize an object to YAML
    """
    @staticmethod
    def serialize(obj, file_name):
        assert isinstance(file_name, str)

        dist_dir = f"{Path(__file__).parent.parent}/outputs"

        if not os.path.exists(dist_dir):
            os.mkdir(dist_dir)

        with open(f"{dist_dir}/{file_name}",'a') as file:
            yaml.dump(obj, file, sort_keys=False)
            file.write('\n')



        