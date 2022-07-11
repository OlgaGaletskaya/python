from places import Place
from abc import ABC, abstractmethod

class FireAGun:
    def fire_a_gun(self):
        print('PIU PIU')

class Lazers:
    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

class RoundhouseKick:
    def roundhouse_kick(self):
        print('Bump')

class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
    
    def find(self, place: Place):
        place.get_antagonist()

    def find(self, place: Place):
        place.get_antagonist()

    @abstractmethod
    def attack(self):
        pass

    def ultimate(self):
        pass


class Superman(SuperHero, Lazers):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        return 'Kick'

    def ultimate(self):
        self.incinerate_with_lasers()

class ChackNorris (SuperHero, FireAGun):

    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris', False)

    def attack(self):
        self.fire_a_gun()

