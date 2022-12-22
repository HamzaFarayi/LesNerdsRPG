import pygame
import sys
import player
import draw
from config import *

pygame.display.set_caption("Les Nerds RPG")


class Start:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True

        self.player = player.Player("XXX", 100, 50, 0, 384, 320)
        self.Draw = draw.Draw(self.screen)

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = True
                if event.key == pygame.K_DOWN:
                    self.player.moving_down = True
                if event.key == pygame.K_UP:
                    self.player.moving_up = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = False
                if event.key == pygame.K_DOWN:
                    self.player.moving_down = False
                if event.key == pygame.K_UP:
                    self.player.moving_up = False

    def player_movement(self):
        if self.player.moving_right:
            self.player.X += 32
        if self.player.moving_left:
            self.player.X -= 32
        if self.player.moving_down:
            self.player.Y += 32
        if self.player.moving_up:
            self.player.Y -= 32

    def draw(self):
        self.screen.fill("black")

        self.Draw.draw_lines()

        self.Draw.draw_player(self.player.X, self.player.Y)

        pygame.display.flip()

    def main(self):

        while self.playing:
            self.events()

            self.player_movement()
            self.draw()

            self.clock.tick(10)


start = Start()

while start.running:
    start.main()

pygame.quit()
sys.exit()
