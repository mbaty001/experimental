from ast import literal_eval
from logger import log

class Country(object):
    ''' class describing Country object '''
    def __init__(self, name, color, neighbors, income, attack, 
                 defense, experience, number, morale):
        log.debug('Creating Country object for %s' %name)
        self.name = name     
        self.color = literal_eval(color) # convert from str '( )' to tuple ()  
        self.neighbors = neighbors # list
        self.income = income # 0-10
        self.attack = attack # 1-50
        self.defense = defense # 1-50
        self.experience = experience # 1 - 1 000 000
        self.number = number # 1 - 1 000
        self.morale = morale # -2 -1 0 1 2
        
    def __str__(self):
        return self.get_name()
       
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_neighbors(self):
        return self.neighbors
    
    def add_neighbors(self, new_neighbors):
        log.debug('Add new neighbors to %s: %s' %(self, new_neighbors))
        for neighbor in new_neighbors:
            self.neighbors.append(neighbor)    
    
    def del_neighbors(self, old_neighbors):
        log.debug('Remove neighbors from %s: %s' %(self, old_neighbors))
        for neighbor in old_neighbors:
            self.neighbors.remove(neighbor)
            
    def get_income(self):
        return self.income
    
    def increase_income(self, increase):
        log.debug('Increase income for %s by %s' %(self, increase))
        self.income += increase
        
    def decrease_income(self, decrease):
        log.debug('Decrease income for %s by %s' %(self, decrease))
        self.income -= decrease
        
    def get_attack(self):
        return self.attack
    
    def increase_attack(self, increase):
        log.debug('Increase attack for %s by %s' %(self, increase))
        self.attack += increase
        
    def get_defense(self):
        return self.defense
    
    def increase_defense(self, increase):
        log.debug('Increase defense for %s by %s' %(self, increase))
        self.defense += increase
        
    def get_experience(self):
        return self.experience
    
    def increase_experience(self, increase):
        log.debug('Increase experience for %s by %s' %(self, increase))
        self.experience += increase
        
    def get_number(self):
        return self.number
    
    def increase_number(self, increase):
        log.debug('Increase number for %s by %s' %(self, increase))
        self.number += increase
        
    def decrease_number(self, decrease):
        log.debug('Decrease number for %s by %s' %(self, decrease))
        self.number -= decrease
        
    def get_morale(self):
        return self.morale
    
    def increase_morale(self, increase):
        log.debug('Increase morale for %s by %s' %(self, increase))
        if self.morale < 2:        
            self.morale += increase        
    
    def decrease_morale(self, decrease):
        log.debug('Decrease morale for %s by %s' %(self, decrease))
        if self.morale > -2:
            self.morale -= decrease            
    
class World(object):
    ''' class describing whole World (all the countries) '''
    def __init__(self):
        log.debug('Creating world object')
        self.all_countries = list()
        self.player_country = None
        
    def get_country_by_name(self, name):
        ''' return Country object if country with such name exists (or None) '''    
        for country in self.all_countries:
            if country.get_name() == name:
                return country
        return None

    def get_country_by_color(self, color):
        ''' return Country object if country with such color exists (or None) '''
        log.debug('Checking %s' %color)
        for country in self.all_countries:
            log.debug('Checking %s' %country)
            log.debug('COLOR: ' + str(country.get_color()))
            if country.get_color() == color:
                log.debug('Found %s' %country)
                return country
        return None
    
    def click(self, color):
        ''' analyze what has been clicked '''
        clicked_country = self.get_country_by_color(color)
        log.debug('Clicked country: %s' %clicked_country)
        if clicked_country == self.player_country:
            log.debug('Player has clicked in his country')
            log.debug('TODO Player country infortmation should be displayed')
        elif clicked_country == None:
            log.debug('Player has clicked nothing important')
        else:
            log.debug(self.player_country.get_neighbors())
            if str(clicked_country) in self.player_country.get_neighbors():
                log.debug('Player has clicked in his country neighbor: WAR!')
            else: 
                log.debug('Player has clicked in NOT his country neighbor')
                log.debug('TODO message will be show - this country it to far away')