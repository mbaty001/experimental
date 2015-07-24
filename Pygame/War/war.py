import json
import pygame
import random
import sys

from pygame.locals import *
from utils.logger import log
from utils.model import Country, World

VERSION = '0.02 20150721'
MAP = 'europe1914'
COMPANY = 'Batir Software'
NAME = 'War'

class War(object):
    def __init__(self, sizeX=800, sizeY=600):
        log.debug('Creating War object')
        self.world = ''
        pygame.init()
        pygame.display.set_caption('%s - %s %s' %(NAME, COMPANY, VERSION))
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.screen = pygame.display.set_mode((self.sizeX, self.sizeY))                
        
    def load_map(self, map_file='maps/%s.png' %MAP):
        log.debug('Loading map: %s' %map_file)
        self.map = pygame.image.load(map_file)
        self.map = pygame.transform.scale(self.map, (self.sizeX, self.sizeY))     
        with open('maps/%s.json' %MAP, 'r') as json_file:
            self.data = json.load(json_file)
        log.debug(self.data)
        
    def create_objects(self):        
        self.world = World()
        
        for country in self.data['countries']:
            country_object = Country(country['name'], country['color'], country['neighbors'], 
                                     country['income'], country['attack'], country['defense'],
                                     country['experience'], country['number'], country['morale'])
            self.world.all_countries.append(country_object)
            
    def choose_country_for_player(self, countries):
        forPlayer = random.sample(countries, 1)[0]
        log.debug('Choosen country: %s' %forPlayer)
        return forPlayer
        
    def terminate(self):
        pygame.quit()
        sys.exit()    
        
    def run(self):       
        self.load_map()
        self.create_objects()
        self.world.player_country = self.choose_country_for_player(self.world.all_countries)
        
        self.screen.blit(self.map, (0,0))
        while True:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    log.debug('QUIT')
                    self.terminate()
                if event.type == MOUSEBUTTONUP:
                    log.debug('MOUSEBUTTONUP')
                    mouseX, mouseY = event.pos
                    clicked_color = self.map.get_at((mouseX, mouseY))                    
                    log.debug('Clicked color: %s' %clicked_color)
                    #
                    # Analyze if player clicked a neighbor, his country or nothing important 
                    #
                    self.world.click(clicked_color)
                    
            pygame.display.update()            
        
def main():
    war = War()
    try:
        war.run()
    except Exception, error: 
        log.debug('Exception catch: %s' %error)
        war.terminate()
    
if __name__ == '__main__':
    main()