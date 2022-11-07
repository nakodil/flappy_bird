import pygame  # весь?


class Tube(pygame.sprite.Sprite):
    """
    В Pygame Y растет вниз,
    X0, Y0 - это левый верхний угол
    """
    def __init__(
        self,
        midright=100,
        centery=100,
        width=100,
        height=100
    ):
        super().__init__()
        self.image = pygame.image.load("assets/tube.png")
        # self.image = pygame.transform.scale(self.image, (50, 400))
        self.rect = self.image.get_rect()
        self.x_speed = 10
        self.rect.midright = midright,
        self.rect.centery = centery

    def update(self, screen_rect, game):
        if self.rect.right > screen_rect.left:
            self.rect.x -= self.x_speed
        else:
            game.score += 1  # Как отсюда изменить счет?
            self.kill()
