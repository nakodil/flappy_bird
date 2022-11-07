import pygame  # весь?


class Bird(pygame.sprite.Sprite):
    """
    В Pygame Y растет вниз,
    X0, Y0 - это левый верхний угол

    # TODO: сделать задержку следующего прыжка
    """
    def __init__(self, screen_rect, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        self.y_speed = 10
        self.can_jump = True
        self.is_falling = True

    def update(self, screen_rect, game):
        # падение
        if self.rect.bottom < screen_rect.bottom and self.is_falling:
            self.rect.y -= self.y_speed
            self.y_speed -= 1
        
        # столкновение с низом экрана
        if self.rect.bottom >= screen_rect.bottom and self.is_falling:
            self.is_falling = False
            self.rect.bottom = screen_rect.bottom - 1  # Отлепляем от низ птицы от низа экрана, а то не прыгнет
        
        # столкновение с верхом экрана
        if self.rect.top <= screen_rect.top:
            self.can_jump = False
            self.rect.top = screen_rect.top + 1
            self.can_jump = True

    def jump(self, power):
        if self.can_jump:
            self.is_falling = True
            self.y_speed = power
