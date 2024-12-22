from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

class Leonardo(NinjaTurtle):
    def __init__(self):
        self._real_name = "Leonardo"
        self._alias = "Leo"

    @property
    def name(self):
        return self._alias

class Michelangelo(NinjaTurtle):
    def __init__(self):
        self._real_name = "Michelangelo"
        self._alias = "Mikey"

    @property
    def name(self):
        return self._alias

class Donatello(NinjaTurtle):
    def __init__(self):
        self._real_name = "Donatello"
        self._alias = "Donnie"

    @property
    def name(self):
        return self._alias

class Raphael(NinjaTurtle):
    def __init__(self):
        self._real_name = "Raphael"
        self._alias = "Raph"

    @property
    def name(self):
        return self._alias