import pygame
import sys
import player
import draw
import sprite
from button import Button
from config import *
from pyvidplayer import Video

BG = pygame.image.load("images/Background.jpg")
pygame.display.set_caption("Les Nerds RPG")
SCREEN = pygame.display.set_mode((800, 608))


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


vid = Video("resources/video/intro.mp4")
vid.set_size((800, 608))


def intro():
    while True:
        vid.draw(SCREEN, (0, 0))

        for event in pygame.event.get():
            if event.type == 768:
                if event.key == pygame.K_RETURN:
                    vid.close()
                    while start.running:
                        start.main()

        pygame.display.update()


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

        intro()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(425, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("images/Play Rect.png"), pos=(400, 240), 
                            text_input="PLAY", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("images/Options Rect.png"), pos=(400, 330), 
                            text_input="OPTIONS", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("images/Quit Rect.png"), pos=(400, 420), 
                            text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


# Returns Press-Start-2P in the desired size
def get_font(size):
    return pygame.font.Font("resources/fonts/font.ttf", size)


start = Start()

main_menu()
while start.running:
    start.main()

main_menu()
pygame.quit()
sys.exit()
