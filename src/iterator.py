from abc import ABC, abstractmethod
# from component import Component

class Iterator(ABC):
    def __init__(self) -> None:
        self.children = []

    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass

class ComponentIterator(Iterator):
    def __init__(self) -> None:
        super().__init__()
        
    def has_next(self) -> bool:
        return len(self.children) > 0

    def next(self):
        if not self.has_next():
            return None
        current = self.children.pop(0)
        return current
