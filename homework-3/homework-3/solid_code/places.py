from abc import ABC, abstractmethod


class Place(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_antagonist(self):
        pass


class Kostroma(Place):
    def get_name(self):
        return 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    def get_name(self):
        return 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')
