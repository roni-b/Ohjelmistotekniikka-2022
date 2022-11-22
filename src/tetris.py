import pygame, random


BLOCK_SIZE = 50
height = 20
width = 10

def test():
    pass

#draw grid
grid = [pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE) for x in range(width) for y in range(height)]
shapes_positions = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

from pygame.locals import (
        K_DOWN,
        K_LEFT,
        K_RIGHT
    )

class NewShape(pygame.sprite.Sprite):
    def __init__(self):
        super(NewShape, self).__init__()
        #make surface
        #self.surf = pygame.Surface((75, 25))
        #choose color
        #self.surf.fill((255, 255, 255))
        #draw rect around
        #self.rect = self.surf.get_rect()

        

    def update(self, pressed_keys):
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > display_width:
            self.rect.right = display_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= display_height:
            self.rect.bottom = 0

display_height = height * BLOCK_SIZE
display_width = width * BLOCK_SIZE

display = pygame.display.set_mode((display_width, display_height))
pygame.mouse.set_visible(False)


shapes = [[pygame.Rect(x + width // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in shapes_positions]
shape_rect = pygame.Rect(0, 0, BLOCK_SIZE - 2, BLOCK_SIZE- 2)

shape = shapes[0]




#specify object
#shape = NewShape()
#group containing sprites and then drawing them
#shape_group = pygame.sprite.Group()
#shape_group.add(shape)
pygame.init()




running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    #shape.update(pressed_keys)
    display.fill((0, 0, 0))
    [pygame.draw.rect(display, (40, 40, 40), i_rect, 1) for i_rect in grid]

    for i in range(4):
        shape_rect.x = shape[i].x * BLOCK_SIZE
        shape_rect.y = shape[i].y * BLOCK_SIZE
        pygame.draw.rect(display, (255, 255, 255), shape_rect)

    #for entity in shape_group:
        #display.blit(entity.surf, entity.rect)
    

    pygame.display.update()
pygame.quit()

