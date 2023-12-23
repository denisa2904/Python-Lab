import pygame
from hexagon_matrix import draw_hexagon_matrix


LIGHT_GREEN = (43, 175, 98)

width, height = 900, 700


def main():
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Trap the Mouse")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(LIGHT_GREEN)
        draw_hexagon_matrix(screen, 11, 11)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
