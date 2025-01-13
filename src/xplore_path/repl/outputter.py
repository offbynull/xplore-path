from abc import abstractmethod, ABC


class Outputter(ABC):
    @abstractmethod
    def extension(self):
        ...

    @abstractmethod
    def output(self, collection, write_path):
        ...
