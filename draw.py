import pygame
import config


class Draw:

    def __init__(self, screen):
        self.screen = screen

    def draw_lines(self):
        width = config.WIN_WIDTH
        height = config.WIN_HEIGHT

        for x in range(25):
            pygame.draw.line(self.screen, (255, 255, 255), (x*32, 0), (x*32, height))

        for y in range(19):
            pygame.draw.line(self.screen, (255, 255, 255), (0, y*32), (width, y*32))

    def draw_player(self, x, y):
        color = (255, 0, 0)
        rect = pygame.rect.Rect(x, y, 32, 32)

        pygame.draw.rect(self.screen, color, rect)




