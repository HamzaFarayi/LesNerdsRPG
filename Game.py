import Player
import pygame


class Game:
    def __init__(self):
        self.Player = Player.Player("XXX", 100, 50, 0, 400, 304)

    def player_movement(self, key):
        if key == pygame.K_RIGHT:
            self.Player.X += 16
        if key == pygame.K_LEFT:
            self.Player.X -= 16
        if key == pygame.K_DOWN:
            self.Player.Y += 16
        if key == pygame.K_UP:
            self.Player.Y -= 16
