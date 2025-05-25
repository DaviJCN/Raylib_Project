import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((800, 600))
        self.clock = pygame.Clock()
        loop = True
        self.run(loop)

    def run(self, loop):
        dt = self.clock.tick() / 1000
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False


Game()
