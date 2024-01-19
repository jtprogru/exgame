import time

import pygame
from random import randint

# Инициализация
pygame.init()
# Настройки игры
FPS = 60  # Скорость отрисовки влияет на скорость игры
WIDTH, HEIGHT = 400, 600  # Ширина и высота окна

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save the frog")
clock = pygame.time.Clock()
running = True


# Классы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Frog.png")
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 80))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Mask.png")
        self.rect = self.image.get_rect(center=(randint(40, WIDTH - 40), -70))

    def update(self):
        self.rect.y += 7
        if self.rect.top > HEIGHT:
            self.rect.center = (randint(40, WIDTH - 40), -70)


def game_over():
    """
    Функция окончания игры
    :return: None
    """
    global running
    running = False
    screen.fill((255, 0, 0))
    font = pygame.font.SysFont(None, 48)
    text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))


def game_run():
    """
    Функция запуска игры
    :return: None
    """
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        if pygame.sprite.collide_rect(player, enemy):
            game_over()
        else:
            screen.fill((120, 180, 220))
            all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    # Инициализация игры
    player = Player()
    enemy = Enemy()
    all_sprites = pygame.sprite.Group(player, enemy)
    # Запуск игры
    game_run()
    # Завершение работы с задержкой в 2 секунды
    time.sleep(2)
    pygame.quit()
