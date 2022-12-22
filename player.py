
class Player:
    def __init__(self, name, health, gold, experience, x, y):
        self.Name = name
        self.Health = health
        self.Experience = experience
        self.Gold = gold
        self.X = x
        self.Y = y

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
