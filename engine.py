import pygame
import pygame.time


def should_keep_running():
    for event in pygame.event.get():
        if is_exit_event(event):
            return False
    return True


def is_exit_event(event):
    def esc_key_pressed(e):
        return e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE

    def exit_button_pressed(e):
        return e.type == pygame.QUIT

    return esc_key_pressed(event) or exit_button_pressed(event)


def write(screen, text):
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(text, 1, (255, 255, 0))
    screen.blit(label, (100, 100))


def main(main_loop):
    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.init()

    clock = pygame.time.Clock()

    while should_keep_running():
        clock.tick(30)
        pygame.display.flip()
        # print(clock.get_fps())
        main_loop(screen)
