import pygame
def main():
    __init__()#initialiserer pygame
    screen = get_screen()#Lager lerretet vi kan tegne spillet på
    run(screen)#kjører selve spillet

def __init__():
    pygame.init()
    pygame.display.set_caption("Andromeda Expedition")

def get_screen():
    stats = pygame.display.Info()
    screen_w = stats.current_w
    screen_h = stats.current_h
    screen = pygame.display.set_mode((screen_w,screen_h), pygame.FULLSCREEN)
    return screen


def run(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
    



main()