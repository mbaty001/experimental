MINI14 = '1.4GHz Mac mini'

class AppleFactory:
    ''' director object '''
    class MacMini14:
        ''' builder object '''
        def __init__(self):
            self.memory = 4 # in gigabytes
            self.hdd = 500 # in gigabytes
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = (f'Model: {MINI14}',
                    f'Memory: {self.memory}GB',
                    f'Hard Disk: {self.hdd}GB')
            return '\n'.join(info)
    
    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            msg = f"I don't know how to build {model}"
            print(msg)

if __name__ == "__main__":
    apple_factory = AppleFactory()
    mac_mini = apple_factory.build_computer(MINI14)
    print(mac_mini)