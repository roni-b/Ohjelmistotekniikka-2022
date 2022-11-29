import os
import random
import pygame

wd = os.getcwd()
clock = pygame.time.Clock()

BLOCK_SIZE = 50
HEIGHT = 20
WIDTH = 10
DISPLAY_HEIGHT = BLOCK_SIZE * HEIGHT
DISPLAY_WIDTH = BLOCK_SIZE * WIDTH

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.mouse.set_visible(False)


grid = [pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE) for x in range(WIDTH) for y in range(HEIGHT)]

from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP


class NewShape(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        next_shape = random.randint(1, 7)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'shapes', str(next_shape)+'.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 105))
        self.rect = self.image.get_rect()

    def input(self, pressed_keys):
        if pressed_keys[K_DOWN] and self.rect.bottom < DISPLAY_HEIGHT and collision() is False:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] and self.rect.bottom < DISPLAY_HEIGHT and collision() is False:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.bottom < DISPLAY_HEIGHT and collision() is False:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_UP] and self.rect.bottom <= DISPLAY_HEIGHT:
            self.rotate(self.image.get_width(), self.image.get_height())

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > DISPLAY_WIDTH:
            self.rect.right = DISPLAY_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= DISPLAY_HEIGHT:
            self.rect.bottom = DISPLAY_HEIGHT
            shapes.add(DroppedShapes(self.image, self.rect))
            self.give_new_shape()
    def rotate(self, rect_x, rect_y):
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(center = self.image.get_rect(center = (rect_x, rect_y)).center)

    def drop(self):
        if not collision():
            self.rect.move_ip(0, 1)
        else:
            self.rect.move_ip(0, -3)
            shapes.add(DroppedShapes(self.image, self.rect))
            self.give_new_shape()


    def update(self, pressed_keys):
        self.input(pressed_keys)
        self.drop()

    def give_new_shape(self):
        next_shape = random.randint(1, 7)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'shapes', str(next_shape)+'.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 105))
        self.rect = self.image.get_rect()

class DroppedShapes(pygame.sprite.Sprite):
    def __init__(self, image, rect):
        super().__init__()
        self.image = image
        self.rect = rect

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([600,1200])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

class Grid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

shape = pygame.sprite.GroupSingle()
shape.add(NewShape())

shapes = pygame.sprite.Group()

background = pygame.sprite.Group()
background.add(Background())

all_sprites = pygame.sprite.Group()
all_sprites.add(NewShape())


pygame.init()

def collision():
    if pygame.sprite.spritecollide(shape.sprite, shapes, False):
        return True
    return False


def loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()
        display.fill((0, 0, 0))
        [pygame.draw.rect(display, (40, 40, 40), i_rect, 1) for i_rect in grid]
        shape.update(pressed_keys)
        shape.draw(display)
        shapes.draw(display)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

loop()
