import pygame
import sys
from pygame.locals import *
import random


def main():
    pygame.init()

    clock = pygame.time.Clock()
    fps = 60

    res = wid, hi = 1440, 870
    d_surf = pygame.display.set_mode(res)

    while True:

        # d_surf.fill((0, 0, 0))

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == 27:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    main()