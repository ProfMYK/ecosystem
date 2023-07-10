import pygame
import random
from rabbit import Rabbit
from food import Food
from perlin_noise import PerlinNoise

noise = PerlinNoise()

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

BLUE = (22, 159, 245)
GREEN = (101, 219, 61)
YELLOW = (250, 216, 177)
PURPLE = (209, 19, 136)

envSize = (20, 20)
cellSize = 50

array = []
rabbits = []
foods = []

rabbitAmount = 5
foodAmount = 20

timer = 0


def findRandomPosition(array):
    positions = []

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 1 or array[i][j] == 2:
                positions.append((i, j))

    if positions:
        return random.choice(positions)
    else:
        return None


def update(dt, window):
    global timer
    timer += dt

    for x in range(envSize[0]):
        for y in range(envSize[1]):
            val = array[x][y]
            color = BLUE
            if val == 1:
                color = YELLOW
            elif val == 2:
                color = GREEN
            elif val == 3:
                color = (0, 0, 0)
            pygame.draw.rect(window, color, (x*cellSize, y*cellSize, cellSize, cellSize))

    for rabbit in rabbits:
        rabbit.draw(pygame, window, cellSize)
    for food in foods:
        food.draw(window, pygame, PURPLE, cellSize)

    for rabbit in rabbits:
        rabbit.draw(pygame, window, cellSize)
    if timer >= 2:
        rabbitsToRemove = []
        for rabbit in rabbits:
            isDead = rabbit.update(array)
            if isDead:
                rabbitsToRemove.append(rabbit)

        for r in rabbitsToRemove:
            rabbits.remove(r)
        timer = 0

        print("Population: " + str(Rabbit.population))


for x in range(envSize[0]):
    row = []
    for y in range(envSize[1]):
        noise_val = noise([x/envSize[0]*2, y/envSize[1]*2])
        if noise_val < -.1:
            row.append(0)
        elif noise_val < 0:
            row.append(1)
        else:
            row.append(2)
    array.append(row)

for i in range(rabbitAmount):
    rabbit = Rabbit(findRandomPosition(array))
    rabbits.append(rabbit)

for i in range(foodAmount):
    food = Food(findRandomPosition(array))
    foods.append(food)

run = True
while run:
    delta_time = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((60, 60, 60))

    update(delta_time, screen)
    if Rabbit.population == 0:
        run = False

    pygame.display.update()


pygame.quit()
