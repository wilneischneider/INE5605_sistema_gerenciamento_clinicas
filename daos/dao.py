import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, "wb"))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, "rb"))

    def add(self, chave, objeto):
        self.__cache[chave] = objeto
        self.__dump()

    def update(self, chave, objeto):
        try:
            if self.__cache[chave] != None:
                self.__cache[chave] = objeto
                self.__dump()
        except KeyError:
            return None

    def get(self, chave):
        try:
            return self.__cache[chave]
        except KeyError:
            return None

    def remove(self, chave):
        try:
            self.__cache.pop(chave)
            self.__dump()
        except KeyError:
            return None

    def get_all(self):
        return self.__cache.values()

    def get_dict(self):
        return self.__cache
