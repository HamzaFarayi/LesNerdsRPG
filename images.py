import pygame
pygame.init()

SX = 640
SY = 640

screen = pygame.display.set_mode((SX, SY))
screen.fill((30, 200, 100))

class image:
    def __init__(self, Image, load, x, y):
        self.Image = Image
        self.load = load
        self.x = x
        self.y = y

    def loadImage(self):
        a = pygame.image.load(self.load)
        self.Image = pygame.transform.scale(a, (32, 32))

i1 = image("", 'cloud.png', 0, 0)
i2 = image("", 'cloud_around_outside.png', 32, 0)
i3 = image("", 'cloud_corner.png', 64, 0)
i4 = image("", 'cloud_side.png', 96, 0)
i5 = image("", 'grass_1.png', 128, 0)
i6 = image("", 'grass_2.png', 160, 0)
i7 = image("", 'grass_3.png', 192, 0)
i8 = image("", 'grass_corner.png', 224, 0)
i9 = image("", 'grass_corner_2.png', 256, 0)
i10 = image("", 'grass_side.png', 288, 0)
i11 = image("", 'grass_side_2.png', 320, 0)
i12 = image("", 'soil.png', 352, 0)
i13 = image("", 'soil_2.png', 384, 0)
i14 = image("", 'soil_corner.png', 416, 0)
i15 = image("", 'soil_corner_2.png', 448, 0)
i16 = image("", 'soil_side.png', 480, 0)
i17 = image("", 'soil_side_2.png', 512, 0)
images = (i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17)

for a in images:
    a.loadImage()
    screen.blit(a.Image, (a.x, a.y))


for x in range(20):
    pygame.draw.line(screen, (255,255, 255), (32*x-0.5, 0), (32*x-0.5, 640))
    pygame.draw.line(screen, (255, 255, 255), (0, 32*x-0.5), (640, 32*x-0.5))

Run = True
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

    pygame.display.update()

pygame.quit()

