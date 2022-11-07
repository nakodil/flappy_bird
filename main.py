import pygame
from random import randint
from bird import Bird
from tube import Tube


class App:
    """
    TODO: все размеры спрайтов считать от размеров экрана!
    Размеры экрана учитывают масштаб интерфейса в 10 Винде
    2560 * 0.8 = 2048
    1440 * 0.8 = 1152
    """
    def __init__(self, fullscreen=False) -> None:
        pygame.init()
        screen_sizes = pygame.display.get_desktop_sizes()
        if fullscreen:
            self.screen_width = screen_sizes[0][0]
            self.screen_height = screen_sizes[0][1]
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN) 
        else:
            self.screen_width = int(screen_sizes[0][0] * 0.8)  # нужно место для интерфейса окна (заголовка, кнопок, ...) 
            self.screen_height = int(screen_sizes[0][1]  * 0.8)
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.bird = Bird(self.screen_rect, width=100, height=100, color=(255, 0, 0))
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bird)
        self.is_running = False
        self.main_loop()

    def main_loop(self):
        self.is_running = True
        self.score = 0
        MAKE_TUBE = pygame.event.custom_type()  # MAKE_TUBE:int !
        pygame.time.set_timer(MAKE_TUBE, 1000)

        while self.is_running:

            # заливаем экран, иначе изображения рисует своей поверхностью полосы
            self.screen.fill((255, 255, 255))
            
            # рисуем все спрайты
            self.all_sprites.draw(self.screen)
 
            # проходим по событиям
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:  # эту клавишу нельзя зажать
                    if event.key == pygame.K_ESCAPE:
                        self.is_running = False
                    else:
                        self.bird.jump(20)
                if event.type == MAKE_TUBE:
                    self.make_tube()
                
            # собираем нажатия клавиш
            keys = pygame.key.get_pressed()
    
            # эту клавишу можно зажимать
            if keys[pygame.K_q]:
                pass

            # дефолтный метод каждого спрайта
            self.all_sprites.update(screen_rect=self.screen_rect, game=self)

            # у дисплея есть буфер, как бы обратная сторона листа, вся графика сначала рисуется на ней,
            # а потом flip переворачивает лист, таким способом графика буферизируется
            pygame.display.flip()

            # ожидание, цикл выполняется не чаще FPS раз в секунду
            self.clock.tick(self.fps)

        pygame.quit()

    def make_tube(self):
        tube = Tube(
            midright=self.screen_rect.midright,
            centery=self.screen_rect.centery + randint(-150, 150),
            width=10,
            height=500
        )
        self.all_sprites.add(tube)


if __name__ == "__main__":
    App()