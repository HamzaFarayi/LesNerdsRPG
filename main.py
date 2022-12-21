import pygame, sys
import Player

pygame.display.set_caption("Les Nerds RPG")

def main():
    pygame.init()

    running = True

    CurrentPlayer = Player.Player("XXX", 100, 50, 0, 400, 304)

    while running:

        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Player Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    CurrentPlayer.X += 16
                if event.key == pygame.K_LEFT:
                    CurrentPlayer.X -= 16
                if event.key == pygame.K_DOWN:
                    CurrentPlayer.Y += 16
                if event.key == pygame.K_UP:
                    CurrentPlayer.Y -= 16


if __name__ == "main":
    main()
