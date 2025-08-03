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

def firkant(koord_vr, koord_lr, bredde, høyde, screen, farge):
    firkanten = pygame.Rect(koord_vr, koord_lr, bredde, høyde)
    pygame.draw.rect(screen,farge, firkanten)
    return firkanten

def splash_text(screen, text_string, Chosen_font = "Arial",font_size = 80, color=(255,255,255), factoroffset=1, height_adjust = 0):
    w,h = pygame.display.get_surface().get_size()
    font = pygame.font.SysFont(Chosen_font, font_size)
    text = font.render(text_string,True, color)
    (wt,ht) = font.size(text_string)
    screen.blit(text,(w/2 - wt/2 ,h/2 - ht/2 * factoroffset + height_adjust))
    return (wt,ht)

def splash_page(screen):
    splash_text(screen,"Laget av Audun Steinkopf i pygame")
    pygame.display.update()
    time.sleep(1)

def main_menu(screen):
    #Definerer verdiene som brukes for å vise alternativene på hovedmenyen
    farge1 = (255,255,255)
    farge2 = (0,0,0)
    w,h = pygame.display.get_surface().get_size()
    Exit_height_adjust = h/3
    (wt,ht) = splash_text(screen, "Avslutt Spillet", height_adjust=Exit_height_adjust)
    (wi, hi) = splash_text(screen, "Instillinger", factoroffset=9, height_adjust=Exit_height_adjust)


    #Definerer og tegner selve alternativene
    avsluttfirkant2 = firkant(w/2 - wt *1.1, h/2 - ht*1.1 + Exit_height_adjust, wt * 2.2, ht * 2.2, screen, farge1)
    avsluttfirkant1 = firkant(w/2 - wt, h/2 - ht + Exit_height_adjust, wt * 2, ht * 2, screen, farge2)

    Instillingsfirkant2 = firkant(w/2 - wt *1.1, h/2 - ht*5.1 + Exit_height_adjust, wt * 2.2, ht * 2.2, screen, farge1)
    Instillingsfirkant1 = firkant(w/2 - wt, h/2 - ht*5 + Exit_height_adjust, wt * 2, ht * 2, screen, farge2)

    splash_text(screen, "Avslutt Spillet", height_adjust=Exit_height_adjust)
    splash_text(screen, "Instillinger", factoroffset=9, height_adjust=Exit_height_adjust)


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if avsluttfirkant1.collidepoint(pygame.mouse.get_pos()):
                return "quit"
            if Instillingsfirkant1.collidepoint(pygame.mouse.get_pos()):
                return "instillinger"

        #Dersom ingenting annet blir valgt fortsetter løkken som før
    return "main_menu"

def instillinger(screen):
    farge1 = (255,255,255)
    farge2 = (0,0,0)
    w,h = pygame.display.get_surface().get_size()
    Exit_height_adjust = h/3

    (wt,ht) = splash_text(screen, "Avslutt Spillet", height_adjust=Exit_height_adjust)
    (wf,hf) = splash_text(screen, "Veksle Fullskjerm", factoroffset=9, height_adjust=Exit_height_adjust)
    togglefirkant2 = firkant(w/2 - wt *1.1, h/2 - ht*5.1 + Exit_height_adjust, wt * 2.2, ht * 2.2, screen, farge1)
    togglefirkant1 = firkant(w/2 - wt, h/2 - ht*5 + Exit_height_adjust, wt * 2, ht * 2, screen, farge2)
    splash_text(screen, "Veksle fullskjerm", factoroffset=9, height_adjust=Exit_height_adjust)

    #Tilbakeknapp
    avsluttfirkant2 = firkant(w/2 - wt *1.1, h/2 - ht*1.1 + Exit_height_adjust, wt * 2.2, ht * 2.2, screen, farge1)
    avsluttfirkant1 = firkant(w/2 - wt, h/2 - ht + Exit_height_adjust, wt * 2, ht * 2, screen, farge2)
    splash_text(screen, "Tilbake", height_adjust=Exit_height_adjust)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if avsluttfirkant1.collidepoint(pygame.mouse.get_pos()):
                return "main_menu"
            if togglefirkant1.collidepoint(pygame.mouse.get_pos()):
                pygame.display.toggle_fullscreen()

    return "instillinger"


def run(screen):
    running = True
    splash_page(screen)
    state = "main_menu"

    while running:
        screen.fill((0,0,0))
        if state == "main_menu":
            state = main_menu(screen)
        if state == "quit":
            running = False
        if state == "instillinger":
            state = instillinger(screen)
        pygame.display.update()
    



main()