
class UpTo:
    # giving the parameter a default value of 0
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        # The next method will throw an
        # exception when the termination condition is reached.
        if self.n > self.max:
            raise StopIteration
        else:
            result = self.n
            self.n += 1
            return result
for number in UpTo(5):
    print(number)