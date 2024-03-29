import json
# import tomllib
from pprint import pprint
from typing import Type
from .__CustomException import ArgumentException
from .__PrefLoader import *


class PreferencesTreeBase:
    def __init__(self, filename: str = None,
                 pref_dict: dict = None,
                 loader: Type[PreferencesLoaderBase] = PreferencesLoaderJSON,
                 default_filename='settings.json'):
        self.__loader = loader
        self.__pref: dict | None = None
        self.__filename = default_filename

        if filename is not None and pref_dict is not None:
            raise ArgumentException('Wrong argument called on {}!'.format(self.__class__.__name__))
        if filename is None and pref_dict is None:
            raise ArgumentException('No argument called on {}!'.format(self.__class__.__name__))
        if filename is not None:
            self.__filename = filename
            self.__pref = self.__loader.load(filename)
        elif pref_dict is not None:
            self.__pref = pref_dict

    @property
    def tree(self) -> dict:
        return self.__pref

    def to_dict(self):
        return self.tree

    def __getitem__(self, item: str):
        return self.__pref.__getitem__(item)

    def __setitem__(self, key, value):
        self.__pref.__setitem__(key, value)

    def setdefault(self, key, value):
        self.__pref.setdefault(key, value)

    def remove(self, key):
        """
        Remove value from preferences tree

        :param key: Key
        :return: Value removed
        """
        return self.__pref.pop(key)

    def __len__(self):
        return self.__pref.__len__()

    def save(self, filename: str = None):
        """
        Save preferences tree to json file

        :param filename: File name to save to
        :return:
        """
        if filename is None:
            self.__loader.write(self.__pref, self.__filename)
        else:
            self.__loader.write(self.__pref, filename)

    def print(self):
        pprint(self.__pref)

    def __str__(self):
        return str(self.__pref)

    def __repr__(self):
        return self.__str__()
