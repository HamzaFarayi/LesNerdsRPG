import pygame

BlockList = []
class region:
  def __init__(self, mainColor, mainColor_2, lineColor):
    self.mainColor = mainColor
    self.mainColor_2 = mainColor_2
    self.lineColor = lineColor


  def DrawLines(self, screen):
    for a in range(37):
      pygame.draw.line(screen, self.lineColor, (0, 16*(a+1)), (800, 16*(a+1)), 1)
      horizontalLineList = []
      for b in range(50):
        horizontalLineList.append("-")

    for b in range(50):
      pygame.draw.line(screen, self.lineColor, (16*(b+1), 0), (16*(b+1), 608), 1)

      BlockList.append(horizontalLineList)


  def CheckBlock(self, screen, CurrentRegion):
    for x in range(37):
      for y in range(50):
        if CurrentRegion == Wind:
          if BlockList[x][y] == "-":
            pygame.draw.rect(screen, skyblue, []
      

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





