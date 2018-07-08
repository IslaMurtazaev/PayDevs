import abc


class Interactor(abc.ABC):

    """ Base class Interactor """

    @abc.abstractmethod
    def set_params(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        pass
