from abc import ABCMeta, abstractmethod


class BaseLoader(metaclass = ABCMeta):
    """
    An abstraction for file loaders
    """
    @abstractmethod
    def load_from_file(self):
        pass