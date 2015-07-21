import json
import pygame
import sys

from pygame.locals import *

VERSION = '0.01 20150717'
MAP = 'europe1914'

class War(object):
    def __init__(self, sizeX=800, sizeY=600):    
        pygame.init()
        pygame.display.set_caption('War - Batir Software %s' %VERSION)
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.screen = pygame.display.set_mode((self.sizeX, self.sizeY))                
        
    def load_map(self, map_file='maps/%s.png' %MAP):
        self.map = pygame.image.load(map_file)
        self.map = pygame.transform.scale(self.map, (self.sizeX, self.sizeY))     
        with open('maps/%s.json' %MAP, 'r') as json_file:
            self.data = json.load(json_file)
        print self.data    
        
    def terminate(self):
        pygame.quit()
        sys.exit()    
        
    def run(self):
        
        self.load_map()
        self.screen.blit(self.map, (0,0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == MOUSEBUTTONUP:
                    mouseX, mouseY = event.pos
                    clicked_color = self.map.get_at((mouseX, mouseY))                    
                    for country in self.data['countries']:
                        if str(clicked_color) == country['color']:
                            print 'dude, you clikced %s' %country
            pygame.display.update()
            
        
def main():
    war = War()
    war.run()
    
if __name__ == '__main__':
    main()