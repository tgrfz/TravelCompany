from abc import ABC, abstractmethod

class AbstractList(ABC):
    @abstractmethod
    def append():
        pass

    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)
    

    