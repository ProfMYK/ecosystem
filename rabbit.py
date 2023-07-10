import random


class Rabbit:
    population = 0

    def __init__(self, pos, speed=10, ran=10):
        Rabbit.population += 1
        self.values = {
            "thirst": 0,
            "health": 0
        }

        self.genes = {
            "speed": speed,
            "range": ran
        }

        self.pos = pos
        self.currentPath = []

    def update(self, array):
        self.addValues()
        big = max(self.values.values())
        if big == self.values["thirst"]:
            if len(self.currentPath) > 0:
                self.pos = self.getNexPosition()
            else:
                water = self.findClosestWater(array)
                self.currentPath = self.find_line_path(water)
        elif big == self.values["hunger"]:
            pass
        return self.checkIfDead()

    def draw(self, pygame, window, cellSize):
        pygame.draw.rect(window, (143, 86, 20),
                         (self.pos[0]*cellSize + cellSize / 4,
                          self.pos[1]*cellSize + cellSize / 4,
                          cellSize / 2,
                          cellSize / 2))

    def getNexPosition(self):
        last = self.currentPath[0]
        self.currentPath.remove(last)
        return last

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

    def findClosestWater(self, array):
        closest_distance = float('inf')
        closest_position = None

        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] == 0:
                    distance = abs(i - self.pos[0]) + abs(j - self.pos[1])

                    if distance <= self.genes["range"] and distance < closest_distance:
                        closest_distance = distance
                        closest_position = (i, j)

        if closest_position is None:
            adjacent_positions = [(self.pos[0] - 1, self.pos[1]), (self.pos[0] + 1, self.pos[1]),
                                  (self.pos[0], self.pos[1] - 1), (self.pos[0], self.pos[1] + 1)]
            valid_adjacent_positions = [
                pos for pos in adjacent_positions if 0 <= pos[0] < len(array) and 0 <= pos[1] < len(array[pos[0]])]
            closest_position = random.choice(valid_adjacent_positions)

        return closest_position

    def findClosestPosition(self, foodPositions, array):
        closestDistance = 99999999
        closest_position = None

        for position in foodPositions:
            distance = abs(position[0] - self.pos[0]) + abs(position[1] - self.pos[1])

            if distance < closestDistance:
                closestDistance = distance
                closest_position = position

        if closest_position is None:
            adjacent_positions = [(self.pos[0] - 1, self.pos[1]), (self.pos[0] + 1, self.pos[1]),
                                  (self.pos[0], self.pos[1] - 1), (self.pos[0], self.pos[1] + 1)]
            valid_adjacent_positions = [
                pos for pos in adjacent_positions if 0 <= pos[0] < len(array) and 0 <= pos[1] < len(array[pos[0]])]
            closest_position = random.choice(valid_adjacent_positions)

        return closest_position

    def find_line_path(self, target_pos):
        x1, y1 = self.pos
        x2, y2 = target_pos
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1
        err = dx - dy

        line_path = []
        while x1 != x2 or y1 != y2:
            line_path.append((x1, y1))
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

        line_path.append((x1, y1))
        return line_path[1:]
