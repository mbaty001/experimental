'''
---=== Decorator (aka wrapper) ===---

- extends the functionality of object dynamically,
- alternative to subclasses,
- class become a decorator when it implements the same interface as opaque object, 
- from caller (application) it is identical

Stack = Notifier()
If sms_enabled: 
	stack = SMSDecorator(stack)
if email_enabled: 
	stack = EmailDecorator(stack)
app.setNotifier(stack);
notifier.send() -> email -> sms

When to use:
Use the Decorator pattern when you need to:
- be able to assign extra behaviors to objects at runtime without breaking the code that uses these objects.
'''

from abc import abstractmethod, ABC

class App():
    def set_notifier(self, notifier):
        self.notifier = notifier

    def do_something(self, message):
        self.notifier.send(message)

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        raise NotImplementedError()

class ConcreteNotifier(Notifier):
    def send(self, message):
        print(f"Concrete notifier: {message}")

class Wrapper():
    def __init__(self, wrappee):
        self.wrappee = wrappee

    def send(self, message):
        print(f"{message} from wrapper")
    
class SMSNotifier(Wrapper):
    def __init__(self, notifier):
        self.wrappee = notifier

    def send(self, message):
        print(f"Sending SMS: {message}")
        self.wrappee.send(message)

class SlackNotifier(Wrapper):
    def __init__(self, notifier):
        self.wrappee = notifier

    def send(self, message):
        print(f"Sending slack: {message}")
        self.wrappee.send(message)

class EmailNotifier(Wrapper):
    def __init__(self, notifier):
        self.wrappee = notifier

    def send(self, message):
        print(f"Sending Email: {message}")
        self.wrappee.send(message)

# stack = Notifier()
# stack = SMSNotifier(stack)
# stack = SlackNotifier(stack)
# stack = EmailNotifier(stack)

# app = App()
# app.set_notifier(stack)
# app.do_something("this is a message")


# -----------------


class Decorator(Notifier):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _notifier: Notifier = None

    def __init__(self, notifier: Notifier) -> None:
        self._notifier = notifier

    @property
    def notifier(self) -> Notifier:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._notifier

    def send(self, message) -> str:
        return self._notifier.send(message)


class SMSNotifier(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def send(self, message) -> str:
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        print(f"SMS {message}")
        self.notifier.send(message)


class EmailNotifier(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """

    def send(self, message) -> str:
        print(f"Email {message}")
        self.notifier.send(message)





if __name__ == "__main__":

    app = App()

    # This way the client code can support both simple components...
    stack = ConcreteNotifier()
    app.set_notifier(stack)
    app.do_something("this is a message")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    stack = ConcreteNotifier()
    stack = SMSNotifier(stack)
    stack = EmailNotifier(stack)
    
    app.set_notifier(stack)
    app.do_something("this is a message")
