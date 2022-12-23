import pygame
import sys
import player
import draw
import sprite
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
        self.Sprite = sprite.Sprite()

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.horizontal_direction = "right"

                if event.key == pygame.K_LEFT:
                    self.player.horizontal_direction = "left"

                if event.key == pygame.K_DOWN:
                    self.player.vertical_direction = "down"

                if event.key == pygame.K_UP:
                    self.player.vertical_direction = "up"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.player.horizontal_direction = None

                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.player.vertical_direction = None

                if self.player.horizontal_direction is None and self.player.vertical_direction is None:
                    self.player.sprite_index = 0

    def player_movement(self):
        if self.player.horizontal_direction is None and self.player.vertical_direction is None:
            return

        if self.player.horizontal_direction == "right":
            self.player.X += 32

        if self.player.horizontal_direction == "left":
            self.player.X -= 32

        if self.player.vertical_direction == "down":
            self.player.Y += 32

        if self.player.vertical_direction == "up":
            self.player.Y -= 32

        # Update index
        self.player.sprite_index += 1
        self.player.sprite_index = self.player.sprite_index % 8

    def draw(self):
        self.screen.fill("black")

        self.Draw.draw_lines()

        sprite = self.Sprite.return_sprite(self.player.sprite_index, self.player.horizontal_direction,
                                           self.player.vertical_direction)

        self.Draw.draw_player(self.player.X, self.player.Y, sprite)

        pygame.display.flip()

    def main(self):

        while self.playing:
            self.events()

            self.player_movement()
            self.draw()

            self.clock.tick(4)


start = Start()

while start.running:
    start.main()

pygame.quit()
sys.exit()
