import pygame
import random
from rabbit import Rabbit
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

envSize = (50, 50)
cellSize = 20

array = []
rabbits = []

rabbitAmount = 10


timer = 0


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
            pygame.draw.rect(window, color, (x*cellSize, y*cellSize, cellSize, cellSize))

    for rabbit in rabbits:
        rabbit.draw(pygame, window, cellSize)
    if timer >= 0.3:
        rabbitsToRemove = []
        for rabbit in rabbits:
            isDead = rabbit.update()
            if isDead:
                rabbitsToRemove.append(rabbit)

        for r in rabbitsToRemove:
            rabbits.remove(r)
        timer = 0

        print("Population: " + str(Rabbit.population))


for x in range(envSize[0]):
    row = []
    for y in range(envSize[1]):
        noise_val = noise([x/envSize[0]*5, y/envSize[1]*5])
        if noise_val < -.1:
            row.append(0)
        elif noise_val < 0:
            row.append(1)
        else:
            row.append(2)
    array.append(row)

for i in range(rabbitAmount):
    rabbit = Rabbit([0, i])
    rabbits.append(rabbit)

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
