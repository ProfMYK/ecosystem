class Food:
    def __init__(self, pos, health=100):
        self.pos = pos
        self.health = health

    def draw(self, window, pygame, color, cellSize):
        pygame.draw.rect(window, color,
                         (self.pos[0]*cellSize + cellSize / 4,
                          self.pos[1]*cellSize + cellSize / 4,
                          cellSize / 2,
                          cellSize / 2))
