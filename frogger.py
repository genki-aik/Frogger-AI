import pygame

WIDTH, HEIGHT = 760, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FroggerAI")
FPS = 30


WHITE = (255, 255, 255)

def draw():
    WIN.fill(WHITE)

    pygame.display.update()


def main():

    clock = pygame.time.Clock()
    run = True
    while(run):

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()


if __name__ == "__main__":
    main()