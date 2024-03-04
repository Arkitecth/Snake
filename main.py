import pygame
from pygame.locals import *

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20


class Snake:
    def __init__(self) -> None:
        self.body = [Rect(WIDTH / 2, HEIGHT / 2, CELL_SIZE, CELL_SIZE),
                     Rect((WIDTH / 2) + CELL_SIZE,
                          (HEIGHT / 2), CELL_SIZE, CELL_SIZE),
                     Rect((WIDTH / 2) + 40, (HEIGHT / 2), CELL_SIZE, CELL_SIZE)]
        self.direction = (0, 0)

    def draw(self, screen):
        for parts in self.body:
            pygame.draw.rect(screen, "blue", parts, 1)

    def extend(self):
        pass

    def move_snake(self, direction):
        if self.direction != (0, 0):
            head = self.body[-1]
            new_rect = head.move(
                direction[0] * CELL_SIZE, direction[1] * CELL_SIZE)
            self.body.append(new_rect)
            self.body.pop(0)  # Pop tail

    def move(self):
        keys = pygame.key.get_pressed()
        self.move_snake(self.direction)
        if keys[pygame.K_LEFT] and self.direction != (1, 0):
            self.direction = (-1, 0)
        if keys[pygame.K_RIGHT] and self.direction != (-1, 0):
            self.direction = (1, 0)
        if keys[pygame.K_DOWN] and self.direction != (0, -1):
            self.direction = (0, 1)
        if keys[pygame.K_UP] and self.direction != (0, 1):
            self.direction = (0, -1)


class Apple:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.apple = pygame.rect.Rect(self.x, self.y, 10, 10)

    def draw(self, screen):
        pygame.draw.rect(screen, 'red', self.apple)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    snake = Snake()
    apple = Apple(100, 100)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        snake.draw(screen)
        apple.draw(screen)
        snake.move()
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()


main()
