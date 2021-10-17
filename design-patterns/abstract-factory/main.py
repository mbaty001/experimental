import random


class Frog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}!'
        print(msg)

class Bug:
    def __str__(self):
        return 'a bug'
    def action(self):
        return 'eats it'


# Abstract factory
class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return '\n\n\t------ Frog World ------'
    # factory method
    def make_character(self):
        return Frog(self.player_name)
    # factory method
    def make_obstacle(self):
        return Bug()

class Wizard:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Wizard battles against {obstacle} and {act}!'
        print(msg)

class Ork:
    def __str__(self):
        return 'an evil ork'
    def action(self):
        return 'kills it'

class Troll:
    def __str__(self):
        return 'huge, slow troll'
    def action(self):
        return 'change it to the stone'

# Abstract factory
class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return '\n\n\t------ Wizard World ------'
    # factory method
    def make_character(self):
        return Wizard(self.player_name)
    # factory method
    def make_obstacle(self):
        if random.randint(0, 100) % 2 == 0:
            return Ork()
        else:
            return Troll()

class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you? ')
        age = int(age)
    except ValueError as err:
        print(f'Age {age} is invalid, please try again...')
        return (False, age)
    return (True, age)

def main():
    while True:
        name = input("Hello. What's your name? Type 'quit' to finish: ")
        if name == 'quit':
            break
        valid_input = False
        while not valid_input:
            valid_input, age = validate_age(name)
        while input("Action: ") != 'quit':
            game = FrogWorld if age < 18 else WizardWorld
            environment = GameEnvironment(game(name))
            environment.play()
    print('Bye!')
if __name__ == '__main__':
    main()