#===============================================================================
#Purpose: To draw the board and player starting positions inorder to play 
#         IceBreaker
#By Thomas Charlebois
#===============================================================================
from graphics import *
print('CMPT_103_IceBreaker.py by Thomas Charlebois')
#-------------------------------------------------------------------------------
# Constants
WIN_W, WIN_H = 400, 440
TILE_W, TILE_H = 40, 40 # Tile size

#-------------------------------------------------------------------------------
# Variables
win = None
tile_list = [] # stores tile position
current_player = 'red' # stores whos turn it is
x1, y1 = 0, 3 # stores (x, y) coordinates for red
x2, y2 = 9, 3 # stores (x, y) coordinates for Blue
ice_location = set() # stores set with coordinates of each broken ice location
playertxt = None # stores text for displaying current player
legal = False # stores whether a move is legal or illegal
#-------------------------------------------------------------------------------
# Helper Functions

# Displays splash screen
# Takes no parameters
# Returns nothing
def splash_screen():
    global win, WIN_W, WIN_H
    while True:
        win.setBackground('light blue')
        txt1 = Text(Point(WIN_W // 2, WIN_H // 4), 'Ice Breaker')
        txt2 = Text(Point(WIN_W // 2, WIN_H // 4 + 30), 'Click to Play!')
        txt1.setSize(20)
        txt2.setSize(20)
        txt1.draw(win)
        txt2.draw(win)
        win.getMouse()
        txt1.undraw()
        txt2.undraw()
        break

# Draws the board
# Takes no parameters
# Returns tile_list with all tile locations
def draw_board():
    global win, tile_list
    for row in range(7):
        tile_list.append([])
        for col in range(10):
            x = col * TILE_W
            y = row * TILE_H
            r = Image(Point(x + 20, y + 20), "ice-white.gif")
            tile_list[row].append(r)
            tile_list[row][col].undraw()
            tile_list[row][col].draw(win)
    
    return tile_list

# Draws the player onto the board
# Takes no parameters
# Returns nothing
def player():
    player_0 = Image(Point (20, 140), "player-0.gif")
    player_1 = Image(Point(380.0, 140),"player-1.gif")
    tile_list[3][0] = player_0
    tile_list[3][9] = player_1
    tile_list[3][0].draw(win)
    tile_list[3][9].draw(win)

# Gets the click coordinates and returns them into bx, by
# takes no parameters
# Returns bx, by
def get_click():
    pt = win.getMouse()
    mx, my = int(pt.getX()), int(pt.getY())
    bx, by = mx // TILE_W, my // TILE_H
    return bx, by

# Moves the current player if legal to coordinates bx, by
# Takes mouse coordinates (bx, by)
# Returns tile_list updated with player 
def move_player(bx, by):
    global win, tile_list, current_player
    global x1, y1, x2, y2
    if current_player == 'red':
        player = Image(Point(bx * TILE_W +20, by * TILE_H + 20), "player-0.gif")
        tile_list[by][bx] = player # overwrites board piece with player piece
        tile_list[by][bx].draw(win)
        x1, y1 = bx, by # saves mouse coordinates to current player location 
    elif current_player == 'blue':
        player = Image(Point(bx * TILE_W +20, by * TILE_H + 20), "player-1.gif")
        tile_list[by][bx] = player # overwrites board piece with player piece
        tile_list[by][bx].draw(win)
        x2, y2 = bx, by # saves mouse coordinates to current player location
    return tile_list

# Switches current player after each turn
# Takes no parameters
# Returns nothing
def switch_player():
    global current_player, playertxt
    
    if current_player == 'red':
        current_player = 'blue'
    else:
        current_player = 'red'
    # updates current player text   
    playertxt.setText('Player: '+ current_player)
        
# Determines if a move is legal, players can move anywhere within one square 
# Takes mouse coordinates (bx, by)
# Returns False if a move is deemed illegal and True if it is legal
def legal_move(bx, by):
    global x1, y1, x2, y2, current_player, ice_location
    legal = False
    # tests if move is to broken ice
    for i in range(len(ice_location)):
        if (bx, by) in ice_location:
            return False
    # test if move is within one square of players current position
    if current_player == 'red':
        if bx == x2 and by == y2:
            return False
        elif bx == x1 + 1 and by == y1:
            return True
        elif  bx == x1 + 1 and by == y1 + 1:
            return True
        elif  bx == x1 + 1 and by == y1 - 1:
            return True
        elif  bx == x1 and by == y1 + 1:
            return True
        elif  bx == x1 - 1 and by == y1 + 1:
            return True
        elif  bx == x1 - 1 and by == y1:
            return True
        elif  bx == x1 - 1 and by == y1 - 1:
            return True
        elif  bx == x1 and by == y1 - 1:
            return True
        else:
            return False
    elif current_player == 'blue':
        if bx == x1 and by == y1:
            return False
        elif bx == x2 + 1 and by == y2:
            return True
        elif  bx == x2 + 1 and by == y2 + 1:
            return True
        elif  bx == x2 + 1 and by == y2 - 1:
            return True
        elif  bx == x2 and by == y2 + 1:
            return True
        elif  bx == x2 - 1 and by == y2 + 1:
            return True
        elif  bx == x2 - 1 and by == y2:
            return True
        elif  bx == x2 - 1 and by == y2 - 1:
            return True
        elif  bx == x2 and by == y2 - 1:
            return True      
        else:
            return False
            
# "Breaks Ice" where px, py specify
# Takes mouse click coordinates (px, py) and tile list
# Returns ice location set updated with most recent broken ice position
def break_ice(px, py, tile_list):
    global win, x1, y1, x2, y2, ice_location
    while True:
        for row in range(len(tile_list)):
            for col in range(len(tile_list[row])):
                if row == py and col == px:
                    if x1 == px == x2 and y1 == py == y2: # prevents breaking
                        px, py = get_click()              # ice on player
                        col = 0
                        row = 0 
                        continue
                    else:
                        i = Image(Point(px * TILE_W + 20,
                                        py * TILE_H + 20),"ice-blue.gif")
                        tile_list[row][col] = i
                        tile_list[row][col].draw(win)
                        ice_location.add((col,row))
                        return ice_location

# Detects whether or not one player has surrounded the other
# Takes no parameters
# Returns True if a player has won and False if there is no winner
def detect_win():
    global x1, y1, x2, y2, ice_location
    winposred = {(x1+1, y1), (x1+1, y1-1), (x1, y1-1), (x1-1, y1-1),
                 (x1-1, y1), (x1-1, y1+1), (x1, y1+1), (x1+1, y1+1)}
    
    winposblue = {(x2+1, y2), (x2+1, y2-1), (x2, y2-1), (x2-1, y2-1),
                  (x2-1, y2), (x2-1, y2+1), (x2, y2+1), (x2+1, y2+1)} 
    
    if winposred.issubset(ice_location):
        return True
    elif winposblue.issubset(ice_location):
        return True
    else:
        return False

# Displays the menu below the game board
# Takes no parameters
# Returns nothing
def menu():
    global win, playertxt
    # Creates Quit Button
    quit = Rectangle(Point(5,285),Point(75, 325))
    txtq = Text(Point(35, 305), 'Quit')
    quit.draw(win)
    txtq.draw(win)
    # Creates Restart Button
    restart = Rectangle(Point(325,285),Point(395, 325))
    txtr = Text(Point(360, 305), 'Restart')
    restart.draw(win)
    txtr.draw(win)
    # Draws current player text
    playertxt = Text(Point(400//2, 305), 'Player: '+ current_player)
    playertxt.draw(win)
    
# Restarts game from beginning   
# Takes no parameters
# Returns nothing
def restart():
    global x1, y1, x2, y2, tile_list, current_player
    for i in range(len(tile_list)):
        for x in range(len(tile_list[i])):
            tile_list[i][x].undraw()
    
    x1, y1 = 0, 3
    x2, y2 = 9, 3 
    tile_list = []
    ice_location.clear()
    draw_board()
    player()    
    current_player = 'red'
    playertxt.setText('Player: '+ current_player)

# Displays text specifying the winner
# Takes no parameters
# Returns nothing
def game_win():
    wintxt=Text(Point(WIN_H // 2, 390), current_player.title() + ' Player Wins!')
    wintxt.draw(win)
    
#-------------------------------------------------------------------------------
# Main Function
def main():
    global win, tile_list, legal
    global x1, y1, x2, y2, playertxt
    win = GraphWin('IceBreaker', WIN_W, WIN_H)
    splash_screen()
    draw_board()
    menu()
    player()
    ice_location = set()
    # main game loop
    while True:
        if detect_win() == True: # detects winner
            game_win()
        bx, by = get_click()
        if 0 <= bx <= 1 and 7 <= by <= 8: # quits game if quit is pressed
            break
        elif 8 <= bx <= 9 and 7 <= by <= 8: # restarts game if restart is pressed
            restart()
        if legal_move(bx, by) != True:
            continue
        # undraws piece before player is moved
        if current_player == 'red': 
            tile_list[y1][x1].undraw()
        else:
            tile_list[y2][x2].undraw()
        
        tile_list = move_player(bx, by)
        px, py = get_click()
        if 0 <= px <= 1 and 7 <= py <= 8: # quits game if quit is pressed
            break
        elif 8 <= px <= 9 and 7 <= py <= 8: # restarts game if restart is pressed
            restart()
            continue
        ice_location = break_ice(px, py, tile_list)
        
        switch_player()
    win.close()
    
#-------------------------------------------------------------------------------
# TEST CODE

if __name__ == '__main__':
    main()