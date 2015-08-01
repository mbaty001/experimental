import json
import pygame
import sys

from pygame.locals import *
from utils.logger import log
from utils.model import *
from pip._vendor.html5lib.filters import whitespace
from pygame.surface import Surface

VERSION = '0.02 20150721'
MAP = 'europe1914'
COMPANY = 'Batir Software'
NAME = 'War'

class War(object):
    def __init__(self, sizeX=800, sizeY=600, sizeFont=12):
        log.debug('Creating War object')
        self.world = ''
        pygame.init()
        pygame.display.set_caption('%s - %s %s' %(NAME, COMPANY, VERSION))
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.sizeF = sizeFont
        self.screen = pygame.display.set_mode((self.sizeX, self.sizeY))                
        
    def load_map(self, map_file='maps/%s.png' %MAP):
        log.debug('Loading map: %s' %map_file)
        self.map = pygame.image.load(map_file)
        self.map = pygame.transform.scale(self.map, (self.sizeX, self.sizeY))     
        with open('maps/%s.json' %MAP, 'r') as json_file:
            self.data = json.load(json_file)
        log.debug(self.data)
        
    def create_objects(self):        
        self.world = World(self.sizeF)
        
        for country in self.data['countries']:
            country_object = Country(country['name'], country['color'], country['neighbors'], 
                                     country['income'], country['attack'], country['defense'],
                                     country['experience'], country['number'], country['morale'])
            self.world.all_countries.append(country_object)            
        
    def terminate(self):
        pygame.quit()
        sys.exit()
        
    def print_status(self, sizeX, sizeY):
        pygame.draw.rect(self.map, WHITE, (1, 1, sizeX, sizeY))
        fontObj = pygame.font.SysFont('calibri', self.sizeF)
        
        if len(self.world.msg) == 0:
            textRect = self.print_first_msg(self.map, fontObj, 'Your country: %s' %self.world.player_country, BLUE, WHITE)            
            self.print_next_msg(self.map, fontObj, textRect, 'Attack: %s' %self.world.player_country.get_attack(), BLUE, WHITE)
            self.print_next_msg(self.map, fontObj, textRect, 'Defense: %s' %self.world.player_country.get_defense(), BLUE, WHITE)
            self.print_next_msg(self.map, fontObj, textRect, 'Experience: %s' %self.world.player_country.get_experience(), BLUE, WHITE)
            self.print_next_msg(self.map, fontObj, textRect, 'Morale: %s' %self.world.player_country.get_morale(), BLUE, WHITE)
            self.print_next_msg(self.map, fontObj, textRect, 'Size of army: %s' %self.world.player_country.get_number(), BLUE, WHITE)
            self.print_next_msg(self.map, fontObj, textRect, 'No of recruits: %s' %self.world.player_country.get_income(), BLUE, WHITE)
        else:            
            textRect = self.print_first_msg(self.map, fontObj, self.world.msg[0], BLUE, WHITE)
            for msg in self.world.msg[1:]:
                self.print_next_msg(self.map, fontObj, textRect, msg, BLUE, WHITE)                
        
    def print_first_msg(self, surface, fontObj, msg, color, bColor):
        textSurface = fontObj.render(msg, True, color, bColor)
        textRect = textSurface.get_rect()
        surface.blit(textSurface, textRect)
        return textRect
    
    def print_next_msg(self, surface, fontObj, textRect, msg, color, bColor):
        textSurface = fontObj.render(msg, True, BLUE, WHITE)
        textRect.centery += (self.sizeF + 1)
        surface.blit(textSurface, textRect)
        
    def run(self):       
        self.load_map()
        self.create_objects()
        self.world.set_player_country()
                                
        #        
        # Display status window
        #
        self.print_status(self.sizeX/5, self.sizeY/3)
        self.screen.blit(self.map, (0,0))
        while True:            
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                log.debug('QUIT')
                self.terminate()
            elif event.type == MOUSEBUTTONUP:
                log.debug('MOUSEBUTTONUP')
                mouseX, mouseY = event.pos
                clicked_color = self.map.get_at((mouseX, mouseY))
                log.debug('Clicked color: %s' %clicked_color)
                #
                # Analyze if player clicked a neighbor, his country or nothing important 
                #
                self.world.click(clicked_color)
            
            self.print_status(self.sizeX/5, self.sizeY/3)
            self.screen.blit(self.map, (0,0))
            pygame.display.update()
            
            self.world.msg = list()       
        
def main():
    war = War()
    try:
        war.run()
    except Exception, error: 
        log.debug('Exception catch: %s' %error)
        war.terminate()
    
if __name__ == '__main__':
    main()