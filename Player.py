class Player:
    def __init__(self, name, color):
        self.turn = 0
        self.won = False
        self.score = 0
        self.color = color
        self.name = name
        self.pieces = {
            'QB': 1, #Queen Bee
            'S': 2, #spider
            'B': 2,#Beetle
            'G': 3,#Grasshopper
            'A': 3,#Ant
        }