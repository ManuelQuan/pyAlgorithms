from abc import ABC,abstractmethod
from AdjacencyList import AdjacencyList
class Search:
    @abstractmethod
    def __init__(self,graph,s):
        pass

    @abstractmethod
    def marked(v) -> bool:
        pass

    @abstractmethod
    def count() -> int:
        pass