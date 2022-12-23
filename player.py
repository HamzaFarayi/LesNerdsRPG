
class Player:
    def __init__(self, name, health, gold, experience, x, y):
        self.Name = name
        self.Health = health
        self.Experience = experience
        self.Gold = gold
        self.X = x
        self.Y = y

        self.sprite_index = 0

        self.horizontal_direction = None
        self.vertical_direction = None
