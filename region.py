class region:
  def __init__(self, mainColor, mainColor_2, lineColor, number):
    self.mainColor = mainColor
    self.mainColor_2 = mainColor_2
    self.lineColor = lineColor
    
#Wind region
skyBlue = (137, 189, 222)
white = (225, 225, 225)
white_2 = (220, 222, 222)

region_wind = region(skyBlue, white, white_2, 0)

#Water region
oceanBlue = (0, 105, 148)
clearBlue = (79,220,255)
blue_2 = (0,84,106)

region_water = region(oceanBlue, clearBlue, blue_2, 1)

#Rock region
rockColor = (90, 77, 65)
rockColor_2 = (160, 82, 45)
rockColor_3 = (139, 69, 19)

region_rock = region(rockColor, rockColor_2, rockColor_3, 2)

#Fire region
red_1 = (160, 82, 45)
red_2 = (134, 64, 64)
red_3 = (225, 0, 0)

region_fire = region(red_1, red_2, red_3, 3)

#Boss region
purple = (101, 32, 108)
black = (0, 0, 0)

region_boss = region(purple, black, black, 4)

regions = [region_wind, region_water, region_rock, region_fire, region_boss]






