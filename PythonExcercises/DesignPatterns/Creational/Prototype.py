'''
Prototype -  lets you copy existing objects without making your code dependent on their classes.
delegates the cloning process to the actual objects that are being cloned. 

When use:
Use the Prototype pattern when your code shouldn’t depend on the concrete classes
of objects that you need to copy.
'''

from abc import abstractmethod, ABC

class Prototype(ABC):

    @abstractmethod
    def clone(self):
        raise NotImplementedError()
    

class Michal(Prototype):

    def __init__(self, arg1:str) -> None:
        self.arg1 = arg1
    
    def clone(self) -> Prototype:
        return Michal(self.arg1)
    
class MichalSubclass(Michal):
    
    def __init__(self, arg1:str, arg2:str) -> None:
        super().__init__(arg1)
        self.arg2 = arg2

    def clone(self) -> Prototype:
        return MichalSubclass(self.arg1, self.arg2)
    
michal = Michal(1)
print(f"ID: {michal}, arg1: {michal.arg1}")
clone = michal.clone()
print(f"ID: {clone}, arg1: {clone.arg1}")
