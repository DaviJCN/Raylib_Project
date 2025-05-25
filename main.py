import pygame
from os.path import join


class Game:
    def __init__(self):
        pygame.init()  # Inicializa os modulos do pygame
        self.width = 800
        self.height = 600
        self.display_surface = pygame.display.set_mode(
            (self.width, self.height)
        )  # Cria a janela principal do jogo
        self.clock = pygame.Clock()
        self.jogador = pygame.image.load(
            join("anti_bobby.png")
        )  # Carrega a imagem do anti_bobby
        self.jogador = pygame.transform.scale(
            self.jogador, (60, 60)
        )  # Aumenta a imagem para 60x60
        self.jogador_rect = self.jogador.get_frect(
            center=(
                self.width / 2,
                self.height / 2,
            )  # Cria Rect da imagem no centro da tela
        )
        self.running = True  # Variavel de controle de fim de jogo/fechar a janela
        self.run()  # Inicializa a funçao run, para rodar o jogo

    def run(self):
        dt = (
            self.clock.tick(60) / 1000
        )  # Variavel Delta Time, usada para funções de movimento e para limitar o fps do jogo
        self.mouse_motion()
        while self.running:  # Loop do jogo
            # Verifica se tentou fechar a janela, caso sim, ela fecha
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.display_surface.fill("blue")
            self.display_surface.blit(self.jogador, self.jogador_rect)
            self.input(dt)
            pygame.display.update()

    def input(self, dt):  # Input WASD Básico
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.jogador_rect.centery -= 1
        if keys[pygame.K_s]:
            self.jogador_rect.centery += 1
        if keys[pygame.K_a]:
            self.jogador_rect.centerx -= 1
        if keys[pygame.K_d]:
            self.jogador_rect.centerx += 1
    
    def mouse_motion(self): # Função mouse
        position = pygame.mouse.set_pos(self.jogador_rect.x, self.jogador_rect.y) # Pega a posição do mouse
        pygame.mouse.set_visible(False) # define com invisível
        
        

Game()
