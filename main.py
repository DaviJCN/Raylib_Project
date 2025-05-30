import pygame
from os.path import join


class Game:
    def __init__(self):
        pygame.init()  # Inicializa os modulos do pygame
        self.width = 800
        self.height = 600
        pygame.display.set_caption('Pedro, Morra!') # Nome da janela
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
        self.jogador_direcao = pygame.Vector2()
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
            self.circle_anti_bobvy()
            pygame.display.update()
            
    def input(self, dt):  # Input WASD Básico
        keys = pygame.key.get_pressed()
        self.jogador_direcao[0] = (
            int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        )  # Se o jogador vai direita a direção é 1, se vai pra esquerda é -1, parado é 0
        self.jogador_direcao[1] = int(keys[pygame.K_s]) - int(
            keys[pygame.K_w]
        )  # Mesma coisa, so que pro eixo y
        self.jogador_direcao = (
            self.jogador_direcao.normalize()
            if self.jogador_direcao
            else self.jogador_direcao
        )  # "Normaliza" a direção do jogador, fazendo o numero ficar entre 1 e -1, para nao alterar a velocidade do mesmo
        self.jogador_rect.centerx += (
            self.velocidade_jogador * dt * self.jogador_direcao[0]
        )  # O jogador so mexe se a direção for diferente de 0
        self.jogador_rect.centery += (
            self.velocidade_jogador * dt * self.jogador_direcao[1]
        )

    def mouse(self):  # Rastreia o mouse
        mouse_x, mouse_y = (
            pygame.mouse.get_pos()
        )  # Obtém a posição atual do mouse a cada frame
        print(mouse_x, mouse_y)  # Escreve a posição do mouse
        pygame.mouse.set_visible(True)  # Define o mouse como invisível
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

    def circle_anti_bobvy(self):
        circle = pygame.draw.circle(self.display_surface, (255, 255, 255), self.jogador_rect.center , radius=38, width=1)
        
        
        


Game()
