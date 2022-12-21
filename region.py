import pygame

BlockList = []
class region:
  def __init__(self, mainColor, mainColor_2, lineColor):
    self.mainColor = mainColor
    self.mainColor_2 = mainColor_2
    self.lineColor = lineColor


  def DrawLines(self, screen):
    for a in range(50):
      pygame.draw.line(screen, self.lineColor, (16*(a+1), 0), (16*(a+1), 608), 1)
      LineList = []
      for b in range(38):
        LineList.append("-")

      BlockList.append(LineList)

    for b in range(37):
      pygame.draw.line(screen, self.lineColor, (0, 16*(a+1)), (800, 16*(a+1)), 1)


  def CheckBlock(self, screen):
    for x in range(50):
      for y in range(38):
        Block = BlockList[x][y]
        if self == Wind:
          if Block == "-":
            pygame.draw.rect(screen, skyBlue, [16*x+ 0.2, 16*y+ 0.2, 15.6, 15.6])

          elif Block == "road":
            pygame.draw.rect(screen, white, [16*x+ 0.2, 16*y+ 0.2, 15.6, 15.6])

          elif Block == "side":
            pygame.draw.circle(screen, white, (16*x+8, 16*y+8), 7.9)

#Wind region
skyBlue = (137, 189, 222)
white = (225, 225, 225)
white_2 = (220, 222, 222)

Wind = region(skyBlue, white, white_2)

#Water region
oceanBlue = (0, 105, 148)
clearBlue = (79,220,255)
blue_2 = (0,84,106)

Water = region(oceanBlue, clearBlue, blue_2)

#Rock region
rockColor = (90, 77, 65)
rockColor_2 = (160, 82, 45)
rockColor_3 = (139, 69, 19)

Rock = region(rockColor, rockColor_2, rockColor_3)

#Fire region
red_1 = (160, 82, 45)
red_2 = (134, 64, 64)
red_3 = (225, 0, 0)

Fire = region(red_1, red_2, red_3)

regions = [Wind, Water, Rock, Fire]






