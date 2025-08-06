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

def fullscreen_change_reversion_screen(screen, time = 600):
    fps_cap = pygame.time.Clock()
    w,h = pygame.display.get_surface().get_size()
    farge1 = (255,255,255)
    farge2 = (0,0,0)
    while time > 1:
        screen.fill((0,0,0))
        tid = time//60

        akseptfirkant2 = firkant(w/2-h/2.4, h/2 * 0.75, h/1.2, h * 0.12, screen, farge1)
        akseptfirkant1 = firkant(w/2-h/2.6, h/2 * 0.76, h/1.3, h * 0.11, screen, farge2)

        revertfirkant2 = firkant(w/2-h/2.4, h/2 * 1.22, h/1.2, h * 0.12, screen, farge1)
        revertfirkant1 = firkant(w/2-h/2.6, h/2 * 1.23, h/1.3, h * 0.11, screen, farge2)

        splash_text(screen, f"Skjermen reverteres om {tid}", font_size=skalering(120), factoroffset=0.25)
        splash_text(screen, "Behold endringen", font_size=skalering(120) ,factoroffset= 0.76)
        splash_text(screen, "Gå tilbake", font_size=skalering(120), factoroffset=1.25)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):
                if revertfirkant1.collidepoint(pygame.mouse.get_pos()):
                    pygame.display.toggle_fullscreen()
                    return
                elif akseptfirkant1.collidepoint(pygame.mouse.get_pos()):
                    return
                

        fps_cap.tick(60)#Begrense fpsen er enkel måte å sikre timeout uten å programmere en hel dedikert timer
        pygame.display.update()
        time -= 1
    pygame.display.toggle_fullscreen()


def skalering(font_size):
    _,h = pygame.display.get_surface().get_size()
    scale = h / 1440
    #print("scale: ",scale, "font er: ", scale*font_size,"h er: ",h)
    return (round(scale * font_size))

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


    #Definerer og tegner selve alternativene
    avsluttfirkant2 = firkant(w/2-h/3.2, h/2 * 0.94 + Exit_height_adjust, h/1.6, h * 0.12, screen, farge1)
    avsluttfirkant1 = firkant(w/2-h/3.4, h/2 * 0.948 + Exit_height_adjust, h/1.7, h * 0.11, screen, farge2)

    Instillingsfirkant2 = firkant(w/2-h/3.2, h/2 * 0.49 + Exit_height_adjust, h/1.6, h * 0.12, screen, farge1)
    Instillingsfirkant1 = firkant(w/2-h/3.4, h/2 * 0.498 + Exit_height_adjust, h/1.7, h * 0.11, screen, farge2)

    splash_text(screen, "Avslutt Spillet",font_size=skalering(120),factoroffset = 0.99, height_adjust=Exit_height_adjust)
    splash_text(screen, "Instillinger",font_size=skalering(120), factoroffset=0.54, height_adjust=Exit_height_adjust)


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
    rez_string = f"Oppløsning: {w}X{h}"
    #print(rez_string)
    splash_text(screen, rez_string,font_size=skalering(120), factoroffset=0)

    rezfirkant2 = firkant(w/2-h/3.2, h/2 * 0.01 + Exit_height_adjust,  h/1.6, h * 0.12, screen, farge1)
    rezfirkant1 = firkant(w/2-h/3.4, h/2 * 0.02 + Exit_height_adjust, h/1.7, h * 0.11, screen, farge2)
    splash_text(screen, "Endre Oppløsning",font_size=skalering(90), factoroffset=0.06, height_adjust=Exit_height_adjust)

    #Velger mellom fullskjerm eller vindu
    togglefirkant2 = firkant(w/2-h/3.2, h/2 * 0.49 + Exit_height_adjust,   h/1.6, h * 0.12, screen, farge1)
    togglefirkant1 = firkant(w/2-h/3.4, h/2 * 0.498 + Exit_height_adjust, h/1.7, h * 0.11, screen, farge2)
    splash_text(screen, "Veksle fullskjerm",font_size=skalering(90), factoroffset=0.55, height_adjust=Exit_height_adjust)

    #Tilbakeknapp
    avsluttfirkant2 = firkant(w/2-h/3.2, h/2 * 0.94 + Exit_height_adjust,  h/1.6, h * 0.12, screen, farge1)
    avsluttfirkant1 = firkant(w/2-h/3.4, h/2 * 0.948 + Exit_height_adjust, h/1.7, h * 0.11, screen, farge2)
    splash_text(screen, "Tilbake",font_size=skalering(90), height_adjust=Exit_height_adjust)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if avsluttfirkant1.collidepoint(pygame.mouse.get_pos()):
                return "main_menu"
            if togglefirkant1.collidepoint(pygame.mouse.get_pos()):
                #Obs toggle fullscreen kan kræsje displayet dersom en bruker ekstreme oppløsninger, aldri gå under 800 bredde 600 høyde
                pygame.display.toggle_fullscreen()
                #Dersom noe går galt under fullscreen:
                fullscreen_change_reversion_screen(screen)
            if rezfirkant1.collidepoint(pygame.mouse.get_pos()):
                screeninfo = pygame.display.list_modes()
                nåværende_oppløsning = pygame.display.get_surface().get_size()
                if nåværende_oppløsning in screeninfo:
                    index = screeninfo.index(nåværende_oppløsning)
                    neste_index = (index + 1) % len(screeninfo)
                    print(screeninfo[neste_index])
                    #Sirkulerer tilbake til start når vi begynner å få små oppløsninger
                    if screeninfo[neste_index][0]<800 or screeninfo[neste_index][1]<600:
                        print("Nesteindekstrigger")
                        neste_index = 0
                else:
                    neste_index = 0
                
                pygame.display.set_mode((screeninfo[neste_index]))





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