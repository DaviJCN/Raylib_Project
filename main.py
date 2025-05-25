import pygame

class Game:

    def __init__():

        pygame.init()
        pygame.display.set_mode((800, 600))
        clock = pygame.Clock()
    
    def run():
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type  == pygame.QUIT:
                    loop = False
                