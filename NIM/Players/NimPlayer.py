from abc import ABC, abstractmethod

from Nim import Nim


class NimPlayer(ABC):

    def __init__(self, name:str, author:str="Unknown"):
        self.name = name
        self.author = author

    @abstractmethod
    def get_move(self, game: Nim) -> int:
        pass

    def get_config(self) -> dict[str, str]:
        return{
            "name": self.name,
            "author": self.author,
        }