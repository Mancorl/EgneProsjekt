import pygame
import math
import sys
import copy
pygame.font.init()


def __init__():
    #initialiserer pygame
    pygame.init()
    pygame.display.set_caption("Sjakk")

#Initaliserer fraksjonene
class faction():
    def __init__(self, color, player):
        self.color = color
        self.player = player
        self.surrenderd = False
    
    
#Definerer verdien til brikkene (For cpu)
class Unitvalues:
    def __init__(self):
        unitlist = ["Pawn", "Rook", "Knight", "Bishop", "Queen", "King"]#0=pawn, 1=Rook, 2=Knight, 3 = Bishop, 4 = Queen, 5 = King1, 6 = King2 
        factions = ["Cpu", "Player"]# side 1 = player side0 = Cpu
        self.value_state = [[[[ 0  for _ in range(8)] for _ in range(8)] for _ in range(len(unitlist)+2)] for _ in range(len(factions)+1)]
        for unit in range(len(unitlist) +2):
            for side in range(len(factions)+1):
                for i in range(8):
                    for j in range(8):
                        
                        if unit == 0:
                            if side == 1:
                                self.value_state[side][unit][i][j] = 0.1 * (i) + 0.1*abs(7-j)
                            else:
                                self.value_state[side][unit][i][j] = 0.1 * abs(7-i) + 0.1*j
                        if unit == 1:
                            self.value_state[side][unit][i][j] = abs(0.1 * (3 - ((i-3)/3) ) * (3 - ((j-3)/3))) + 15
                        if unit == 2:
                            self.value_state[side][unit][i][j] = abs(0.1 * (1 - ((i-3)/3) ) * (1 - ((j-3)/3))) + 3
                        if unit == 3:
                            self.value_state[side][unit][i][j]= abs(0.1 * (abs(i-j))) + 5
                        if unit == 4:
                            self.value_state[side][unit][i][j] = abs(0.1 * (1 - ((i-3)/3) ) * (1 - ((j-3)/3))) + 30
                        if unit == 5:
                            if side == 1:
                                if j == 7:
                                    if i < 2 or i > 5:
                                        self.value_state[side][unit][i][j] = 100
                                    else:
                                        self.value_state[side][unit][i][j] = -500
                                else:
                                    self.value_state[side][unit][i][j] = -500
                            else:
                                if j == 0:
                                    if i < 2 or i > 5:
                                        self.value_state[side][unit][i][j] = 100
                                    else:
                                        self.value_state[side][unit][i][j] = -500
                                else:
                                    self.value_state[side][unit][i][j] = -500
                        if unit == 6:
                            if side == 1:
                                self.value_state[side][unit][i][j] = 100
                            else:
                                self.value_state[side][unit][i][j] = 100

        
class board():
    def __init__(self, Player):
        #Definerer variabler som blir brukt for å holde kontroll på lovlige trekk
        self.running = True
        self.board_state = [[None for _ in range(8)] for _ in range(8)]
        self.en_passant = False
        self.PlayerRokkerright = True
        self.PlayerRokkerleft = True
        self.enemyRokkerright = True
        self.enemyRokkerleft = True
        self.turntomove = "White"
        self.en_passant_counter = self.turntomove
        self.prev_i = -100
        self.prev_j = -100
        
        #Initialiserer brettet dersom spiller er hvit
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
                        
                        #Initialiserer spillet dersom spiller er sort
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
                        
    #Select funksjonen viser de lovlige trekkene til en valgt brikke
    def select(self, unit, i, j, screen):
        
        if self.en_passant_counter == self.turntomove:
            self.en_passant = "False"
        
        y = screen.get_height()
        centering = y//8
        
        #Viser lovlige trekk for bonden
        if unit == "PlayerPawn":
            #an passant
            if self.en_passant and (j == 3) and (self.prev_i == i+1  or self.prev_i == i-1) and self.prev_i != i:
                pygame.draw.circle(screen, (120,120,120), (self.prev_i * centering + centering//2, (self.prev_j - 1) *centering + centering//2), centering//2)
            
            #Starttrekk, hvor det er lov å bevege brikken to steg fremover
            if i == 6:
                if self.board_state[i-1][j] is None:
                    pygame.draw.circle(screen, (255,255,0), ((j) * centering + centering//2, (i-1) *centering + centering//2), centering//2)
                    if self.board_state[i-2][j] is None:
                        pygame.draw.circle(screen, (255,255,0), ((j) * centering + centering//2,(i-2) *centering + centering//2), centering//2)
            elif self.board_state[i-1][j] is None:
                pygame.draw.circle(screen, (255,255,0), ((j) * centering + centering//2, (i-1) *centering + centering//2), centering//2)
                
            #Viser dersp, det er lov å ta en brikke opp og mot høyre dersom det er en fiendtlig brikke
            try:
                if self.board_state[i-1][j+1] != None:
                    if self.board_state[i-1][j+1].startswith("Enemy"):
                        pygame.draw.circle(screen, (255, 0, 0), ((j + 1) * centering + centering // 2, (i-1) * centering + centering // 2), centering // 4)
            except:
                pass
            
            #Viser dersp, det er lov å ta en brikke opp og mot venstre dersom det er en fiendtlig brikke
            try:
                if self.board_state[i-1][j-1] != None: 
                    if self.board_state[i-1][j-1].startswith("Enemy"):
                        pygame.draw.circle(screen, (255, 0, 0), ((j - 1) * centering + centering // 2, (i-1) * centering + centering // 2), centering // 4)
            except:
                pass
            
            #Viser lovlige trekk for tårnet
        if unit == "PlayerRook":
            self.moveRight(i,j,screen,centering)
            self.moveLeft(i,j,screen,centering)
            self.moveUp(i,j,screen,centering)
            self.moveDown(i,j,screen,centering)
                
                
        #Viser lovlige trekk for hesten
        if unit == "PlayerKnight":
            if i + 2 < 8 and j +1 <8:
                if self.board_state[i + 2][j + 1] is not None:
                    if self.board_state[i + 2][j + 1].startswith("Player") == False:
                        pygame.draw.circle(screen, (255, 0, 0), ((j + 1) * centering + centering // 2, (i +2) * centering + centering // 2), centering // 4)
                        
                if self.board_state[i + 2][j+1] is None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j + 1) * centering + centering // 2, (i +2) * centering + centering // 2), centering // 2)
                    
            if i + 1 < 8 and j +2 <8:
                if self.board_state[i + 1][j + 2] is not None:
                    if self.board_state[i + 1][j + 2].startswith("Player") == False:
                        pygame.draw.circle(screen, (255, 0, 0), ((j + 2) * centering + centering // 2, (i+ 1) * centering + centering // 2), centering // 4)
                if self.board_state[i + 1][j+2] is None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j + 2) * centering + centering // 2, (i +1) * centering + centering // 2), centering // 2)
                    
            if i + 1 < 8 and j -2 >-1:
                if self.board_state[i + 1][j - 2] is not None:
                    if self.board_state[i + 1][j - 2].startswith("Player") == False:
                        pygame.draw.circle(screen, (255, 0, 0), ((j - 2) * centering + centering // 2, (i +1) * centering + centering // 2), centering // 4)
                if self.board_state[i + 1][j-2] is None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j - 2) * centering + centering // 2, (i +1) * centering + centering // 2), centering // 2)
            
            if i - 1 > -1 and j -2 >-1:
                if self.board_state[i - 1][j - 2] is not None:
                    if self.board_state[i - 1][j - 2].startswith("Player") == False:
                        pygame.draw.circle(screen, (255, 0, 0), ((j - 2) * centering + centering // 2, (i -1) * centering + centering // 2), centering // 4)
                if self.board_state[i - 1][j-2] is None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j - 2) * centering + centering // 2, (i -1) * centering + centering // 2), centering // 2)
            
            if i + 2 < 8 and j -1 >-1:
                if self.board_state[i + 2][j - 1] is not None:
                    if self.board_state[i + 2][j - 1].startswith("Player") == False:
                        pygame.draw.circle(screen, (255, 0, 0), ((j - 1) * centering + centering // 2, (i +2) * centering + centering // 2), centering // 4)
                if self.board_state[i + 2][j-1] is None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j - 1) * centering + centering // 2, (i +2) * centering + centering // 2), centering // 2)
                    
            if i - 1 > -1 and j + 2 <8:
                if self.board_state[i - 1][j + 2] is not None:
                    if self.board_state[i - 1][j + 2].startswith("Player") == False:
                        if self.board_state[i - 1][j + 2].startswith("Player") == False:
                            pygame.draw.circle(screen, (255, 0, 0), ((j + 2) * centering + centering // 2, (i -1) * centering + centering // 2), centering // 4)
                if self.board_state[i - 1][j+2] is None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j + 2) * centering + centering // 2, (i -1) * centering + centering // 2), centering // 2)
            
            if i - 2 > -1 and j + 1 <8:
                if self.board_state[i - 2][j + 1] is not None:
                    if self.board_state[i - 2][j + 1].startswith("Player") == False:
                        if self.board_state[i - 2][j + 1].startswith("Player") == False:
                            pygame.draw.circle(screen, (255, 0, 0), ((j + 1) * centering + centering // 2, (i -2) * centering + centering // 2), centering // 4)
                if self.board_state[i - 2][j+1] is None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j + 1) * centering + centering // 2, (i -2) * centering + centering // 2), centering // 2)
            
            if i - 2 > -1 and j - 1 >-1:
                if self.board_state[i - 2][j - 1] is not None:
                    if self.board_state[i - 2][j - 1].startswith("Player") == False:
                        if self.board_state[i - 2][j - 1].startswith("Player") == False:
                            pygame.draw.circle(screen, (255, 0, 0), ((j - 1) * centering + centering // 2, (i -2) * centering + centering // 2), centering // 4)
                if self.board_state[i - 2][j-1] is None:
                    pygame.draw.circle(screen, (255, 255, 0), ((j - 1) * centering + centering // 2, (i -2) * centering + centering // 2), centering // 2)
            
        #Lovlige trekk for løperen
        if unit == "PlayerBishop":
            self.bishopmovesul(i,j,screen,centering)
            self.bishopmovesdl(i,j,screen,centering)
            self.bishopmovesur(i,j,screen,centering)
            self.bishopmovesdr(i,j,screen,centering)
        #viser lovlige trekk for dronningen
        if unit == "PlayerQueen":
            self.bishopmovesul(i,j,screen,centering)
            self.bishopmovesdl(i,j,screen,centering)
            self.bishopmovesur(i,j,screen,centering)
            self.bishopmovesdr(i,j,screen,centering)
            self.moveDown(i,j,screen,centering)
            self.moveUp(i,j,screen,centering)
            self.moveLeft(i,j,screen,centering)
            self.moveRight(i,j,screen,centering)
            #Lovlige trekk for konen
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
            if self.board_state[x - 1][y - 1] is None and blocked == False:
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
            if self.board_state[x + 1][y - 1] is None and blocked == False:
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
            if self.board_state[x - 1][y + 1] is None and blocked == False:
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
            if self.board_state[x + 1][y + 1] is None and blocked == False:
                pygame.draw.circle(screen, (255, 255, 0), ((y + 1) * centering + centering // 2, (x + 1) * centering + centering // 2), centering // 2)
                if not king:
                    self.bishopmovesdr(x+1, y+1, screen, centering)
            if self.board_state[x+1][y+1] is not None:
                if self.board_state[x+1][y+1].startswith("Enemy"):
                    blocked = True
                    pygame.draw.circle(screen, (255, 0, 0), ((y + 1) * centering + centering // 2, (x + 1) * centering + centering // 2), centering // 4)

    def moveDown(self, x, y,screen, centering,king = False):
        if x + 1 < 8:
            if self.board_state[x+1][y] is None:
                pygame.draw.circle(screen, (255, 255, 0), ((y) * centering + centering // 2, (x + 1) * centering + centering // 2), centering // 2)
                if not king:
                    self.moveDown(x+1, y, screen, centering)
            if self.board_state[x+1][y] is not None:
                if self.board_state[x+1][y].startswith("Enemy"):
                    pygame.draw.circle(screen, (255, 0, 0), ((y) * centering + centering // 2, (x+1) * centering + centering // 2), centering // 4)
        
    def moveUp(self, x, y,screen, centering,king = False):
        if x - 1 > -1:
            if self.board_state[x-1][y] is None:
                pygame.draw.circle(screen, (255, 255, 0), ((y) * centering + centering // 2, (x - 1) * centering + centering // 2), centering // 2)
                if not king:
                    self.moveUp(x-1, y, screen, centering)
            if self.board_state[x-1][y] is not None:
                if self.board_state[x-1][y].startswith("Enemy"):
                    pygame.draw.circle(screen, (255, 0, 0), ((y) * centering + centering // 2, (x-1) * centering + centering // 2), centering // 4)
                    
    def moveLeft(self, x, y,screen, centering,king = False):
        if y - 1 > -1:
            if self.board_state[x][y-1] is None:
                pygame.draw.circle(screen, (255, 255, 0), ((y-1) * centering + centering // 2, (x) * centering + centering // 2), centering // 2)
                if not king:
                    self.moveLeft(x, y-1, screen, centering)
            if self.board_state[x][y-1] is not None:

                if self.board_state[x][y-1].startswith("Enemy"):

                    pygame.draw.circle(screen, (255, 0, 0), ((y-1) * centering + centering // 2, (x) * centering + centering // 2), centering // 4)
                    
    def moveRight(self, x, y,screen, centering, king = False):
        if y + 1 < 8:
            if self.board_state[x][y+1] is None:
                pygame.draw.circle(screen, (255, 255, 0), ((y+1) * centering + centering // 2, (x) * centering + centering // 2), centering // 2)
                if not king:
                    self.moveRight(x, y+1, screen, centering)
            if self.board_state[x][y+1] is not None:

                if self.board_state[x][y+1].startswith("Enemy"):

                    pygame.draw.circle(screen, (255, 0, 0), ((y+1) * centering + centering // 2, (x) * centering + centering // 2), centering // 4)
    def rokadesjekk(self,x,y,screen,centering):
        if self.PlayerRokkerleft:
            try:
                if self.board_state[7][0] == "PlayerRook":
                    
                    if self.board_state[7][1] is None and self.board_state[7][2] is None:
                        if self.board_state[7][3] is None or self.board_state[7][3].endswith("King"):
                            pygame.draw.circle(screen, (255, 255, 0), ((y-2) * centering + centering // 2, (x) * centering + centering // 2), centering // 2)
            except:
                pass
        if self.PlayerRokkerright:
            try:
                if self.board_state[7][7] == "PlayerRook":
                    
                    if self.board_state[7][5] is None and self.board_state[7][6] is None:
                        if self.board_state[7][4] is None or self.board_state[7][4].endswith("King"):
                            pygame.draw.circle(screen, (255, 255, 0), ((y+2) * centering + centering // 2, (x) * centering + centering // 2), centering // 2)
            except:
                pass
            
            
                    
        
    #Execute garderer om et trekk er lovlig, og gjør trekket
    def Execute(self, unit, i,j,x,y,square_size, screen, player = False, showgraphics = True):
        #Hjelper for å la både cpu og spiller bruke execute for å gjøre trekk
        enemyvar = "Enemy"
        if player == False:
            enemyvar = "Player"
        if unit is None:
            return
        playerfactor = 1
        playercolor = ((255,255,255))
        if not player:
            playerfactor = -1
            playercolor = ((0,0,0))
        
        #Lovlige bondetrekk
        if unit.endswith("Pawn"):
            #en passant
            if self.en_passant:
                if self.prev_i != None and self.en_passant_counter != self.turntomove:
                    if (self.prev_i == i + 1 or self.prev_i == i -1) and self.prev_j == j:
                        if ((x == i +1 or x == i -1) and y == j -1*playerfactor and ismovelegal(self,i,j,x,y,player,unit)):
                            self.board_state[j][i] = None
                            self.board_state[y][x] = unit
                            self.board_state[self.prev_j][self.prev_i] = None
                            
            #Tar andre brikker
            if ((x == i - 1 or x == i+1) and (y == j-1 * playerfactor and y != j)):
                try:
                    if self.board_state[y][x].startswith(enemyvar):
                        if ismovelegal(self,i,j,x,y,player,unit):
                            self.board_state[j][i] = None
                            self.board_state[y][x] = unit
                except:
                    pass
            #Går fremover
            if (y == j - 1 * playerfactor and x == i) and ismovelegal(self,i,j,x,y,player,unit):
                if self.board_state[j-1*playerfactor][i] is None:
                    self.board_state[j][i] = None
                    self.board_state[y][x] = unit
            #Håndterer Forfremmelse
            if ((player and y == 0) or (not player and y == 7)):
                if self.board_state[y][x] is None:
                    return
                while self.board_state[y][x].endswith("Pawn"):
                    if showgraphics == False:
                        self.board_state[y][x] = "EnemyQueen"
                        return
                        
                    draw_rook(screen, x*square_size, (y + 3 * playerfactor)*square_size,square_size, color=playercolor)
                    draw_knight(screen, x*square_size, (y + 2 * playerfactor)*square_size,square_size, color=playercolor)
                    draw_bishop(screen, x*square_size, (y + 1 * playerfactor)*square_size ,square_size, color=playercolor)
                    draw_queen(screen, x*square_size, y*square_size,square_size, color=playercolor)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if pygame.mouse.get_pressed()[0]:
                            (a,e) = pygame.mouse.get_pos()
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
                                        
                        
            #Dersom første trekk beveger seg fremover med to
            if (((y == j - 2 * playerfactor and ((player == True and j == 6) or (player == False and j == 1)) and x == i)) and ismovelegal(self,i,j,x,y,player,unit)): 
                if self.board_state[y][x] is None and self.board_state[y+1*playerfactor][x] is None:
                    self.board_state[j][i] = None
                    self.board_state[y][x] = unit
                    self.en_passant = True
                    self.en_passant_counter = self.turntomove
                    self.prev_j = y
                    self.prev_i = x
        #Håndterer kongetrekk
        if unit.endswith("Knight"):
            if ((((y == j + 2 or y == j -2) and (x == i +1 or x == i - 1)) or ((y == j +1 or y == j - 1) and (x == i + 2 or x == i - 2))) and ismovelegal(self,i,j,x,y,player,unit)):
                try:
                    if self.board_state[y][x].startswith(playerfactor):
                        return
                except:
                    pass

                try:
                    if self.board_state[y][x].startswith(enemyvar):
                        self.board_state[j][i] = None
                        self.board_state[y][x] = unit
                except:
                    pass
                
                if self.board_state[y][x] is None:
                    self.board_state[j][i] = None
                    self.board_state[y][x] = unit
                    
        #Håndterer løpertrekk
        if unit.endswith("Bishop") and ismovelegal(self,i,j,x,y,player,unit):
            if self.bishopmove(j,i,y,x, player):
                self.board_state[j][i] = None
                self.board_state[y][x] = unit
        #Tårn
        if unit.endswith("Rook"):
            if self.rockmove(j,i,y,x,player):
                if (j == y or x == i) and ismovelegal(self,i,j,x,y,player,unit):
                    self.board_state[j][i] = None
                    self.board_state[y][x] = unit
        #Dronning
        if unit.endswith("Queen"):
            if (self.bishopmove(j,i,y,x, player) or (self.rockmove(j,i,y,x, player) and (x == i or y == j)))and ismovelegal(self,i,j,x,y,player,unit):
                self.board_state[j][i] = None
                self.board_state[y][x] = unit
        #Konge
        if unit.endswith("King"):
            if (self.bishopmove(j,i,y,x,player, True) or ((self.rockmove(j,i,y,x, player, True) and (x == i or y == j)))) and ismovelegal(self,i,j,x,y,player,unit):
                self.board_state[j][i] = None
                self.board_state[y][x] = unit
                if player:
                    self.PlayerRokkerleft = False
                    self.PlayerRokkerright = False
                else:
                    self.enemyRokkerleft = False
                    self.enemyRokkerright = False
            if (x == i-2 or x == i + 2) and ismovelegal(self,i,j,x,y,player,unit):
                self.Kongerokade(i,j,x,y, player)
                    
                
    def rockmove(self,j,i,y,x,player, king = False):
        #Håndterer logikken bak tårntrekk
        playervar = "Player"
        enemyvar = "Enemy"
        if player == False:
            playervar = "Enemy"
            enemyvar = "Player"
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
                        if self.board_state[j+k][i].startswith(playervar):
                            return False
                    except:
                        pass
                    return True
                try:
                    if(self.board_state[j+k][i].startswith(enemyvar) or self.board_state[j+k][i].startswith(playervar)):
                        up = False
                except:
                    pass
            if down:
                if j-k == y:
                    try:
                        if self.board_state[j-k][i].startswith(playervar):
                            return False
                    except:
                        pass
                    return True
                try:
                    if(self.board_state[j-k][i].startswith(enemyvar) or self.board_state[j-k][i].startswith(playervar)):
                        down = False
                except:
                    pass
            if left:
                if i-k == x:
                    try:
                        if self.board_state[j][i-k].startswith(playervar):
                            return False
                    except:
                        pass
                    return True
                try:
                    if(self.board_state[j][i-k].startswith(enemyvar) or self.board_state[j][i-k].startswith(playervar)):
                        left = False
                except:
                    pass
            if right:
                if i+k == x:
                    try:
                        if self.board_state[j][i+k].startswith(playervar):
                            return False
                    except:
                        pass
                    return True
                try:
                    if(self.board_state[j][i+k].startswith(enemyvar) or self.board_state[j][i+k].startswith(playervar)):
                        right = False
                except:
                    pass
        return False
    
    #Håndterer logikken til løpertrekk (med speisaltilfellet dersom brikken er kongen)
    def bishopmove(self, i , j, x,y, player, king = False):
        playervar = "Player"
        enemyvar = "Enemy"
        if player == False:
            playervar = "Enemy"
            enemyvar = "Player"
        ur = True
        dr = True
        ul = True
        dl = True
        rangevar = 8
        if king:
            rangevar = 2
        #Itererer gjennom lovlige trekk i en forløkke, tbh virker det som en mye bedre måte slik jeg implementerte det senere i sjakksjekk funksjonene
        for k in range(1,rangevar):
            if True:
                
                if dr:
                    if (i + k == x and j + k == y):
                        try:
                            if self.board_state[i+k][j+k].startswith(playervar):
                                return False
                        except:
                            pass
                        return True
                    try:
                        if(self.board_state[i+k][j+k].startswith(enemyvar) or self.board_state[i+k][j+k].startswith(playervar)):
                            
                            dr = False
                    except:
                        pass
                    
                    
                if dl:
                    if (i + k == x and j - k == y):
                        try:
                            if self.board_state[i+k][j-k].startswith(playervar):
                                return False
                        except:
                            pass
                        
                        return True
                    
                    try:
                        if(self.board_state[i+k][j-k].startswith(enemyvar) or self.board_state[i+k][j-k].startswith(playervar)):
                            dl = False
                    except:
                        pass
                if ur:
                    if (i - k == x and j + k == y ):
                        try:
                            if self.board_state[i-k][j+k].startswith(playervar):
                                return False
                        except:
                            pass
                        return True
                    try:
                        
                        if(self.board_state[i-k][j+k].startswith(enemyvar) or self.board_state[i-k][j+k].startswith(playervar)):
                            ur = False
                    except:
                        pass
                if ul:
                    if (i - k == x and j - k == y):
                        try:
                            if self.board_state[i-k][j-k].startswith(playervar):
                                return False
                        except:
                            pass
                        return True
                    try:
                        if(self.board_state[i-k][j-k].startswith(enemyvar) or self.board_state[i-k][j-k].startswith(playervar)):
                            ul = False
                    except:
                        pass
                    
        return False
    #Logikk for å håndtere rokade
    def Kongerokade(self, i,j,x,y, player = True):
        if self.PlayerRokkerleft and player:
            try:
                if self.board_state[7][0] == "PlayerRook":
                    
                    if self.board_state[7][1] is None and self.board_state[7][2] is None:
                        if self.board_state[7][3] is None or self.board_state[7][3].endswith("King"):
                            self.board_state[i][j] = None
                            self.board_state[7][0] = None
                            self.board_state[j][i-1] = "PlayerRook"
                            self.board_state[j][i-2] = "PlayerKing"
            except:
                pass
        if self.PlayerRokkerright and player:
            try:
                if self.board_state[7][7] == "PlayerRook":
                    
                    if self.board_state[7][5] is None and self.board_state[7][6] is None:
                        if self.board_state[7][4] is None or self.board_state[7][4].endswith("King"):
                            self.board_state[j][i] = None
                            self.board_state[7][7] = None
                            self.board_state[j][i+1] = "PlayerRook"
                            self.board_state[j][i+2] = "PlayerKing"
            except:
                pass
        if not player:
            if self.enemyRokkerleft:
                try:
                    if self.board_state[0][0] == "EnemyRook":
                    
                        if self.board_state[0][1] is None and self.board_state[0][2] is None:
                            if self.board_state[0][3] is None or self.board_state[0][3].endswith("King"):
                                self.board_state[i][j] = None
                                self.board_state[0][0] = None
                                self.board_state[j][i-1] = "EnemyRook"
                                self.board_state[j][i-2] = "EnemyKing"
                except:
                    pass
            if self.enemyRokkerright:
                try:
                    if self.board_state[0][7] == "EnemyRook":
                    
                        if self.board_state[0][5] is None and self.board_state[0][6] is None:
                            if self.board_state[0][4] is None or self.board_state[0][4].endswith("King"):
                                self.board_state[j][i] = None
                                self.board_state[0][7] = None
                                self.board_state[j][i+1] = "EnemyRook"
                                self.board_state[j][i+2] = "EnemyKing"
                except:
                    pass
            
        
        
        
        return

def sjakksjekk(brett,x,y, player):
    #Sjekker alle rettninger om kongen er i sjakk
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
    elif brett.board_state[y][x+1].endswith("King"):
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
        #Basecase
    if y - 1 < 0:
        return False
    if brett.board_state[y-1][x] is None:
        #Sjekker neste rekursivt da nåværende lokasjon ikke gir info
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
    if y + 1 > 7:
        return False
    if brett.board_state[y+1][x] is None:
        #Sjekker neste rekursivt da nåværende lokasjon ikke gir info
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
    if brett.board_state[y-1][x+1] is None:
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
    if brett.board_state[y-1][x-1] is None:
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
    if brett.board_state[y+1][x-1] is None:
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
        if brett.board_state[y+1][x-1] == "PlayerBishop" or brett.board_state[y+1][x-1] == "PlayerQueen":
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
    if brett.board_state[y+1][x+1] is None:
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
        
        
        #Sjekker om kongen er sjakket av en hest
def sjekkknight(brett,x,y, player):
    for i in range(-2,3):
        for j in range(-2,3):
            if (abs(j) == 1 and abs(i) == 2) or (abs(j) == 2 and abs(i) == 1):
                if y+j >-1 and x + i > -1 and x +i < 8 and y + j < 8 and y-j >-1 and x - i > -1 and x -i < 8 and y - j < 8 :
                    if player:
                        if brett.board_state[y+j][x+i] is not None:
                            if brett.board_state[y+j][x+i]== "EnemyKnight":
                                return True
                    if not player:
                        if brett.board_state[y+j][x+i] is not None:
                            if brett.board_state[y+j][x+i]== "PlayerKnight":
                                return True
    return False


#sjekker at et trekk er lovlig
def ismovelegal(brett, i, j,x,y, player, unit):
    otherplater = True
    if player:
        otherplater = False
    brette = copy.deepcopy(brett)
    brette.board_state[y][x] = unit
    brette.board_state[j][i] = None
    #Finner kongen
    try:
        (konx,kony) = findking(player,brette)
    except:
        konx = x
        kony = y
    try:
        (kongx,kongy) = findking(otherplater,brette)
    except:
        kongx = x
        kongy = y
    #Etter mye debugging fant jeg ut at det er lettest å sjekke at kongene ikke kommer for nærme hverandre her, da andre løsninger andre plasser fort gav vanskelige bugs
    if (abs(konx-kongx) <= 1 and abs(kony-kongy) <= 1):
        return False
    
    if sjakksjekk(brette,konx,kony,player):
        #sjekker for sjakk, dersom ingen sjakk etter trekket er trekket lovlig
        return False
    else:
        return True

#Hjelpegunksjon for ismovelegal. Finner koordinatene til kongene
def findking(player, board):
    for i in range(8):
        for j in range(8):
            if player:
                if board.board_state[j][i] == "PlayerKing":
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
    

#Sjekker at lovlige trekk eksisterer, slik at spillet kan erklære en vinner eller patt
def Legal_moves_exist(brett,size,screen, player):
    brett2 = copy.deepcopy(brett)
    brikkeliste = ["EnemyPawn","EnemyKnight", "EnemyRook", "EnemyBishop", "EnemyQueen", "EnemyKing"]
    if player:
        brikkeliste = ["PlayerPawn","PlayerKnight", "PlayerRook", "PlayerBishop", "PlayerQueen", "PlayerKing"]
    #Itererer gjennom hvert eneste trekk for hver eneste brikke, dersom den finner en lovlig returnerer den umiddelbart. Ikke optimal implementasjon da den er O(n**5) men den funker
    for brikke in brikkeliste:
        for x in range(8):
            for y in range(8):
                if brett2.board_state[y][x] == brikke:
                    for i in range(8):
                        for j in range(8):
                            brett2.Execute(brikke,x,y,i,j,size,screen, player=player)
                            if brett.board_state[y][x] != brett2.board_state[y][x]:
                                return True
    return False


#Finner alle lovlige trekk for cpuen minst effektive funksjonen i hele programmet da denne er O(n**5) og må kjøre gjennom alle variabler i motsetning til legal_moves_exist
def Do_legal_move(brett, size, screen, player):
    brett2 = copy.deepcopy(brett)
    lawful_move_list = []
    brikkeliste = ["EnemyPawn","EnemyKnight", "EnemyRook", "EnemyBishop", "EnemyQueen", "EnemyKing"]
    if player:
        brikkeliste = ["PlayerPawn","PlayerKnight", "PlayerRook", "PlayerBishop", "PlayerQueen", "PlayerKing"]#Støtter dypere leting dersom en vil ha det
    for brikke in brikkeliste:
        for x in range(8):
            for y in range(8):
                if brett2.board_state[y][x] == brikke:
                    for i in range(8):
                        for j in range(8):
                            brett_temp = copy.deepcopy(brett)
                            brett_temp.Execute(brikke,x,y,i,j,size,screen, player, False)
                            if brett.board_state[y][x] != brett_temp.board_state[y][x]:
                                if not sjakksjekk(brett_temp,i,j,False):
                                    lawful_move_list.append(brett_temp)#samler en liste av alle lovlige trekk som returneres i slutten
                                else:
                                    continue
                                    #dobbel else som følge av debug
                            else:
                                continue
                                
    return lawful_move_list
    
    #Sjekker verdiene på hvert brett, slik at vi finner det beste trekket, verdiene kan endres direkte her, eller for de individuelle brikkene i values klassen
def Checkoardvalues(board, values):
    sum = 0
    #self.value_state[side][unit][i][j]
    for unit in range(6):
        for i in range(8):
            for j in range(8):
                if board.board_state[j][i] is not None:
                    if "Player" in board.board_state[j][i]:
                        sum -= 10* values.value_state[1][unit][i][j]#Ved 10X begynner cpuen faktisk å ta en brikke engang i blandt
                    else:
                        sum += values.value_state[0][unit][i][j]
                    
    return sum
                    
    #Returnerer trekket cpuen ønsker å ta
def Makecpumove(board, player, values, size, screen, cpu):
    sum = -9001
    index = 0
    movelist = [[] for _ in range(18)]
    movevalue = [[] for _ in range(9)]
    movelist = Do_legal_move(board, size,screen,False)
    for v in range(len(movelist)):
        movevalue.append(Checkoardvalues(movelist[v], values))
    #Dersom ai-en av en eller annen grunn ikke finner et trekk overgir den seg
    if len(movelist) == 0 or movelist[0] == []:
        cpu.surrenderd = True
        return board

    #Finner trekket som gir cpu best verdi iflg checkboardvalues, og velger det
    for value in range(len(movevalue[0])):
        current_value = movevalue[0][value]
        if current_value > sum:
            sum = current_value
            index = value
    
    return movelist[index]
    
#Tegner brettet
def draw_board(screen,height, Player, Gameboard):
    square_size = height//(8)
    vertical_list = []
    horizontal_list = [[]]
    enemyColor = ((50,50,50))
    playerColor = ((200,200,200))
    #Tegner brettet for sort i samme slengen dersom du vil spille som sort
    if Player.color == "Black":
        enemyColor = ((255,255,255))
        playerColor = ((0,0,0))
    #Definerer horisontal og vertikal liste
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
    #Initialiserer brikkene på brettet og farger rutene
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
            
            akk += 1


        akk += 1
#Tar spillerens input
def input(size, board, screen,cpu):
    for event in pygame.event.get():
        event = pygame.event.wait()
        unit = None
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            size
            (x,y) = pygame.mouse.get_pos()
            x = x // size
            y = y//size
            if x < 8 and y < 8:
                if board.board_state[y][x] and Legal_moves_exist(board, size, screen, False) == True:
                    unit = board.select(board.board_state[y][x], y, x, screen)
                    if unit is not None:
                        waitingforinput = True
                        while waitingforinput:
                            event = pygame.event.wait()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                (z,w) = pygame.mouse.get_pos()
                                z = z//size
                                w = w//size
                                if z < 8 and w < 8:
                                    #Hvor z og w representerer klikk på forksjellige deler av brettet
                                    board2 = copy.deepcopy(board)
                                    board.Execute(unit, x,y,z,w,size, screen, player=True)
                                    #Fortsetter kun dersom Execute faktisk har gjort endringer på brettet
                                    if board2.board_state !=board.board_state:
                                        waitingforinput = False
                                        pygame.time.wait(100)
                                        board.turntomove = cpu.color
                                        return
                                    return
                                
                else:
                    print("click on board, but nothing on it")
            else:
                if (x == 9 or x == 10) and (y == 1 or y == 0):
                    pygame.display.quit()
                    main("White")
                if (x == 11 or x == 12) and (y == 1 or y == 0):
                    pygame.display.quit()
                    main("Black")
                if (x == 11 or x == 12 or x == 13) and (y == 6 or y == 7):
                    pygame.display.quit()
                    sys.exit()


#Tegner brukerinterfacet som lar spilleren velge annen farge eller avslutte spillet
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


#Kjøreløkken som kjører spillet
def run(gameboard, Player,cpu,values, width = 1280, height = 720):
    checkvar = False
    if Player.color == "White":
        checkvar = True
    screen = pygame.display.set_mode((width,height))
    while gameboard.running:
        screen.fill((0,0,0))
        draw_board(screen, height,Player,gameboard)
        user_interface(screen, height)
        pygame.display.flip()
        pygame.time.wait(100)
        
        
        if gameboard.turntomove == Player.color:
            input(height//8, gameboard, screen, cpu)
            checkvar = False
        elif gameboard.turntomove == cpu.color:
            gameboard = Makecpumove(gameboard, Player, values, height//8, screen,cpu)
            gameboard.turntomove = Player.color
            
            checkvar = True
            
        
        #Seier/Uavgjort skjermen som popper opp
        if Legal_moves_exist(gameboard, height//8, screen, checkvar) == False or cpu.surrenderd == True:
                option_font = pygame.font.SysFont('Helvetica', 96)
                player = False
                while True:
                    if player:
                        (x,y)=findking(player,gameboard)
                        screen.fill((0,0,0))
                        if sjakksjekk(gameboard,x,y,player):
                            option = option_font.render("Game over, you lose", False, (0,255,255) )
                        else:
                            option = option_font.render("Game over, Draw", False, (0,255,255) )
                    
                        screen.blit(option,(height//6, height//2 ))
                        user_interface(screen,height)
                        input(height//8, gameboard, screen, cpu)
                        pygame.display.flip()
                    else:
                        (x,y)=findking(player,gameboard)
                        screen.fill((0,0,0))
                    
                        if sjakksjekk(gameboard,x,y,player):
                            option = option_font.render("Game over, you win", False, (0,255,255) )
                        else:
                            option = option_font.render("Game over, Draw", False, (0,255,255) )
                        
                        if cpu.surrenderd:
                            option_font = pygame.font.SysFont('Helvetica', 58)
                            option = option_font.render("Game over, you win, the ai surrenders", False, (0,255,255) )

                        screen.blit(option,(height//6, height//2 ))
                        user_interface(screen,height)
                        input(height//8, gameboard, screen,cpu)
                        pygame.display.flip()
            



#Main funksjonen som starter spillet
def main(color = "White"):
    __init__()
    cpu_color = "Black"
    if color == "Black":
        cpu_color = "White"
    Player = faction(color, True)
    Cpu = faction(cpu_color, False)
    gameboard = board(Player)
    values = Unitvalues()
    run(gameboard, Player, Cpu, values)

#Kaller main
main()