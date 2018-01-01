import pygame
import sys
from pygame.locals import *
from spirograph import Circle


# TODO determine when a graph is done
# TODO make it possible to parameterise
# TODO insta-done button
# TODO colours

def main():
    pygame.init()

    clock = pygame.time.Clock()
    fps = 180

    res = wid, hi = 1440, 870
    d_surf = pygame.display.set_mode(res)

    outer_c = Circle(240, is_active=True, point=100)
    outer_c.set_position(wid // 2, hi // 2)

    inner_c = Circle(132, is_active=True, point=100)
    inner_c.set_position(outer_c.x, outer_c.y - outer_c.radius + inner_c.radius)

    outer_c.add_child(inner_c)

    while True:

        outer_c.inc_angle(1)
        p_x, p_y = inner_c.get_point_position()
        d_surf.set_at((int(p_x), int(p_y)), (255, 255, 255))

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == 27:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    main()
