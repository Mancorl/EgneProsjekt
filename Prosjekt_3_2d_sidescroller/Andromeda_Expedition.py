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

def splash_text(screen, text_string, Chosen_font = "Arial",font_size = 50, color=(255,255,255), factoroffset=1, height_adjust = 0):
    w,h = pygame.display.get_surface().get_size()
    font = pygame.font.SysFont(Chosen_font, font_size)
    text = font.render(text_string,True, color)
    (wt,ht) = font.size(text_string)
    screen.blit(text,(w/2 - wt/2 ,h/2 * factoroffset + height_adjust))
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
    (wi, hi) = splash_text(screen, "Instillinger", factoroffset=0.5, height_adjust=Exit_height_adjust)


    #Definerer og tegner selve alternativene
    avsluttfirkant2 = firkant(w/3.1, h/2 * 0.94 + Exit_height_adjust, w/2.8, h * 0.12, screen, farge1)
    avsluttfirkant1 = firkant(w/3, h/2 * 0.948 + Exit_height_adjust, w/3, h * 0.11, screen, farge2)

    Instillingsfirkant2 = firkant(w/3.1, h/2 * 0.49 + Exit_height_adjust, w/2.8, h * 0.12, screen, farge1)
    Instillingsfirkant1 = firkant(w/3, h/2 * 0.498 + Exit_height_adjust, w/3, h * 0.11, screen, farge2)

    splash_text(screen, "Avslutt Spillet",factoroffset = 0.99, height_adjust=Exit_height_adjust)
    splash_text(screen, "Instillinger", factoroffset=0.54, height_adjust=Exit_height_adjust)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                return "quit"
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
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
    Exit_height_adjust = h/4
    (wt,ht) = splash_text(screen, "Avslutt Spillet", height_adjust=Exit_height_adjust)

    rezfirkant2 = firkant(w/3.25, h/2 * 0.01 + Exit_height_adjust, w/2.6, h * 0.12, screen, farge1)
    rezfirkant1 = firkant(w/3.10, h/2 * 0.02 + Exit_height_adjust, w/2.8, h * 0.11, screen, farge2)
    splash_text(screen, "Endre Oppløsning", factoroffset=0.06, height_adjust=Exit_height_adjust)

    #Velger mellom fullskjerm eller vindu
    togglefirkant2 = firkant(w/3.25, h/2 * 0.49 + Exit_height_adjust,  w/2.6, h * 0.12, screen, farge1)
    togglefirkant1 = firkant(w/3.10, h/2 * 0.498 + Exit_height_adjust, w/2.8, h * 0.11, screen, farge2)
    splash_text(screen, "Veksle fullskjerm", factoroffset=0.55, height_adjust=Exit_height_adjust)

    #Tilbakeknapp
    avsluttfirkant2 = firkant(w/3.25, h/2 * 0.94 + Exit_height_adjust, w/2.6, h * 0.12, screen, farge1)
    avsluttfirkant1 = firkant(w/3.10, h/2 * 0.948 + Exit_height_adjust, w/2.8, h * 0.11, screen, farge2)
    splash_text(screen, "Tilbake", height_adjust=Exit_height_adjust)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if avsluttfirkant1.collidepoint(pygame.mouse.get_pos()):
                return "main_menu"
            if togglefirkant1.collidepoint(pygame.mouse.get_pos()):
                pygame.display.toggle_fullscreen()
            if rezfirkant1.collidepoint(pygame.mouse.get_pos()):
                if (w,h) != (2560,1440) and (w,h) != (1920,1080) and (w,h) != (1280,720):
                    pygame.display.set_mode((2560,1440), pygame.RESIZABLE)
                #Cant test these two lines properly:
                elif (w,h) == (2560,1440):
                    pygame.display.set_mode((1920,1080))
                elif (w,h) == (1920,1080):
                    pygame.display.set_mode((1280,720))
                else:
                    screeninfo = pygame.display.list_modes()
                    if screeninfo:
                        (w,h) = screeninfo[0]
                    else:
                        #Skulle aldri måtte kjøres, kun dersom katastrofal feil skulle oppstå
                        (w,h) = (1920,1080)
                    pygame.display.set_mode((w,h))


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