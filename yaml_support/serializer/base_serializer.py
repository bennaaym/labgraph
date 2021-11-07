from abc import ABCMeta, abstractmethod


class BaseSerializer(metaclass=ABCMeta):
    """
    An abstraction for serializers.
    """

    @abstractmethod
    def serialize(self, obj):
        pass

