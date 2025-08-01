import pygame
import time
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

def splash_page(screen):
    w,h = pygame.display.get_surface().get_size()
    font = pygame.font.SysFont(pygame.font.get_default_font(),80)
    splash_string = "Laget av Audun Steinkopf i pygame"
    text = font.render(splash_string,True, (255,255,255))
    (wt,ht) = font.size(splash_string)
    screen.blit(text,(w/2 - wt/2 ,h/2 - ht/2))
    pygame.display.update()
    time.sleep(3)

def main_menu(screen):
    #Definerer verdiene som brukes for å vise alternativene på hovedmenyen
    w,h = pygame.display.get_surface().get_size()
    Exit_height_adjust = h/3
    font = pygame.font.SysFont(pygame.font.get_default_font(),80)
    Exit = "Avslutt Spillet"
    text = font.render(Exit,True, (255,255,255))
    (wt,ht) = font.size(Exit)


    #Definerer og tegner selve alternativene
    avsluttfirkant2 = pygame.Rect(w/2 - wt *1.1, h/2 - ht*1.1 + Exit_height_adjust, wt * 2.2, ht * 2.2)
    pygame.draw.rect(screen,(255,255,255), avsluttfirkant2)
    avsluttfirkant1 = pygame.Rect(w/2 - wt, h/2 - ht + Exit_height_adjust, wt * 2, ht * 2)
    pygame.draw.rect(screen,(0,0,0), avsluttfirkant1)
    screen.blit(text,(w/2 - wt/2 ,h/2 - ht/2 + Exit_height_adjust))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (x,y) = pygame.mouse.get_pos()
            print(x,y)
            if avsluttfirkant1.collidepoint(x,y):
                return "quit"

        #Dersom ingenting annet blir valgt fortsetter løkken som før
    return "main_menu"



def run(screen):
    running = True
    splash_page(screen)
    state = "main_menu"

    while running:
        screen.fill((0,0,0))
        if state == "main_menu":
            choice = main_menu(screen)
            if choice != "main_menu":
                state = choice
        if state == "quit":
            running = False
        pygame.display.update()
    



main()