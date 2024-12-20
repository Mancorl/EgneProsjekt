import pygame
import math
import sys
import copy
pygame.font.init()

#TODO: AI
#TODO: Sjakkmatt
#TODO: Uavgjort
#TODO: Pawn an pasang

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
        self.running = True
        self.board_state = [[None for _ in range(8)] for _ in range(8)]
        self.en_passant = False
        self.PlayerRokkerright = True
        self.PlayerRokkerleft = True
        self.enemyRokkerright = True
        self.enemyRokkerleft = True
        self.en_passant_counter = 0
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
                        
    def select(self, unit, i, j, screen, prev_i = 100, prev_j = 100):
        y = screen.get_height()
        centering = y//8
        if unit == "PlayerPawn":
            print("Pawn selected")
            if i == 6:
                if self.board_state[i-1][j] == None:
                    pygame.draw.circle(screen, (255,255,0), ((j) * centering + centering//2, (i-1) *centering + centering//2), centering//2)
                    if self.board_state[i-2][j] == None:
                        pygame.draw.circle(screen, (255,255,0), ((j) * centering + centering//2,(i-2) *centering + centering//2), centering//2)
            elif self.board_state[i-1][j] == None:
                pygame.draw.circle(screen, (255,255,0), ((j) * centering + centering//2, (i-1) *centering + centering//2), centering//2)
            try:
                if self.board_state[i-1][j+1] != None:
                    print(f"board is not none but {self.board_state[j+1][i-1]} j+1:{j+1}, i-1:{i-1}") 
                    if self.board_state[i-1][j+1].startswith("Enemy"):
                        print("im printing")
                        pygame.draw.circle(screen, (255, 0, 0), ((j + 1) * centering + centering // 2, (i-1) * centering + centering // 2), centering // 4)
            except:
                print(f"exception has occurred i:{i} j:{j}")
                pass
            try:
                if self.board_state[i-1][j-1] != None: 
                    print(f"board is not none but {self.board_state[j-1][i-1]}j+1:{j-1}, i+1:{i-1}")
                    if self.board_state[i-1][j-1].startswith("Enemy"):
                        print("im also printing")
                        pygame.draw.circle(screen, (255, 0, 0), ((j - 1) * centering + centering // 2, (i-1) * centering + centering // 2), centering // 4)
            except:
                print(f"exception has occurred i:{i} j:{j}")
                pass

                
            if self.en_passant and prev_j > j and (prev_i == i+1  or prev_i == i-1):
                if prev_j > j and prev_i == i+1:
                    pygame.draw.circle(screen, (120,120,120), i + y + centering, centering//2)
                elif prev_j > j and prev_i == i-1:
                    pygame.draw.circle(screen, (120,120,120), i + 2 * y + centering, centering//2)
            
        if unit == "PlayerRook":
            self.moveRight(i,j,screen,centering)
            self.moveLeft(i,j,screen,centering)
            self.moveUp(i,j,screen,centering)
            self.moveDown(i,j,screen,centering)
                
        if unit == "PlayerKnight":
            if i + 2 < 8 and j +1 <8:
                if self.board_state[i + 2][j + 1] is not None:
                    if self.board_state[i + 2][j + 1].startswith("Player") == False:
                        pygame.draw.circle(screen, (255, 0, 0), ((j + 1) * centering + centering // 2, (i +2) * centering + centering // 2), centering // 4)
                        
                if self.board_state[i + 2][j+1] == None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j + 1) * centering + centering // 2, (i +2) * centering + centering // 2), centering // 2)
                    
            if i + 1 < 8 and j +2 <8:
                if self.board_state[i + 1][j + 2] is not None:
                    if self.board_state[i + 1][j + 2].startswith("Player") == False:
                        pygame.draw.circle(screen, (255, 0, 0), ((j + 2) * centering + centering // 2, (i+ 1) * centering + centering // 2), centering // 4)
                if self.board_state[i + 1][j+2] == None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j + 2) * centering + centering // 2, (i +1) * centering + centering // 2), centering // 2)
                    
            if i + 1 < 8 and j -2 >-1:
                if self.board_state[i + 1][j - 2] is not None:
                    if self.board_state[i + 1][j - 2].startswith("Player") == False:
                        pygame.draw.circle(screen, (255, 0, 0), ((j - 2) * centering + centering // 2, (i +1) * centering + centering // 2), centering // 4)
                if self.board_state[i + 1][j-2] == None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j - 2) * centering + centering // 2, (i +1) * centering + centering // 2), centering // 2)
            
            if i - 1 > -1 and j -2 >-1:
                if self.board_state[i - 1][j - 2] is not None:
                    if self.board_state[i - 1][j - 2].startswith("Player") == False:
                        pygame.draw.circle(screen, (255, 0, 0), ((j - 2) * centering + centering // 2, (i -1) * centering + centering // 2), centering // 4)
                if self.board_state[i - 1][j-2] == None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j - 2) * centering + centering // 2, (i -1) * centering + centering // 2), centering // 2)
            
            if i + 2 < 8 and j -1 >-1:
                if self.board_state[i + 2][j - 1] is not None:
                    if self.board_state[i + 2][j - 1].startswith("Player") == False:
                        pygame.draw.circle(screen, (255, 0, 0), ((j - 1) * centering + centering // 2, (i +2) * centering + centering // 2), centering // 4)
                if self.board_state[i + 2][j-1] == None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j - 1) * centering + centering // 2, (i +2) * centering + centering // 2), centering // 2)
                    
            if i - 1 > -1 and j + 2 <8:
                if self.board_state[i - 1][j + 2] is not None:
                    if self.board_state[i - 1][j + 2].startswith("Player") == False:
                        if self.board_state[i - 1][j + 2].startswith("Player") == False:
                            pygame.draw.circle(screen, (255, 0, 0), ((j + 2) * centering + centering // 2, (i -1) * centering + centering // 2), centering // 4)
                if self.board_state[i - 1][j+2] == None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j + 2) * centering + centering // 2, (i -1) * centering + centering // 2), centering // 2)
            
            if i - 2 > -1 and j + 1 <8:
                if self.board_state[i - 2][j + 1] is not None:
                    if self.board_state[i - 2][j + 1].startswith("Player") == False:
                        if self.board_state[i - 2][j + 1].startswith("Player") == False:
                            pygame.draw.circle(screen, (255, 0, 0), ((j + 1) * centering + centering // 2, (i -2) * centering + centering // 2), centering // 4)
                            print("its me")
                if self.board_state[i - 2][j+1] == None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j + 1) * centering + centering // 2, (i -2) * centering + centering // 2), centering // 2)
            
            if i - 2 > -1 and j - 1 >-1:
                if self.board_state[i - 2][j - 1] is not None:
                    if self.board_state[i - 2][j - 1].startswith("Player") == False:
                        if self.board_state[i - 2][j - 1].startswith("Player") == False:
                            pygame.draw.circle(screen, (255, 0, 0), ((j - 1) * centering + centering // 2, (i -2) * centering + centering // 2), centering // 4)
                if self.board_state[i - 2][j-1] == None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j - 1) * centering + centering // 2, (i -2) * centering + centering // 2), centering // 2)
            
        if unit == "PlayerBishop":
            self.bishopmovesul(i,j,screen,centering)
            self.bishopmovesdl(i,j,screen,centering)
            self.bishopmovesur(i,j,screen,centering)
            self.bishopmovesdr(i,j,screen,centering)
        if unit == "PlayerQueen":
            self.bishopmovesul(i,j,screen,centering)
            self.bishopmovesdl(i,j,screen,centering)
            self.bishopmovesur(i,j,screen,centering)
            self.bishopmovesdr(i,j,screen,centering)
            self.moveDown(i,j,screen,centering)
            self.moveUp(i,j,screen,centering)
            self.moveLeft(i,j,screen,centering)
            self.moveRight(i,j,screen,centering)
        if unit == "PlayerKing":
            self.bishopmovesul(i,j,screen,centering, True)
            self.bishopmovesdl(i,j,screen,centering, True)
            self.bishopmovesur(i,j,screen,centering, True)
            self.bishopmovesdr(i,j,screen,centering, True)
            self.moveDown(i,j,screen,centering, True)
            self.moveUp(i,j,screen,centering, True)
            self.moveLeft(i,j,screen,centering, True)
            self.moveRight(i,j,screen,centering, True)
            self.rokadesjekk(i,j,screen,centering)
        pygame.display.flip()
        return unit
                
    def bishopmovesul(self,x,y, screen, centering, king = False):
        blocked = False
        if x - 1 > -1 and y - 1 > -1:
            if self.board_state[x - 1][y - 1] == None and blocked == False:
                pygame.draw.circle(screen, (255, 255, 0), ((y - 1) * centering + centering // 2, (x - 1) * centering + centering // 2), centering // 2)
                if not king:
                    self.bishopmovesul(x-1, y-1, screen, centering)
            if self.board_state[x-1][y-1] is not None:
                if self.board_state[x-1][y-1].startswith("Enemy"):
                    blocked = True
                    pygame.draw.circle(screen, (255, 0, 0), ((y - 1) * centering + centering // 2, (x - 1) * centering + centering // 2), centering // 4)
                    
    def bishopmovesdl(self,x,y, screen, centering,king = False):
        blocked = False
        if x + 1 < 8 and y - 1 > -1:
            if self.board_state[x + 1][y - 1] == None and blocked == False:
                pygame.draw.circle(screen, (255, 255, 0), ((y - 1) * centering + centering // 2, (x + 1) * centering + centering // 2), centering // 2)
                if not king:
                    self.bishopmovesdl(x+1, y-1, screen, centering)
            if self.board_state[x+1][y-1] is not None:
                if self.board_state[x+1][y-1].startswith("Enemy"):
                    blocked = True
                    pygame.draw.circle(screen, (255, 0, 0), ((y - 1) * centering + centering // 2, (x + 1) * centering + centering // 2), centering // 4)
                    
    def bishopmovesur(self,x,y, screen, centering,king = False):
        blocked = False
        if x - 1 > -1 and y + 1 < 8:
            if self.board_state[x - 1][y + 1] == None and blocked == False:
                pygame.draw.circle(screen, (255, 255, 0), ((y + 1) * centering + centering // 2, (x - 1) * centering + centering // 2), centering // 2)
                if not king:
                    self.bishopmovesur(x-1, y+1, screen, centering)
            if self.board_state[x-1][y+1] is not None:
                if self.board_state[x-1][y+1].startswith("Enemy"):
                    blocked = True
                    pygame.draw.circle(screen, (255, 0, 0), ((y + 1) * centering + centering // 2, (x - 1) * centering + centering // 2), centering // 4)
                    
    def bishopmovesdr(self,x,y, screen, centering,king = False):
        blocked = False
        if x + 1 < 8 and y + 1 < 8:
            if self.board_state[x + 1][y + 1] == None and blocked == False:
                pygame.draw.circle(screen, (255, 255, 0), ((y + 1) * centering + centering // 2, (x + 1) * centering + centering // 2), centering // 2)
                if not king:
                    self.bishopmovesdr(x+1, y+1, screen, centering)
            if self.board_state[x+1][y+1] is not None:
                if self.board_state[x+1][y+1].startswith("Enemy"):
                    blocked = True
                    pygame.draw.circle(screen, (255, 0, 0), ((y + 1) * centering + centering // 2, (x + 1) * centering + centering // 2), centering // 4)

    def moveDown(self, x, y,screen, centering,king = False):
        if x + 1 < 8:
            if self.board_state[x+1][y] == None:
                pygame.draw.circle(screen, (255, 255, 0), ((y) * centering + centering // 2, (x + 1) * centering + centering // 2), centering // 2)
                if not king:
                    self.moveDown(x+1, y, screen, centering)
            if self.board_state[x+1][y] is not None:
                if self.board_state[x+1][y].startswith("Enemy"):
                    pygame.draw.circle(screen, (255, 0, 0), ((y) * centering + centering // 2, (x+1) * centering + centering // 2), centering // 4)
        
    def moveUp(self, x, y,screen, centering,king = False):
        if x - 1 > -1:
            if self.board_state[x-1][y] == None:
                pygame.draw.circle(screen, (255, 255, 0), ((y) * centering + centering // 2, (x - 1) * centering + centering // 2), centering // 2)
                if not king:
                    self.moveUp(x-1, y, screen, centering)
            if self.board_state[x-1][y] is not None:
                if self.board_state[x-1][y].startswith("Enemy"):
                    pygame.draw.circle(screen, (255, 0, 0), ((y) * centering + centering // 2, (x-1) * centering + centering // 2), centering // 4)
                    
    def moveLeft(self, x, y,screen, centering,king = False):
        if y - 1 > -1:
            if self.board_state[x][y-1] == None:
                pygame.draw.circle(screen, (255, 255, 0), ((y-1) * centering + centering // 2, (x) * centering + centering // 2), centering // 2)
                if not king:
                    self.moveLeft(x, y-1, screen, centering)
            if self.board_state[x][y-1] is not None:

                if self.board_state[x][y-1].startswith("Enemy"):

                    pygame.draw.circle(screen, (255, 0, 0), ((y-1) * centering + centering // 2, (x) * centering + centering // 2), centering // 4)
                    
    def moveRight(self, x, y,screen, centering, king = False):
        if y + 1 < 8:
            if self.board_state[x][y+1] == None:
                pygame.draw.circle(screen, (255, 255, 0), ((y+1) * centering + centering // 2, (x) * centering + centering // 2), centering // 2)
                if not king:
                    self.moveRight(x, y+1, screen, centering)
            if self.board_state[x][y+1] is not None:

                if self.board_state[x][y+1].startswith("Enemy"):

                    pygame.draw.circle(screen, (255, 0, 0), ((y+1) * centering + centering // 2, (x) * centering + centering // 2), centering // 4)
    def rokadesjekk(self,x,y,screen,centering):
        if self.PlayerRokkerleft:
            print("Prøver å rokkere")
            try:
                print("er i try setningen")
                if self.board_state[7][0] == "PlayerRook":
                    print("Sjekker torn")
                    
                    if self.board_state[7][1] == None and self.board_state[7][2] == None:
                        print("Sjekker at det er tomt")
                        print(x)
                        if self.board_state[7][3] == None or self.board_state[7][3].endswith("King"):
                            print("Er jeg her skulle det tegnes skikkelig")
                            pygame.draw.circle(screen, (255, 255, 0), ((y-2) * centering + centering // 2, (x) * centering + centering // 2), centering // 2)
            except:
                pass
        if self.PlayerRokkerright:
            print("Prøver å rokkere")
            try:
                print("er i try setningen")
                if self.board_state[7][7] == "PlayerRook":
                    print("Sjekker torn")
                    
                    if self.board_state[7][5] == None and self.board_state[7][6] == None:
                        print("Sjekker at det er tomt")
                        print(x)
                        if self.board_state[7][4] == None or self.board_state[7][4].endswith("King"):
                            print("Er jeg her skulle det tegnes skikkelig")
                            pygame.draw.circle(screen, (255, 255, 0), ((y+2) * centering + centering // 2, (x) * centering + centering // 2), centering // 2)
            except:
                pass
            
            
                    
        
                    
    def Execute(self, unit, i,j,x,y,square_size, screen, prev_i=None, player = False):
        print("Attempting to execute", unit)
        if self.en_passant_counter == 0:
            self.en_passant = False
        else:
            self.en_passant_counter -= 1
        print(player)
        playerfactor = 1
        playercolor = ((255,255,255))
        if sjakksjekk(self,i,j,player):
            print("Kongen er i sjakk")
        if not player:
            playerfactor = -1
            playercolor = ((0,0,0))
            
        if unit.endswith("Pawn"):
            if self.en_passant:
                if prev_i != None:
                    if prev_i == i + 1:
                        if (x == i +1 and y == j -1*playerfactor and ismovelegal(self,i,j,x,y,player,unit)):
                            self.board_state[i][j] = None
                            self.board_state[x][y] = unit
                    if prev_i == i - 1:
                        if (x == i -1 and y == j -1*playerfactor and ismovelegal(self,i,j,x,y,player,unit)):
                            self.board_state[i][j] = None
                            self.board_state[x][y] = unit
            if (y == j - 1 or y == j+1 and (x == x-1 * playerfactor and x != i)):

                try:
                    if self.board_state[y][x].startswith("Enemy") and x !=i:
                        if ismovelegal(self,i,j,x,y,player,unit):
                            self.board_state[j][i] = None
                            self.board_state[y][x] = unit
                except:
                    pass
                
            if (y == j - 1 * playerfactor and x == i) and ismovelegal(self,i,j,x,y,player,unit):
                if self.board_state[j-1][i] == None:
                    self.board_state[j][i] = None
                    self.board_state[y][x] = unit
                    
            if ((player and y == 0) or (not player and y == 7)):
                while self.board_state[y][x].endswith("Pawn"):
                    draw_rook(screen, x*square_size, (y + 3 * playerfactor)*square_size,square_size, color=playercolor)
                    draw_knight(screen, x*square_size, (y + 2 * playerfactor)*square_size,square_size, color=playercolor)
                    draw_bishop(screen, x*square_size, (y + 1 * playerfactor)*square_size ,square_size, color=playercolor)
                    draw_queen(screen, x*square_size, y*square_size,square_size, color=playercolor)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        print(event)
                        if pygame.mouse.get_pressed()[0]:
                            (a,e) = pygame.mouse.get_pos()
                            print(a,e)
                            a = a // square_size
                            e = e // square_size
                            if e == y and a == x:
                                if player:
                                    self.board_state[y][x] = "PlayerQueen"
                                        
                                else:
                                    self.board_state[y][x] = "EnemyQueen"
                            if e == y+1*playerfactor and a == x:
                                if player:
                                    self.board_state[y][x] = "PlayerBishop"
                                        
                                else:
                                    self.board_state[y][x] = "EnemyBishop"
                                    
                            if e == y+2*playerfactor and a == x:
                                if player:
                                    self.board_state[y][x] = "PlayerKnight"
                                    
                                else:
                                    self.board_state[y][x] = "EnemyKnight"
                            if e == y+3*playerfactor and a == x:
                                if player:
                                    self.board_state[y][x] = "PlayerRook"
                                        
                                else:
                                    self.board_state[y][x] = "EnemyRook"
                                        
                        

            if (((y == j - 2 * playerfactor and ((player == True and j == 6) or (player == False and j == 1)) and x == i)) and ismovelegal(self,i,j,x,y,player,unit)): 
                if self.board_state[y][x] == None:
                    print(self.board_state[y][x])
                    self.board_state[j][i] = None
                    self.board_state[y][x] = unit
                    self.en_passant = True
                    self.en_passant_counter = 1
        
        if unit.endswith("Knight"):
            print("knight selected")
            if ((((y == j + 2 or y == j -2) and (x == i +1 or x == i - 1)) or ((y == j +1 or y == j - 1) and (x == i + 2 or x == i - 2))) and ismovelegal(self,i,j,x,y,player,unit)):
                try:
                    if self.board_state[y][x].startswith("Player"):
                        print("I should abort")
                        return
                except:
                    pass

                
                self.board_state[j][i] = None
                self.board_state[y][x] = unit
                
        if unit.endswith("Bishop") and ismovelegal(self,i,j,x,y,player,unit):
            if self.bishopmove(j,i,y,x):
                self.board_state[j][i] = None
                self.board_state[y][x] = unit
                
        if unit.endswith("Rook"):
            if self.rockmove(j,i,y,x):
                if j == y or x == i and ismovelegal(self,i,j,x,y,player,unit):
                    self.board_state[j][i] = None
                    self.board_state[y][x] = unit
                
        if unit.endswith("Queen"):
            if (self.bishopmove(j,i,y,x) or (self.rockmove(j,i,y,x) and (x == i or y == j)))and ismovelegal(self,i,j,x,y,player,unit):
                self.board_state[j][i] = None
                self.board_state[y][x] = unit
        
        if unit.endswith("King"):
            if (self.bishopmove(j,i,y,x, True) or (self.rockmove(j,i,y,x, True) and (x == i or y == j))) and ismovelegal(self,i,j,x,y,player,unit):
                self.board_state[j][i] = None
                self.board_state[y][x] = unit
                if player:
                    self.PlayerRokkerleft = False
                    self.PlayerRokkerright = False
                else:
                    self.enemyRokkerleft = False
                    self.enemyRokkerright = False
            if (x == i-2 or x == i + 2) and ismovelegal(self,i,j,x,y,player,unit):
                self.Kongerokade(i,j,x,y, True)
                    
                
    def rockmove(self,j,i,y,x, king = False):
        up = True
        down = True
        left = True
        right = True
        rangevar = 8
        if king:
            rangevar = 2
        for k in range(1,rangevar):
            if up:
                if j+k == y:
                    try:
                        if self.board_state[j+k][i].startswith("Player"):
                            return False
                    except:
                        pass
                    return True
                try:
                    if(self.board_state[j+k][i].startswith("Enemy") or self.board_state[j+k][i].startswith("Player")):
                        up = False
                except:
                    pass
            if down:
                if j-k == y:
                    try:
                        if self.board_state[j-k][i].startswith("Player"):
                            return False
                    except:
                        pass
                    return True
                try:
                    if(self.board_state[j-k][i].startswith("Enemy") or self.board_state[j-k][i].startswith("Player")):
                        down = False
                except:
                    pass
            if left:
                if i-k == x:
                    try:
                        if self.board_state[j][i-k].startswith("Player"):
                            return False
                    except:
                        pass
                    return True
                try:
                    if(self.board_state[j][i-k].startswith("Enemy") or self.board_state[j][i-k].startswith("Player")):
                        left = False
                except:
                    pass
            if right:
                if i+k == x:
                    try:
                        if self.board_state[j][i+k].startswith("Player"):
                            return False
                    except:
                        pass
                    return True
                try:
                    if(self.board_state[j][i+k].startswith("Enemy") or self.board_state[j][i+k].startswith("Player")):
                        right = False
                except:
                    pass
        return False
    def bishopmove(self, i , j, x,y, king = False):
        print(f"{i}{j}{x}{y}")
        ur = True
        dr = True
        ul = True
        dl = True
        rangevar = 8
        if king:
            rangevar = 2
        for k in range(1,rangevar):
            print(f"k = {k} k + i:{k+1} k + j:{k+j} k-i:{k-i} k-j{k-j}")
            if True:
                
                if dr:
                    if (i + k == x and j + k == y):
                        try:
                            if self.board_state[i+k][j+k].startswith("Player"):
                                return False
                        except:
                            pass
                        return True
                    try:
                        if(self.board_state[i+k][j+k].startswith("Enemy") or self.board_state[i+k][j+k].startswith("Player")):
                            dr = False
                    except:
                        print("Exception dr triggered")
                        pass
                    
                if dl:
                    if (i + k == x and j - k == y):
                        try:
                            if self.board_state[i+k][j-k].startswith("Player"):
                                return False
                        except:
                            pass
                        
                        return True
                    
                    try:
                        if(self.board_state[i+k][j-k].startswith("Enemy") or self.board_state[i+k][j-k].startswith("Player")):
                            dl = False
                    except:
                        print("Exception dl triggered")
                        pass
                if ur:
                    if (i - k == x and j + k == y ):
                        try:
                            if self.board_state[i-k][j+k].startswith("Player"):
                                return False
                        except:
                            pass
                        return True
                    try:
                        
                        if(self.board_state[i-k][j+k].startswith("Enemy") or self.board_state[i-k][j+k].startswith("Player")):
                            ur = False
                    except:
                        print("Exception ur triggered")
                        pass
                if ul:
                    if (i - k == x and j - k == y):
                        try:
                            if self.board_state[i-k][j-k].startswith("Player"):
                                return False
                        except:
                            pass
                        return True
                    try:
                        if(self.board_state[i-k][j-k].startswith("Enemy") or self.board_state[i-k][j-k].startswith("Player")):
                            ul = False
                    except:
                        print("Exception ul triggered")
                        pass
                    
        return False
    def Kongerokade(self, i,j,x,y, player = True):
        if self.PlayerRokkerleft:
            print("Prøver å rokkere")
            try:
                print("er i try setningen")
                if self.board_state[7][0] == "PlayerRook":
                    print("Sjekker torn")
                    
                    if self.board_state[7][1] == None and self.board_state[7][2] == None:
                        print("Sjekker at det er tomt")
                        print(x)
                        if self.board_state[7][3] == None or self.board_state[7][3].endswith("King"):
                            print(i,j)
                            print("Er jeg her skulle det tegnes skikkelig")
                            self.board_state[i][j] = None
                            self.board_state[7][0] = None
                            self.board_state[j][i-1] = "PlayerRook"
                            self.board_state[j][i-2] = "PlayerKing"
            except:
                pass
        if self.PlayerRokkerright:
            print("Prøver å rokkere")
            try:
                print("er i try setningen")
                if self.board_state[7][7] == "PlayerRook":
                    print("Sjekker torn")
                    
                    if self.board_state[7][5] == None and self.board_state[7][6] == None:
                        print("Sjekker at det er tomt")
                        print(x)
                        if self.board_state[7][4] == None or self.board_state[7][4].endswith("King"):
                            
                            print("Er jeg her skulle det tegnes skikkelig")
                            print(self.board_state[j][i])
                            self.board_state[j][i] = None
                            self.board_state[7][7] = None
                            self.board_state[j][i+1] = "PlayerRook"
                            self.board_state[j][i+2] = "PlayerKing"
                            print(self.board_state[j][i])
            except:
                pass
        if not player:
            if self.enemyRokkerleft:
                print("Prøver å rokkere")
                try:
                    print("er i try setningen")
                    if self.board_state[0][0] == "EnemyRook":
                        print("Sjekker torn")
                    
                        if self.board_state[0][1] == None and self.board_state[0][2] == None:
                            print("Sjekker at det er tomt")
                            print(x)
                            if self.board_state[0][3] == None or self.board_state[0][3].endswith("King"):
                                print(i,j)
                                print("Er jeg her skulle det tegnes skikkelig")
                                self.board_state[i][j] = None
                                self.board_state[0][0] = None
                                self.board_state[j][i-1] = "EnemyRook"
                                self.board_state[j][i-2] = "EnemyKing"
                except:
                    pass
            if self.enemyRokkerright:
                print("Prøver å rokkere")
                try:
                    print("er i try setningen")
                    if self.board_state[0][7] == "EnemyRook":
                        print("Sjekker torn")
                    
                        if self.board_state[0][5] == None and self.board_state[0][6] == None:
                            print("Sjekker at det er tomt")
                            print(x)
                            if self.board_state[0][4] == None or self.board_state[0][4].endswith("King"):
                            
                                print("Er jeg her skulle det tegnes skikkelig")
                                print(self.board_state[j][i])
                                self.board_state[j][i] = None
                                self.board_state[0][7] = None
                                self.board_state[j][i+1] = "EnemyRook"
                                self.board_state[j][i+2] = "EnemyKing"
                                print(self.board_state[j][i])
                except:
                    pass
            
        
        
        
        return

def sjakksjekk(brett,x,y, player):
    if Sjekkright(brett,x,y, player) or Sjekkleft(brett,x,y,player) or sjekkup(brett,x,y,player) or sjekkdown(brett,x,y,player)or sjekkur(brett,x,y,player) or sjekkul(brett,x,y,player) or sjekkdr(brett,x,y,player) or sjekkdl(brett,x,y,player) or sjekkknight(brett,x,y,player):
        return True
    else:
        return False

def Sjekkright(brett,x,y, player):
    #Basecase
    if x + 1 > 7:
        return False
    if brett.board_state[y][x+1] is None:
        #Sjekker neste rekursivt da nåværende lokasjon ikke gir info
        return Sjekkright(brett,x+1,y,player)
    elif brett.board_state[y][x+1].endswith("PlayerKing"):
        if player:
            return Sjekkright(brett,x+1,y,player)
        
    elif player:
        #Hvis fiendens tårn eller Dronning er på x- aksen er kongen i sjakk, hvis det er noe annet er ikke spillerens konge i sjakk
        if brett.board_state[y][x+1] == "EnemyRook" or brett.board_state[y][x+1] == "EnemyQueen":
            return True
        else:
            return False
    elif not player:
        if brett.board_state[y][x+1] == "PlayerRook" or brett.board_state[y][x+1] == "PlayerQueen":
            #Hvis Spillerens tårn eller Dronning er på x- aksen er kongen i sjakk, hvis det er noe annet er ikke Fiendens konge i sjakk
            return True
        else:
            return False

def Sjekkleft(brett,x,y, player):
        #Basecase
    if x - 1 < 0:
        return False
    if brett.board_state[y][x-1] is None:
        #Sjekker neste rekursivt da nåværende lokasjon ikke gir info
        return Sjekkleft(brett,x-1,y,player)
    elif brett.board_state[y][x-1].endswith("King"):
        return Sjekkleft(brett,x-1,y,player)
    elif player:
        #Hvis fiendens tårn eller Dronning er på x- aksen er kongen i sjakk, hvis det er noe annet er ikke spillerens konge i sjakk
        if brett.board_state[y][x-1] == "EnemyRook" or brett.board_state[y][x-1] == "EnemyQueen":
            return True
        else:
            return False
    elif not player:
        if brett.board_state[y][x-1] == "PlayerRook" or brett.board_state[y][x-1] == "PlayerQueen":
            #Hvis Spillerens tårn eller Dronning er på x- aksen er kongen i sjakk, hvis det er noe annet er ikke Fiendens konge i sjakk
            return True
        else:
            return False

def sjekkup(brett,x,y,player):
    print("Sjekker opp")
    print(brett.board_state[y][x])
        #Basecase
    if y - 1 < 0:
        print("Basecase trigges")
        return False
    if brett.board_state[y-1][x] is None:
        #Sjekker neste rekursivt da nåværende lokasjon ikke gir info
        print("Gaar ned i neste dybde")
        return sjekkup(brett,x,y-1,player)
    elif brett.board_state[y-1][x].endswith("King"):
        return sjekkup(brett,x,y-1,player)
    elif player:
        #Hvis fiendens tårn eller Dronning er på x- aksen er kongen i sjakk, hvis det er noe annet er ikke spillerens konge i sjakk
        if brett.board_state[y-1][x] == "EnemyRook" or brett.board_state[y-1][x] == "EnemyQueen":
            return True
        else:
            return False
    elif not player:
        if brett.board_state[y-1][x] == "PlayerRook" or brett.board_state[y-1][x] == "PlayerQueen":
            #Hvis Spillerens tårn eller Dronning er på y- aksen er kongen i sjakk, hvis det er noe annet er ikke Fiendens konge i sjakk
            return True
        else:
            return False

def sjekkdown(brett,x,y,player):
    print("Sjekker ned")
    if y + 1 > 7:
        return False
    if brett.board_state[y+1][x] is None:
        #Sjekker neste rekursivt da nåværende lokasjon ikke gir info
        print("Gaar nedover i neste dybde")
        return sjekkdown(brett,x,y+1, player)
    elif brett.board_state[y+1][x].endswith("King"):
        return sjekkdown(brett,x,y+1,player)
    elif player:
        #Hvis fiendens tårn eller Dronning er på y- aksen er kongen i sjakk, hvis det er noe annet er ikke spillerens konge i sjakk
        if brett.board_state[y+1][x] == "EnemyRook" or brett.board_state[y+1][x] == "EnemyQueen":
            return True
        else:
            return False
    elif not player:
        if brett.board_state[y+1][x] == "PlayerRook" or brett.board_state[y+1][x] == "PlayerQueen":
            #Hvis Spillerens tårn eller Dronning er på y- aksen er kongen i sjakk, hvis det er noe annet er ikke Fiendens konge i sjakk
            return True
        else:
            return False

def sjekkur(brett,x,y,player, first = True):
        #Basecase
    if x + 1 > 7 or y -1 <0:
        return False
    if brett.board_state[y-1][x+1] == None:
        #Sjekker neste rekursivt da nåværende lokasjon ikke gir info
        return sjekkur(brett,x+1,y-1,player,  False)
    elif brett.board_state[y-1][x+1].endswith("King"):
        return sjekkur(brett,x+1,y-1,player, False)
    elif player:
        #Hvis fiendens løper eller Dronning er på diagonalen er kongen i sjakk, hvis det er noe annet er ikke spillerens konge i sjakk
        if brett.board_state[y-1][x+1] == "EnemyBishop" or brett.board_state[y-1][x+1] == "EnemyQueen":
            return True
        elif first:
            if brett.board_state[y-1][x+1] == "EnemyPawn":
                return True
        else:
            return False
    elif not player:
        if brett.board_state[y-1][x+1] == "PlayerBishop" or brett.board_state[y-1][x+1] == "PlayerQueen":
            #Hvis Spillerens løper eller Dronning er på diagonalen er kongen i sjakk, hvis det er noe annet er ikke Fiendens konge i sjakk
            return True
        elif first:
            if brett.board_state[y-1][x+1] == "PlayerPawn":
                return True
        else:
            return False
        
def sjekkul(brett,x,y,player, first = True):
        #Basecase
    if x - 1 < 0 or y -1 <0:
        return False
    if brett.board_state[y-1][x-1] == None:
        #Sjekker neste rekursivt da nåværende lokasjon ikke gir info
        return sjekkul(brett,x-1,y-1,player, False)
    elif brett.board_state[y-1][x-1].endswith("King"):
        return sjekkul(brett,x-1,y-1,player, False)
    elif player:
        #Hvis fiendens løper eller Dronning er på diagonalen er kongen i sjakk, hvis det er noe annet er ikke spillerens konge i sjakk
        if brett.board_state[y-1][x-1] == "EnemyBishop" or brett.board_state[y-1][x-1] == "EnemyQueen":
            return True
        elif first:
            if brett.board_state[y-1][x-1] == "EnemyPawn":
                return True
        else:
            return False
    elif not player:
        if brett.board_state[y-1][x-1] == "PlayerBishop" or brett.board_state[y-1][x-1] == "PlayerQueen":
            #Hvis Spillerens løper eller Dronning er på diagonalen er kongen i sjakk, hvis det er noe annet er ikke Fiendens konge i sjakk
            return True
        elif first:
            if brett.board_state[y-1][x-1] == "PlayerPawn":
                return True
        else:
            return False
        
def sjekkdl(brett,x,y,player, first = True):
        #Basecase
    if x - 1 < 0 or y +1 >7:
        return False
    if brett.board_state[y+1][x-1] == None:
        #Sjekker neste rekursivt da nåværende lokasjon ikke gir info
        return sjekkdl(brett,x-1,y+1,player, False)
    elif brett.board_state[y+1][x-1].endswith("King"):
        return sjekkdl(brett,x-1,y+1,player, False)
    elif player:
        #Hvis fiendens løper eller Dronning er på diagonalen er kongen i sjakk, hvis det er noe annet er ikke spillerens konge i sjakk
        if brett.board_state[y+1][x-1] == "EnemyBishop" or brett.board_state[y+1][x-1] == "EnemyQueen":
            return True
        else:
            return False
    elif not player:
        if brett.board_state[y+1][x-1] == "PlayerRook" or brett.board_state[y+1][x-1] == "PlayerQueen":
            #Hvis Spillerens løper eller Dronning er på diagonalen er kongen i sjakk, hvis det er noe annet er ikke Fiendens konge i sjakk
            return True
        elif first:
            if brett.board_state[y+1][x-1] == "PlayerPawn":
                return True
        else:
            return False
        

def sjekkdr(brett,x,y,player, first = True):
        #Basecase
    if x + 1 > 7 or y +1 >7:
        return False
    if brett.board_state[y+1][x+1] == None:
        #Sjekker neste rekursivt da nåværende lokasjon ikke gir info
        return sjekkdr(brett,x+1,y+1, player, False)
    elif brett.board_state[y+1][x+1].endswith("King"):
        return sjekkdr(brett,x+1,y+1,player, False)
    elif player:
        #Hvis fiendens løper eller Dronning er på diagonalen er kongen i sjakk, hvis det er noe annet er ikke spillerens konge i sjakk
        if brett.board_state[y+1][x+1] == "EnemyBishop" or brett.board_state[y+1][x+1] == "EnemyQueen":
            return True
        else:
            return False
    elif not player:
        if brett.board_state[y+1][x+1] == "PlayerBishop" or brett.board_state[y+1][x+1] == "PlayerQueen":
            #Hvis Spillerens løper eller Dronning er på diagonalen er kongen i sjakk, hvis det er noe annet er ikke Fiendens konge i sjakk
            return True
        elif first:
            if brett.board_state[y+1][x+1] == "PlayerPawn":
                return True
        else:
            return False
        
def sjekkknight(brett,x,y, player):
    for i in range(-2,3):
        for j in range(-2,3):
            if abs(j) == 1 and abs(i) == 2 or abs(j) == 2 and abs(i) == 1:
                if y+j >-1 and x + i > -1 and x +i < 8 and y + j < 8 and y-j >-1 and x - i > -1 and x -i < 8 and y - j < 8 :
                    if player:
                        if brett.board_state[y+j][x+i] is not None:
                            if brett.board_state[y+j][x+i]== "EnemyKnight":
                                return True
                    else:
                        if brett.board_state[y+j][x+i] is not None:
                            if brett.board_state[y+j][x+i]== "PlayerKnight":
                                return True

def ismovelegal(brett, i, j,x,y, player, unit):
    otherplater = True
    if player:
        otherplater = False
    brett2 = copy.deepcopy(brett)
    brett2.board_state[y][x] = unit
    brett2.board_state[j][i] = None
    (konx,kony) = findking(player,brett2)
    (kongx,kongy) = findking(otherplater,brett2)
    if (abs(konx-kongx) <= 1 and abs(kony-kongy) <= 1):
        print("hello, illegal moverino")
        return False
    
    if sjakksjekk(brett2,konx,kony,player):
        print("Sjakk")
        return False
    else:
        return True

def findking(player, board):
    for i in range(8):
        for j in range(8):
            if player:
                if board.board_state[j][i] == "PlayerKing":
                    print(f"Kongen er på {i}, {j}")
                    return (i,j)
            else:
                if board.board_state[j][i] == "EnemyKing":
                    return (i,j)
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
            
def input(size, board, screen):
    for event in pygame.event.get():
        unit = None
        if pygame.mouse.get_pressed()[0]:
            size
            (x,y) = pygame.mouse.get_pos()
            x = x // size
            y = y//size
            if x < 8 and y < 8:
                if board.board_state[y][x]:
                    print(board.board_state[y][x], y, x, screen)
                    unit = board.select(board.board_state[y][x], y, x, screen)
                    print(unit)
                    if unit is not None:
                        waitingforinput = True
                        while waitingforinput:
                            event = pygame.event.wait()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                (z,w) = pygame.mouse.get_pos()
                                z = z//size
                                w = w//size
                                if z < 8 and w < 8:
                                    board.Execute(unit, x,y,z,w,size, screen, player=True )
                                    waitingforinput = False
                                    return
                else:
                    print("click on board, but nothing on it")
            else:
                print("click outside game")
                if (x == 9 or x == 10) and (y == 1 or y == 0):
                    pygame.display.quit()
                    main("White")
                if (x == 11 or x == 12) and (y == 1 or y == 0):
                    pygame.display.quit()
                    main("Black")
                print(x,y)
                if (x == 11 or x == 12 or x == 13) and (y == 6 or y == 7):
                    pygame.display.quit()
                    sys.exit()


def user_interface(screen, height):
    offset = height
    option_font = pygame.font.SysFont('Helvetica', 30)
    option_white = option_font.render("White", False, (0,255,255) )
    option_black = option_font.render("Black", False, (0,255,255) )
    option_quit = option_font.render("Quit Game", False, (0,255,255))
    pygame.draw.rect(screen, (120,120,120),(offset + height//7, height//13, height//6, height//6 ) )
    pygame.draw.rect(screen, (120,120,120),(offset + height//2 - height//30, height//13, height//6, height//6 ) )
    pygame.draw.rect(screen, (120,120,120),(offset + height//2 - height//30, height//1.5, height//4, height//4 ) )
    screen.blit(option_white,(offset + height//6, height//8 ))
    screen.blit(option_black,(offset + height//2, height//8 ))
    screen.blit(option_quit,(offset + height//2, height//1.3))

def run(gameboard, Player, width = 1280, height = 720):
    screen = pygame.display.set_mode((width,height))
    while gameboard.running:
        screen.fill((0,0,0))
        draw_board(screen, height,Player,gameboard)
        user_interface(screen, height)
        input(height//8, gameboard, screen)
        pygame.display.flip()
        pygame.time.wait(100)




def main(color = "White"):
    __init__()
    Player = faction(color, True)
    Cpu = faction("Black", False)
    gameboard = board(Player)
    run(gameboard, Player)

main()