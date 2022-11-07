import pygame  # весь?


class Bird(pygame.sprite.Sprite):
    """
    В Pygame Y растет вниз,
    X0, Y0 - это левый верхний угол
    """
    def __init__(self, screen_rect, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        self.y_speed = 10
        self.is_jumping = True

    def update(self, screen_rect, game):
        # падение, если низ птицы не касается низа экрана
        if self.rect.bottom < screen_rect.bottom and self.is_jumping:
            self.rect.y -= self.y_speed
            self.y_speed -= 1
        if self.rect.bottom >= screen_rect.bottom and self.is_jumping:
            self.is_jumping = False
            self.rect.bottom = screen_rect.bottom - 1  # Отлепляем от низ птицы от низа экрана, а то не прыгнет

    def jump(self, power):
            self.is_jumping = True
            self.y_speed = power
