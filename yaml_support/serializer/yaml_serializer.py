from .base_serializer import BaseSerializer
import yaml
import os
import ntpath


class YamlSerializer(BaseSerializer):
    """
    Serialize an object to YAML
    """
    @staticmethod
    def serialize(obj, file_name)-> None:
        assert isinstance(file_name, str)

       
        dist_dir = f"yaml_outputs"

        if not os.path.exists(dist_dir):
            os.mkdir(dist_dir)

        with open(f"{dist_dir}/{ntpath.basename(file_name)}",'a') as file:
            yaml.dump(obj, file, sort_keys=False)
            file.write('\n')



        