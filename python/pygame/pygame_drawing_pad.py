# Small program to help with testing objects being drawn in pygame framework
import pygame
from pygame.locals import *
import sys

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1000
FRAMES_PER_SECOND = 30
GRAY = (230, 230, 230)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)
PURPLE = (255, 0, 255)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(BLACK)

#    standard window parameters
    pygame.draw.line(window, GRAY, (0, 500), (1500, 500), 1)
    pygame.draw.line(window, GRAY, (750, 0), (750, 1000), 1)
    font = pygame.font.SysFont(None, 24)
    img = font.render('X=0/Y=500', True, GRAY)
    window.blit(img, (0, 500))
    img = font.render('X=750/Y=500', True, GRAY)
    window.blit(img, (750, 500))
    img = font.render('X=1500/Y=500', True, GRAY)
    window.blit(img, (1390, 500))
    img = font.render('X=750/Y=0', True, GRAY)
    window.blit(img, (750, 9))
    img = font.render('X=750/Y=1000', True, GRAY)
    window.blit(img, (750, 980))

    # 10 - Draw all window elements
    # Draw a box
#    pygame.draw.line(window, BLUE, (20, 20), (60, 20), 4)  # top
#    pygame.draw.line(window, BLUE, (20, 20), (20, 60), 4)  # left
#    pygame.draw.line(window, BLUE, (20, 60), (60, 60), 4)  # right
#    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4)  # bottom

    # Draw an X in the box
#    pygame.draw.line(window, BLUE, (20, 20), (60, 60), 1)
#    pygame.draw.line(window, BLUE, (20, 60), (60, 20), 1)

    # Draw a filled circle and an empty circle
#    pygame.draw.circle(window, GREEN, (400, 50), 30, 2)  # 2 pixel edge

    # Draw a filled rectangle and an empty rectangle
#    pygame.draw.rect(window, RED, (250, 150, 100, 50), 0)  # filled
#    pygame.draw.rect(window, RED, (400, 150, 100, 50), 1)  # 1 pixel edge

    # Draw a filled ellipse and an empty ellipse
#    pygame.draw.ellipse(window, YELLOW, (250, 250, 80, 40), 0)  # filled
#    pygame.draw.ellipse(window, YELLOW, (400, 250, 80, 40), 2)  # 2 pixel edge

    # Draw a six-sided polygon
#    pygame.draw.polygon(window, TEAL, ((240, 350), (350, 350),
#                                       (410, 410), (350, 470),
#                                       (240, 470), (170, 410)))

    # Draw an arc
#    pygame.draw.arc(window, BLUE, (20, 400, 100, 100), 0, 2, 5)

    # Draw anti-aliased lines: a single line, then a list of points
#    pygame.draw.aaline(window, RED, (500, 400),  (540, 470), 1)
#    pygame.draw.aalines(window, BLUE, True,
#                        ((580, 400), (587, 450),
#                         (595, 460), (600, 444)), 1)

    ev = pygame.event.get()

    if event.type == pygame.MOUSEBUTTONUP:
        x, y = pygame.mouse.get_pos()

        img = font.render('X =' + str(x), True, GREEN)
        window.blit(img, (x+10, y+10))

        img = font.render('Y =' + str(y), True, GREEN)
        window.blit(img, (x+25, y+25))

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
