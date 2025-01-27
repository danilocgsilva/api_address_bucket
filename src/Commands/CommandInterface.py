import abc

class CommandInterface(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass
