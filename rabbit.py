import random


class Rabbit:
    population = 0

    def __init__(self, pos, speed=10, ran=10):
        Rabbit.population += 1
        self.values = {
            "thirst": 0,
        }
        self.genes = {
            "speed": speed,
            "range": ran
        }

        self.pos = pos

    def update(self):
        self.addValues()
        return self.checkIfDead()

    def draw(self, pygame, window, cellSize):
        pygame.draw.rect(window, (143, 86, 20),
                         (self.pos[0]*cellSize + cellSize / 4,
                          self.pos[1]*cellSize + cellSize / 4,
                          cellSize / 2,
                          cellSize / 2))

    def addValues(self):
        self.values["thirst"] += random.randint(0, 5)

    def checkIfDead(self):
        for (key, value) in self.values.items():
            if value >= 100:
                print(key, value)
                Rabbit.population -= 1
                return True
                del self
            else:
                return False
