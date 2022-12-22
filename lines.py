import pygame
  
lineList = [] #tile[x][y] represents the tile at (x, y)

class line:
  def drawLine(screen, currentRegion):
    for a in range(49):
      list_x = []

      for b in range(37):
        list_x.append("-")

      lineList.append(list_x)

      if a <= 48: #vetrical line
        pygame.draw.line(screen, currentRegion.lineColor, (16*(a+1), 0), (16*(a+1), 608))
        
      if a <= 36: #horizontal line
        pygame.draw.line(screen, currentRegion.lineColor, (0, 16*(a+1)), (800, 16*(a+1)))

      
