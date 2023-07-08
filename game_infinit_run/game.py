import pygame
import random

WIDTH = 1200
HEIGHT = 600
SPEED = 10
GAME_SPEED = 10
GROUND_WIDTH = 2 * WIDTH
GROUND_HEIGHT = 30
PLACAR = 0
NIVEL = 1
RECORD = 0
RECORDISTA = ''

playerGroup = pygame.sprite.Group()
groundGroup = pygame.sprite.Group()
obstacleGroup = pygame.sprite.Group()
coinsGroup = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [pygame.image.load('sprites/Run__000.png').convert_alpha(),
                          pygame.image.load('sprites/Run__001.png').convert_alpha(),
                          pygame.image.load('sprites/Run__002.png').convert_alpha(),
                          pygame.image.load('sprites/Run__003.png').convert_alpha(),
                          pygame.image.load('sprites/Run__004.png').convert_alpha(),
                          pygame.image.load('sprites/Run__005.png').convert_alpha(),
                          pygame.image.load('sprites/Run__006.png').convert_alpha(),
                          pygame.image.load('sprites/Run__007.png').convert_alpha(),
                          pygame.image.load('sprites/Run__008.png').convert_alpha(),
                          pygame.image.load('sprites/Run__009.png').convert_alpha(),
                          ]
        self.image_fall = pygame.image.load('sprites/Fall.png').convert_alpha()
        self.image = pygame.image.load('sprites/Run__000.png').convert_alpha()
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.mask = pygame.mask.from_surface(self.image)
        self.current_image = 0

    def update(self, *args):
        def move_player(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                if self.rect[0] < WIDTH - 100:
                    self.rect[0] += GAME_SPEED
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                if self.rect[0] > 0:
                    self.rect[0] -= GAME_SPEED * 1.5
            self.current_image = (self.current_image + 1) % 10
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image, [100, 100])

        move_player(self)
        self.rect[1] += SPEED

        def fly(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] or key[pygame.K_UP]:
                if self.rect[1] > 0:
                    self.rect[1] -= 30
                self.image = pygame.image.load('sprites/Fly.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, [100, 100])

        fly(self)

        def fall(self):
            key = pygame.key.get_pressed()
            if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                self.image = self.image_fall
                self.image = pygame.transform.scale(self.image, [100, 100])

        fall(self)


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/ground.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = HEIGHT - GROUND_HEIGHT

    def update(self, *args):
        self.rect[0] -= GAME_SPEED


class Obstacles(pygame.sprite.Sprite):
    def __init__(self, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/Box.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.rect[0] = xpos
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[1] = HEIGHT - ysize

    def update(self, *args):
        self.rect[0] -= GAME_SPEED


class Coins(pygame.sprite.Sprite):
    def __init__(self, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/coin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [40, 40])
        self.rect = pygame.Rect(100, 100, 20, 20)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[0] = xpos
        self.rect[1] = HEIGHT - ysize

    def update(self, *args):
        self.rect[0] -= GAME_SPEED


def zerar_game():
    global SPEED
    global GAME_SPEED
    global PLACAR
    global NIVEL

    SPEED = 10
    GAME_SPEED = 10
    PLACAR = 0
    NIVEL = 1

    obstacleGroup.remove(obstacleGroup.sprites()[0:])
    playerGroup.remove(playerGroup.sprites()[0:])


def continuar_game():
    obstacleGroup.remove(obstacleGroup.sprites()[0:])
    playerGroup.remove(playerGroup.sprites()[0:])


def game(vida, gamer):
    global GAME_SPEED
    global SPEED
    global PLACAR
    global NIVEL

    def get_random_obstacles(xpos):
        size = random.randint(120, 600)
        box = Obstacles(xpos, size)
        return box

    def get_random_coins(xpos):
        size = random.randint(60, 500)
        coin = Coins(xpos, size)
        return coin

    def is_off_screen(sprite):
        return sprite.rect[0] < -(sprite.rect[2])

    def draw():
        playerGroup.draw(game_window)
        groundGroup.draw(game_window)
        obstacleGroup.draw(game_window)
        coinsGroup.draw(game_window)

    def update():
        groundGroup.update()
        playerGroup.update()
        obstacleGroup.update()
        coinsGroup.update()

    game_window = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('Coleta Moedas')

    BACKGROUND = pygame.image.load('sprites/background_03.jpg')
    BACKGROUND = pygame.transform.scale(BACKGROUND, [WIDTH, HEIGHT])

    player = Player()
    playerGroup.add(player)

    for i in range(2):
        ground = Ground(WIDTH * i)
        groundGroup.add(ground)

        coin = get_random_coins(WIDTH * i + 1000)
        coinsGroup.add(coin)

        obstacle = get_random_obstacles(WIDTH * i + 1000)
        obstacleGroup.add(obstacle)

    gameloop = True
    clock = pygame.time.Clock()

    pygame.init()

    while gameloop:
        try:
            global RECORD
            global RECORDISTA

            game_window.blit(BACKGROUND, (0, 0))
            font = pygame.font.SysFont('Arial', 30)

            text = font.render('Placar', True, [255, 255, 255])
            game_window.blit(text, [1100, 20])

            contador = font.render(f'{PLACAR}', True, [255, 255, 255])
            game_window.blit(contador, [1125, 50])

            text_nivel = font.render('Nível', True, [255, 255, 255])
            game_window.blit(text_nivel, [1000, 20])

            contador_nivel = font.render(f'{int(NIVEL)}', True, [255, 255, 255])
            game_window.blit(contador_nivel, [1025, 50])

            text_vida = font.render('Vidas', True, [255, 255, 255])
            game_window.blit(text_vida, [900, 20])

            contador_vida = font.render(f'{vida}', True, [255, 255, 255])
            game_window.blit(contador_vida, [925, 50])

            text_record = font.render(f'Record', True, [255, 255, 255])
            game_window.blit(text_record, [20, 20])

            contador_record = font.render(f'{RECORDISTA}', True, [255, 255, 255])
            game_window.blit(contador_record, [20, 50])

            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

            if is_off_screen(groundGroup.sprites()[0]):
                groundGroup.remove(groundGroup.sprites()[0])
                newGround = Ground(WIDTH - 40)
                groundGroup.add(newGround)

            if is_off_screen(obstacleGroup.sprites()[0]):
                obstacleGroup.remove(obstacleGroup.sprites()[0])
                newObstacle = get_random_obstacles(WIDTH * 1.5)
                obstacleGroup.add(newObstacle)
                newCoin = get_random_coins(WIDTH * 2)
                newCoin1 = get_random_coins(WIDTH * 2.2)
                newCoin2 = get_random_coins(WIDTH * 2.4)
                newCoin3 = get_random_coins(WIDTH * 2.6)
                newCoin4 = get_random_coins(WIDTH * 2.8)
                coinsGroup.add(newCoin)
                coinsGroup.add(newCoin1)
                coinsGroup.add(newCoin2)
                coinsGroup.add(newCoin3)
                coinsGroup.add(newCoin4)

            if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                SPEED = 0
            else:
                SPEED = 10

            if pygame.sprite.groupcollide(playerGroup, coinsGroup, False, True):
                PLACAR += 1
                if PLACAR > RECORD:
                    RECORD = PLACAR
                    RECORDISTA = f'{gamer}  {RECORD} pontos'

            if PLACAR % 5 == 0 and PLACAR != 0:
                incremento = 0.02
                GAME_SPEED += incremento
                NIVEL += incremento

            if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                break

            update()
            draw()
            pygame.display.update()
        except:
            pass

    return f'VOCÊ PERDEU! Fez um total de {PLACAR} de ponto(s), chegou no nível {int(NIVEL)}.'
