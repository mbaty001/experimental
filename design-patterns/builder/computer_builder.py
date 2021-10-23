class Computer():
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None # in gigabytes
        self.hdd = None # in gigabytes
        self.gpu = None
    def __str__(self):
        info = (f'Memory: {self.memory}GB',
                f'Hard disk: {self.hdd}GB',
                f'Graphics card: {self.gpu}')
        return '\n'.join(info)

class Tablet():
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.cpu = None
        self.size = None
    def __str__(self):
        info = (f'Memory: {self.memory}GB',
                f'CPU: {self.cpu}GB',
                f'Size: {self.size}')
        return '\n'.join(info)

class ComputerBuilder():
    def __init__(self, serial):
        self.computer = Computer(serial)
    def configure_memory(self, amount):
        self.computer.memory = amount
    def configure_hdd(self, amount):
        self.computer.hdd = amount
    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model

class TabletBuilder():
    def __init__(self, name):
        self.tablet = Tablet(name)
    def configure_memory(self, amount):
        self.tablet.memory = amount
    def configure_cpu(self, amount):
        self.tablet.cpu = amount
    def configure_size(self, size):
        self.tablet.size = size

class HardwareEngineer():
    def __init__(self):
        self.builder = None
    def construct_computer(self, serial, memory, hdd, gpu):
        self.builder = ComputerBuilder(serial)
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)
        
    def construct_tablet(self, name, memory, cpu, size):
        self.builder = TabletBuilder(name)
        self.builder.configure_memory(memory)
        self.builder.configure_cpu(cpu)
        self.builder.configure_size(size)

    @property
    def computer(self):
        return self.builder.computer

    @property
    def tablet(self):
        return self.builder.tablet

def main():
    engineer = HardwareEngineer()
    engineer.construct_computer('AS213123', 500, 4, "Nvidia")
    print(engineer.computer)
    engineer.construct_tablet('Acer', 4, 8, 12)    
    print(engineer.tablet)

if __name__ == "__main__":
    main()