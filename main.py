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
        self.velocidade_jogador = 500  # Define a velocidade do player
        self.jogador_rect = self.jogador.get_frect(
            center=(
                self.width / 2,
                self.height / 2,
            )  # Cria Rect da imagem no centro da tela
        )
        self.running = True  # Variavel de controle de fim de jogo/fechar a janela
        self.run()  # Inicializa a funçao run, para rodar o jogo

    def run(self):
        while self.running:  # Loop do jogo
            # Verifica se tentou fechar a janela, caso sim, ela fecha
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            dt = (
                self.clock.tick(144) / 1000
            )  # Variavel Delta Time, usada para funções de movimento e para limitar o fps do jogo (dentro do loop para atualizar a taxa de fps junto com o loop)

            self.mouse()  # Chama a função
            self.display_surface.fill("gray21")
            self.display_surface.blit(self.jogador, self.jogador_rect)
            self.input(dt)
            self.anti_bobby_collision()
            pygame.display.update()

    def input(self, dt):  # Input WASD Básico
        keys = pygame.key.get_pressed()
        x_direction = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        y_direction = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.jogador_rect.centery += self.velocidade_jogador * dt * x_direction
        self.jogador_rect.centerx += self.velocidade_jogador * dt * y_direction

    def mouse(self):
        pygame.mouse.set_pos(
            self.jogador_rect.x, self.jogador_rect.y
        )  # Pega a posição do mouse
        pygame.mouse.set_visible(False)  # Define o mouse como invisível
        self.clicado = (
            pygame.mouse.get_just_pressed()
        )  # variavel de entrada e saida dos clicks do mouse
        if self.clicado[0]:
            print("Left")
        if self.clicado[2]:
            print("Right")

    def anti_bobby_collision(self):  # Define a colisão do antibobby
        if self.jogador_rect.bottom > self.height:
            self.jogador_rect.bottom = self.height

        if self.jogador_rect.top < 0:
            self.jogador_rect.top = 0

        if self.jogador_rect.right > self.width:
            self.jogador_rect.right = self.width

        if self.jogador_rect.left < 0:
            self.jogador_rect.left = 0


Game()
