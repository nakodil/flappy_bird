import pygame  # весь?


class Tube(pygame.sprite.Sprite):
    """
    В Pygame Y растет вниз,
    X0, Y0 - это левый верхний угол
    """
    def __init__(self, screen_rect, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x_speed = 10
        self.can_score = True
        self.rect.right = screen_rect.right
        self.rect.bottom = screen_rect.bottom

    def update(self, screen_rect, game):
        if self.rect.left > screen_rect.left:
            self.rect.x -= self.x_speed
        else:
            game.score += 1  # Как отсюда и
            self.kill()
