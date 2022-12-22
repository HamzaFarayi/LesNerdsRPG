import pygame
import sys
from Game import *

pygame.display.set_caption("Les Nerds RPG")


def main():
    pygame.init()

    running = True

    CurrentGame = Game.Game()

    while running:

        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Player Movement
            if event.type == pygame.KEYDOWN:
                CurrentGame.player_movement(event.key)


if __name__ == "main":
    main()

