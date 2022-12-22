import pygame
import sys
import Game
from config import *

pygame.display.set_caption("Les Nerds RPG")

class Start():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True




    def events(self):

        CurrentGame = Game.Game()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                CurrentGame.player_movement(event.key)


    def draw(self):
        self.screen.fill('black')


    def main(self):

        
        while self.playing:
            self.events()
            self.draw()




start = Start()

while start.running:
    start.main()

pygame.quit()
sys.exit()
