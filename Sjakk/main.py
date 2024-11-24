import pygame
import time
import math
pygame.font.init()

def __init__():
    #initialiserer pygame
    pygame.init()
    pygame.display.set_caption("Sjakk")

class faction():
    def __init__(self, color, player):
        self.color = color
        self.player = player
    
        

        
class board():
    def __init__(self, Player):
        self.board_state = [[None for _ in range(8)] for _ in range(8)]
        if Player.color == "White":
            
            for i in range(8):
                for j in range(8):
                    if i == 0:
                        if j == 0 or j == 7:
                            self.board_state[i][j] = "EnemyRook"
                        if j == 1 or j == 6:
                            self.board_state[i][j] = "EnemyKnight"
                        if j == 2 or j == 5:
                            self.board_state[i][j] = "EnemyBishop"
                        if j == 3:
                            self.board_state[i][j] = "EnemyQueen"
                        if j == 4:
                            self.board_state[i][j] = "EnemyKing"
                    elif i == 1:
                        self.board_state[i][j] = "EnemyPawn"
                    elif i == 6:
                        self.board_state[i][j] = "PlayerPawn"
                    elif i == 7:
                        if j == 0 or j == 7:
                            self.board_state[i][j] = "PlayerRook"
                        if j == 1 or j == 6:
                            self.board_state[i][j] = "PlayerKnight"
                        if j == 2 or j == 5:
                            self.board_state[i][j] = "PlayerBishop"
                        if j == 3:
                            self.board_state[i][j] = "PlayerQueen"
                        if j == 4:
                            self.board_state[i][j] = "PlayerKing"
                    else:
                        self.board_state[i][j] = None
                        
        if Player.color == "Black":
            for i in range(8):
                for j in range(8):
                    if i == 0:
                        if j == 0 or j == 7:
                            self.board_state[i][j] = "EnemyRook"
                        if j == 1 or j == 6:
                            self.board_state[i][j]= "EnemyKnight"
                        if j == 2 or j == 5:
                            self.board_state[i][j]= "EnemyBishop"
                        if j == 4:
                            self.board_state[i][j] = "EnemyQueen"
                        if j == 3:
                            self.board_state[i][j] = "EnemyKing"
                    elif i == 1:
                        self.board_state[i][j] = "EnemyPawn"
                    elif i == 6:
                        self.board_state[i][j] = "PlayerPawn"
                    elif i == 7:
                        if j == 0 or j == 7:
                            self.board_state[i][j] = "PlayerRook"
                        if j == 1 or j == 6:
                            self.board_state[i][j] = "PlayerKnight"
                        if j == 2 or j == 5:
                            self.board_state[i][j] = "PlayerBishop"
                        if j == 4:
                            self.board_state[i][j] = "PlayerQueen"
                        if j == 3:
                            self.board_state[i][j] = "PlayerKing"
                    else:
                        self.board_state[i][j] = None
        

#Definerer grafikken til brikkene og tegner dem
def draw_pawn(screen, x = 0, y = 0,size = 90, color = ((255,0,0))):
    #Definerer relative konstanter, slik at oppløsning kan endres uten å endre grafikkene:
    Padding = size // 5
    pawn_top_radius = size // 6
    x_offset = size // 2
    y_offset = Padding * 2
    
    #Definerer delene av bonden med de relative konstantene
    pawn_top_center = (x + x_offset,y + y_offset)
    Pawn_body = (x+(x_offset//1.22), y + (y_offset) + (pawn_top_radius//2), math.ceil(pawn_top_radius * 1.2), math.ceil(pawn_top_radius * 2))
    pawn_foot = (x + size//4, y+ y_offset + size//3.2, math.ceil(pawn_top_radius * 3), math.ceil(pawn_top_radius))
    
    #Tegner bonden
    pygame.draw.circle(screen, color, pawn_top_center, pawn_top_radius)
    pygame.draw.rect(screen, color, Pawn_body)
    pygame.draw.rect(screen, color, pawn_foot)

#Definerer grafikken til brikkene og tegner dem
def draw_rook(screen, x = 0, y = 0,size = 90, color = ((255,0,0))):
    #Definerer Tårnets relative konstanter
    x_offset = size // 6
    y_offset = size // 2.5
    
    #Definerer delene av Tårnet med De relative konstantene
    rook_body = (x + x_offset, y + y_offset, size//1.5, size//2)
    rook_hat_left = (x + x_offset,y + y_offset - size//10, size // 10, size //10)
    rook_hat_right = (x + size - math.ceil(1.6 * x_offset),y + y_offset - size//10, size // 10, size //10)
    
    #Tegner Tårnet
    pygame.draw.rect(screen, color, rook_body)
    pygame.draw.rect(screen, color, rook_hat_left)
    pygame.draw.rect(screen, color, rook_hat_right)
    
def draw_knight(screen, x = 0, y = 0,size = 90, color = ((255,0,0))):
    #Definerer konstantene
    x_offset = size // 3
    y_offset = size // 5
    #Definerer kroppen
    horse_head = (x+ x_offset, y + y_offset, size //2.5, size//8)
    horse_neck = (x+ x_offset, y + y_offset, size //7, size//4)
    horse_body = (x+ x_offset, y + y_offset + size//4, size //2.5, size//4)
    #Tegner alt
    pygame.draw.rect(screen, color, horse_head)
    pygame.draw.rect(screen, color, horse_neck)
    pygame.draw.rect(screen, color, horse_body)
    
def draw_bishop(screen, x = 0, y = 0,size = 90, color = ((255,0,0))):
    #Definerer Løperens relative konstanter
    x_offset = size // 6
    y_offset = size // 2.5
    
    #Definerer delene av Løperen med De relative konstantene
    bishop_body = (x + x_offset, y + y_offset, size//2, size//2)
    bishop_hat_left = (x + x_offset,y + y_offset - size//10, size // 10, size //10)
    bishop_hat_right = (x + size - math.ceil(2.6 * x_offset),y + y_offset - size//10 - size // 8, size // 10, size //4)
    bishop_hand = (x + 4*x_offset, math.ceil(y + 1.6*y_offset), size//10, size//10)
    bishop_staff = (x + math.ceil(4.5* x_offset), y + y_offset//2 , size//10, size//1.4)
    
    
    #Tegner Løperen
    pygame.draw.rect(screen, color, bishop_body)
    pygame.draw.rect(screen, color, bishop_hat_left)
    pygame.draw.rect(screen, color, bishop_hat_right)
    pygame.draw.rect(screen, color, bishop_hand)
    pygame.draw.rect(screen, color, bishop_staff)
    
def draw_queen(screen, x = 0, y = 0,size = 90, color = ((255,0,0))):
    #Definerer de relative konstantene til dronningen
    x_offset = size // 6
    y_offset = size // 1.2
    
    #Definerer delene av dronningen
    queen_crown_top_center_1 = (math.ceil(x + 1.25*x_offset),y + y_offset - y_offset//4 - size//10)
    queen_top_radius = size // 10
    queen_crown_top_center_2 = (math.ceil(x + 2.5*x_offset),y + y_offset - y_offset//4 - size//10)
    queen_top_radius = size // 10
    queen_crown_top_center_3 = (math.ceil(x + 3.75*x_offset),y + y_offset - y_offset//4 - size//10)
    queen_top_radius = size // 10
    queen_crown_top_center_4 = (math.ceil(x + 5*x_offset),y + y_offset - y_offset//4 - size//10)
    queen_top_radius = size // 10
    queen_body = (x + x_offset,y + y_offset - size//10, size // 1.4, size //5)
    queen_crown_beam_1 = (x + x_offset,y + y_offset - y_offset//5 - size//10, size // 10, size //5)
    queen_crown_beam_2 = (math.ceil(x + 2.25*x_offset),y + y_offset - y_offset//5 - size//10, size // 10, size //5)
    queen_crown_beam_3 = (math.ceil(x + 3.5*x_offset),y + y_offset - y_offset//5 - size//10, size // 10, size //5)
    queen_crown_beam_4 = (math.ceil(x + 4.65*x_offset),y + y_offset - y_offset//5 - size//10, size // 10, size //5)
    
    #Tegner dronningen
    pygame.draw.rect(screen, color, queen_body)
    pygame.draw.rect(screen, color, queen_crown_beam_1)
    pygame.draw.rect(screen, color, queen_crown_beam_2)
    pygame.draw.rect(screen, color, queen_crown_beam_3)
    pygame.draw.rect(screen, color, queen_crown_beam_4)
    pygame.draw.circle(screen, color, queen_crown_top_center_1, queen_top_radius)
    pygame.draw.circle(screen, color, queen_crown_top_center_2, queen_top_radius)
    pygame.draw.circle(screen, color, queen_crown_top_center_3, queen_top_radius)
    pygame.draw.circle(screen, color, queen_crown_top_center_4, queen_top_radius)
    return

def draw_king(screen, x = 0, y = 0,size = 90, color = ((255,0,0))):
    #Definerer kongens relative konstanter
    x_offset = size // 6
    y_offset = size // 1.2
    
    #Definer delene av kongen
    king_body = (x + x_offset,y + y_offset - size//10, size // 1.4, size //5)
    king_beam = (x + 2.6* x_offset,y + y_offset - size//1.9, size // 5, size //1.6)
    king_cross = (x + 1.75* x_offset,y + y_offset//2, size // 2, size //5)
    
    #Tegner kongen
    pygame.draw.rect(screen, color, king_body)
    pygame.draw.rect(screen, color, king_beam)
    pygame.draw.rect(screen, color, king_cross)
    


def draw_board(screen,height, Player, Gameboard):
    square_size = height//(8)
    vertical_list = []
    horizontal_list = [[]]
    enemyColor = ((50,50,50))
    playerColor = ((200,200,200))
    if Player.color == "Black":
        enemyColor = ((255,255,255))
        playerColor = ((0,0,0))
        
    for i in range(8):
        vertical_list = vertical_list + [square_size]
    for j in range(8):
        horizontal_list +=  [vertical_list]
    horizontal_list = horizontal_list[1:]
    screen.fill((0,0,0))
    akk = 1
    color = ((255,0,0))
    x_coordinate = 0
    y_coordinate = 0
    for i in range(len(horizontal_list)):
        for j in range(len(horizontal_list[i])):
            y_coordinate = j * square_size
            x_coordinate = i*square_size
            if akk%2 ==0:
                color = ((0,0,255))
            else:
                color = ((0,255,0))
            pygame.draw.rect(screen, color,(x_coordinate,y_coordinate, square_size,square_size))
            if Gameboard.board_state[j][i] != None:
                if Gameboard.board_state[j][i] == "EnemyRook":
                    draw_rook(screen, x_coordinate, y_coordinate,square_size, enemyColor)
                if Gameboard.board_state[j][i] == "EnemyKnight":
                    draw_knight(screen, x_coordinate, y_coordinate,square_size, enemyColor)
                if Gameboard.board_state[j][i] == "EnemyBishop":
                    draw_bishop(screen, x_coordinate, y_coordinate,square_size, enemyColor)
                if Gameboard.board_state[j][i] == "EnemyQueen":
                    draw_queen(screen, x_coordinate, y_coordinate,square_size, enemyColor)
                if Gameboard.board_state[j][i] == "EnemyKing":
                    draw_king(screen, x_coordinate, y_coordinate,square_size, enemyColor)
                if Gameboard.board_state[j][i] == "EnemyPawn":
                    draw_pawn(screen, x_coordinate, y_coordinate,square_size, enemyColor)
                if Gameboard.board_state[j][i] == "PlayerRook":
                    draw_rook(screen, x_coordinate, y_coordinate,square_size, playerColor)
                if Gameboard.board_state[j][i] == "PlayerKnight":
                    draw_knight(screen, x_coordinate, y_coordinate,square_size, playerColor)
                if Gameboard.board_state[j][i] == "PlayerBishop":
                    draw_bishop(screen, x_coordinate, y_coordinate,square_size, playerColor)
                if Gameboard.board_state[j][i] == "PlayerQueen":
                    draw_queen(screen, x_coordinate, y_coordinate,square_size, playerColor)
                if Gameboard.board_state[j][i] == "PlayerKing":
                    draw_king(screen, x_coordinate, y_coordinate,square_size, playerColor)
                if Gameboard.board_state[j][i] == "PlayerPawn":
                    draw_pawn(screen, x_coordinate, y_coordinate,square_size, playerColor)
            
            #draw_pawn(screen, x_coordinate, y_coordinate,square_size, color=((255,255,255)))
            #draw_rook(screen, x_coordinate, y_coordinate,square_size, color=((255,255,255)))
            #draw_knight(screen, x_coordinate, y_coordinate,square_size, color=((255,255,255)))
            #draw_bishop(screen, x_coordinate, y_coordinate,square_size, color=((255,255,255)))
            #draw_queen(screen, x_coordinate, y_coordinate,square_size, color=((255,255,255)))
            #draw_king(screen, x_coordinate, y_coordinate,square_size, color=((255,255,255)))
            
            akk += 1


        akk += 1
            

def user_interface(screen, height):
    offset = height
    option_font = pygame.font.SysFont('Helvetica', 30)
    option_white = option_font.render("White", False, (0,255,255) )
    option_black = option_font.render("Black", False, (0,255,255) )
    pygame.draw.rect(screen, (120,120,120),(offset + height//7, height//13, height//6, height//6 ) )
    pygame.draw.rect(screen, (120,120,120),(offset + height//2 - height//30, height//13, height//6, height//6 ) )
    screen.blit(option_white,(offset + height//6, height//8 ))
    screen.blit(option_black,(offset + height//2, height//8 ))

def run(gameboard, Player, width = 1280, height = 720):
    running = True
    screen = pygame.display.set_mode((width,height))
    draw_board(screen, height, Player, gameboard)
    while running:
        screen.fill((0,0,0))
        draw_board(screen, height,Player,gameboard)
        user_interface(screen, height)
        pygame.display.flip()




def main():
    __init__()
    Player = faction("White", True)
    Cpu = faction("Black", False)
    gameboard = board(Player)
    run(gameboard, Player)

main()