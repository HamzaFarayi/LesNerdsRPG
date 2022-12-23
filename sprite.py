import pygame


class Sprite:

    right_sprite_sheet = pygame.image.load("resources/graphics/player/right.png")
    left_sprite_sheet = pygame.image.load("resources/graphics/player/left.png")
    down_sprite_sheet = pygame.image.load("resources/graphics/player/down.png")
    up_sprite_sheet = pygame.image.load("resources/graphics/player/up.png")

    last_direction = "down"

    def __init__(self):
        self.right_sprites = self.load_sprites_right()
        self.left_sprites = self.load_sprites_left()
        self.down_sprites = self.load_sprites_down()
        self.up_sprites = self.load_sprites_up()

        self.sprites = {"right": self.right_sprites,
                        "left": self.left_sprites,
                        "down": self.down_sprites,
                        "up": self.up_sprites}

    def load_sprites_right(self):

        sprites = [Sprite.right_sprite_sheet.subsurface(pygame.rect.Rect(21, 4, 21, 48)),
                   Sprite.right_sprite_sheet.subsurface(pygame.rect.Rect(84, 5, 25, 47)),
                   Sprite.right_sprite_sheet.subsurface(pygame.rect.Rect(149, 4, 22, 47)),
                   Sprite.right_sprite_sheet.subsurface(pygame.rect.Rect(211, 4, 23, 47)),
                   Sprite.right_sprite_sheet.subsurface(pygame.rect.Rect(274, 4, 24, 48)),
                   Sprite.right_sprite_sheet.subsurface(pygame.rect.Rect(336, 5, 28, 47)),
                   Sprite.right_sprite_sheet.subsurface(pygame.rect.Rect(402, 4, 24, 48)),
                   Sprite.right_sprite_sheet.subsurface(pygame.rect.Rect(467, 4, 23, 48)),
                   Sprite.right_sprite_sheet.subsurface(pygame.rect.Rect(532, 4, 22, 48))]

        return sprites

    def load_sprites_left(self):

        sprites = [Sprite.left_sprite_sheet.subsurface(pygame.rect.Rect(22, 1, 21, 48)),
                   Sprite.left_sprite_sheet.subsurface(pygame.rect.Rect(83, 2, 25, 47)),
                   Sprite.left_sprite_sheet.subsurface(pygame.rect.Rect(149, 3, 22, 47)),
                   Sprite.left_sprite_sheet.subsurface(pygame.rect.Rect(214, 1, 23, 47)),
                   Sprite.left_sprite_sheet.subsurface(pygame.rect.Rect(278, 1, 24, 48)),
                   Sprite.left_sprite_sheet.subsurface(pygame.rect.Rect(340, 2, 28, 47)),
                   Sprite.left_sprite_sheet.subsurface(pygame.rect.Rect(406, 1, 24, 48)),
                   Sprite.left_sprite_sheet.subsurface(pygame.rect.Rect(470, 1, 23, 48)),
                   Sprite.left_sprite_sheet.subsurface(pygame.rect.Rect(534, 1, 22, 48))]

        return sprites

    def load_sprites_down(self):

        sprites = [Sprite.down_sprite_sheet.subsurface(pygame.rect.Rect(17, 1, 30, 49)),
                   Sprite.down_sprite_sheet.subsurface(pygame.rect.Rect(81, 1, 30, 49)),
                   Sprite.down_sprite_sheet.subsurface(pygame.rect.Rect(145, 1, 30, 50)),
                   Sprite.down_sprite_sheet.subsurface(pygame.rect.Rect(210, 2, 29, 49)),
                   Sprite.down_sprite_sheet.subsurface(pygame.rect.Rect(273, 1, 30, 50)),
                   Sprite.down_sprite_sheet.subsurface(pygame.rect.Rect(337, 1, 30, 49)),
                   Sprite.down_sprite_sheet.subsurface(pygame.rect.Rect(401, 1, 30, 50)),
                   Sprite.down_sprite_sheet.subsurface(pygame.rect.Rect(465, 2, 29, 49)),
                   Sprite.down_sprite_sheet.subsurface(pygame.rect.Rect(529, 1, 30, 50))]

        return sprites

    def load_sprites_up(self):

        sprites = [Sprite.up_sprite_sheet.subsurface(pygame.rect.Rect(17, 5, 30, 48)),
                   Sprite.up_sprite_sheet.subsurface(pygame.rect.Rect(81, 5, 30, 48)),
                   Sprite.up_sprite_sheet.subsurface(pygame.rect.Rect(145, 5, 30, 49)),
                   Sprite.up_sprite_sheet.subsurface(pygame.rect.Rect(209, 6, 29, 49)),
                   Sprite.up_sprite_sheet.subsurface(pygame.rect.Rect(274, 5, 29, 49)),
                   Sprite.up_sprite_sheet.subsurface(pygame.rect.Rect(337, 5, 30, 48)),
                   Sprite.up_sprite_sheet.subsurface(pygame.rect.Rect(401, 5, 30, 49)),
                   Sprite.up_sprite_sheet.subsurface(pygame.rect.Rect(466, 6, 29, 49)),
                   Sprite.up_sprite_sheet.subsurface(pygame.rect.Rect(529, 5, 30, 49))]

        return sprites

    def return_sprite(self, index, horizontal_direction, vertical_direction):
        if horizontal_direction is None and vertical_direction is None:
            return self.sprites[Sprite.last_direction][index]

        if vertical_direction is not None:
            Sprite.last_direction = vertical_direction
            return self.sprites[vertical_direction][index]

        Sprite.last_direction = horizontal_direction
        return self.sprites[horizontal_direction][index]



