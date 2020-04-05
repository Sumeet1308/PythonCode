from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        pass
        #print ("This is HP laptop")

Comp=Laptop()
Comp.process()
