'''
Command - turns a request into a stand-alone object that contains all information about the request. 
This transformation lets you pass requests as a method arguments,
delay or queue a request’s execution, and support undoable operations.

When to use:
Use the Command pattern when you want to queue operations,
schedule their execution,
or execute them remotely.
'''

from abc import abstractmethod, ABC

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Invoker(object):
    def set_command(self, command: Command) -> None:
        self.command = command
    def execute_command(self) -> None:
        self.command.execute()

class DeleteCommand(Command):
    def __init__(self, msg:str) -> None:
        self.msg = msg
    def execute(self) -> None:
        print(f"Deleting...{self.msg}")

class DisplayCommand(Command):
    def execute(self) -> None:
        print(f"Displaying...")

invoker = Invoker()

delete = DeleteCommand("kuku")
display = DisplayCommand()

invoker.set_command(delete)
invoker.execute_command()

invoker.set_command(display)
invoker.execute_command()
