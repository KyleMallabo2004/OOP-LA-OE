LA#27
from abc import ABC, abstractmethod

class PowerRangers(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Red(PowerRangers):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"

class NewPowerRangers(PowerRangers):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"


import structure as st

red = st.Red("Red", "Redflag")
new_ranger = st.NewPowerRangers("NewPowerRangers", "Green")

print(red.alias)
print(new_ranger.alias)
