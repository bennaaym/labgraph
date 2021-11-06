from abc import ABCMeta, abstractmethod


class BaseParser(metaclass=ABCMeta):
    """
    An abstraction for parsers
    """

    @abstractmethod
    def parse(self, tree):
        pass