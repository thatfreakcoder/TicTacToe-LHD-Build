import sys, random, time

#--- GLOBAL VARIABLES ---
board = ['_' , '_' , '_',
         '_' , '_' , '_',
         '_' , '_' , '_']
remove = 1
pos = [1,2,3,4,5,6,7,8,9]
game_continue = True
i = 1
def Display_Board():
  time.sleep(0.5)
  print(' | ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ' + '      | 1 | 2 | 3 |')
  
  print(' | ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ' + '      | 4 | 5 | 6 |')
  
  print(' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ' + '      | 7 | 8 | 9 |')
  time.sleep(1)

Display_Board()


def Play():
  global i
  global game_continue
 # Player2()
  Player1()
  Player2()
  Player1()
  check_for_tie()
  Win()
  i = 1
  while game_continue:
   while i <= 3:
    Win()
    if game_continue == True:
     Player2Smart()
     check_for_tie()
     Win()
     if game_continue == False:
      sys.exit()
     else:
      Player1()
      check_for_tie()
      Win()
    if game_continue == False:
     sys.exit()
    

def Win():
    global game_continue
    
    #-------ROW WINNER CHECK-------
    if board[0] == board[1] == board[2] != '_':
      game_continue = False
      if board[0] == 'X':
        print("Player 1 Wins")
      else:
        print("Player 2 Wins")
    if board[3] == board[4] == board[5] != '_':
      game_continue = False
      if board[3] == 'X':
        print("Player 1 Wins")
      else:
        print("Player 2 Wins")
    if board[6] == board[7] == board[8] != '_':
      game_continue = False
      if board[6] == 'X':
        print("Player 1 Wins")
      else:
        print("Player 2 Wins")
    
    #--------COLUMN WINNER CHECK--------
    if board[0] == board[3] == board[6] != '_':
      game_continue = False
      if board[0] == 'X':
        print("Player 1 Wins")
      else:
        print("Player 2 Wins")
    if board[1] == board[4] == board[7] != '_':
      game_continue = False
      if board[1] == 'X':
        print("Player 1 Wins")
      else:
        print("Player 2 Wins")
    if board[2] == board[5] == board[8] != '_':
      game_continue = False
      if board[2] == 'X':
        print("Player 1 Wins")
      else:
        print("Player 2 Wins")
    
    #----------DIAGONALS WINNER CHECK---------
    if board[0] == board[4] == board[8] != '_':
      game_continue = False
      if board[0] == 'X':
        print("Player 1 Wins")
      else:
        print("Player 2 Wins")
    if board[2] == board[4] == board[6] != '_':
      game_continue = False
      if board[2] == 'X':
        print("Player 1 Wins")
      else:
        print("Player 2 Wins")


def Player1():
    global remove
    n = int(input("Enter Your Position : " ))
    board[n-1] = 'X'
    Display_Board()
    remove = n
    
def Player2():
   global remove
   k = random.randint(1,6)
   if k == 1 and board[4] == "_mlm":
    board[4] = 'O'
    print("AI has chosen : 5")
    Display_Board()
    
   elif k == 2 and board[8] == '_':
    board[8] = 'O'
    print("AI has chosen : 9")
    Display_Board()
   
   elif k == 3 and board[2] == '_':
    board[2] = 'O'
    print("AI has chosen : 3")
    Display_Board()

   elif k == 4 and board[6] == "_":
    board[6] = 'O'
    print("AI has chosen : 7")
    Display_Board()

   elif  k == 5 and board[0] == '_':
    board[0] = 'O'
    print("AI has chosen : 1")
    Display_Board()

   else:
    pos.remove(remove)
    m = random.choice(pos)
    pos.remove(m)
    board[m - 1] = 'O'
    print("AI has chosen : " + str(m))
    Display_Board()
    
def Player2Smart():
    # ----------------O WINNING-------------
      
   #verticle line check 1
  if board[0] == board[1] == 'O' and board[2] == '_':# and Count == 1:
    board[2] = 'O'
    print("AI has chosen : 3")
    Display_Board()
#    Count = Count - 1
  elif board[0] == board[2] == 'O' and board[1] == '_' :#and Count == 1:
    board[1] = 'O'
    print("AI has chosen : 2")
    Display_Board()
#    Count = Count - 1
  elif board[1] == board[2] == 'O' and board[0] == '_':# and Count == 1:
    board[0] = 'O'
    print("AI has chosen : 1")
    Display_Board()
#    Count = Count - 1
  
  #verticle line check 2
  elif board[3] == board[4] == 'O' and board[5] == '_' :#and Count == 1:
    board[5] = 'O'
    print("AI has chosen : 6")
    Display_Board()
 #   Count = Count - 1
  elif board[3] == board[5] == 'O' and board[4] == '_':# and Count == 1:
    board[4] = 'O'
    print("AI has chosen : 5")
    Display_Board()
#    Count = Count - 1
  elif board[4] == board[5] == 'O' and board[3] == '_' :#and Count == 1:
    board[3] = 'O'
    print("AI has chosen : 4")
    Display_Board()
#    Count = Count - 1
 
  #verticle line check 3
  elif board[6] == board[7] == 'O' and board[8] == '_' :#and Count == 1:
    board[8] = 'O'
    print("AI has chosen : 9")
    Display_Board()
 #   Count = Count - 1
  elif board[6] == board[8] == 'O' and board[7] == '_':# and Count == 1:
    board[7] = 'O'
    print("AI has chosen : 8")
    Display_Board()
#    Count = Count - 1
  elif board[7] == board[8] == 'O' and board[6] == '_':# and Count == 1:
    board[6] = 'O'
    print("AI has chosen : 7")
    Display_Board()
 #   Count = Count - 1
    
  #horizontal line check 1
  elif board[0] == board[3] == 'O' and board[6] == '_':# and Count == 1:
    board[6] = 'O'
    print("AI has chosen : 7")
    Display_Board()
#    Count = Count - 1
  elif board[0] == board[6] == 'O' and board[3] == '_' :#and Count == 1:
    board[3] = 'O'
    print("AI has chosen : 4")
    Display_Board()
#    Count = Count - 1
  elif board[3] == board[6] == 'O' and board[0] == '_':# and Count == 1:
    board[0] = 'O'
    print("AI has chosen : 1")
    Display_Board()
 #   Count = Count - 1
 
  #horiontal line check 2
  elif board[1] == board[4] == 'O' and board[7] == '_':# and Count == 1:
    board[7] = 'O'
    print("AI has chosen : 8")
    Display_Board()
 #   Count = Count - 1
  elif board[1] == board[7] == 'O' and board[4] == '_':# and Count == 1:
    board[4] = 'O'
    print("AI has chosen : 5")
    Display_Board()
 #   Count = Count - 1
  elif board[4] == board[7] == 'O' and board[1] == '_' :#and Count == 1:
    board[1] = 'O'
    print("AI has chosen : 2")
    Display_Board()
#    Count = Count - 1
 
  #horizontal line check 3
  elif board[2] == board[5] == 'O' and board[8] == '_':# and Count == 1:
    board[8] = 'O'
    print("AI has chosen : 9")
    Display_Board()
   # Count = Count - 1
  elif board[2] == board[8] == 'O' and board[5] == '_' :#and Count == 1:
    board[5] = 'O'
    print("AI has chosen : 6")
    Display_Board()
   # Count = Count - 1
  elif board[5] == board[8] == 'O' and board[2] == '_' :#and Count == 1:
    board[2] = 'O'
    print("AI has chosen : 3")
    Display_Board()   
    #Count = Count - 1
  
  #diagonal line check 1
  elif board[0] == board[4] == 'O' and board[8] == '_':# and Count == 1:
    board[8] = 'O'
    print("AI has chosen : 9")
    Display_Board()
   # Count = Count - 1
  elif board[0] == board[8] == 'O' and board[4] == '_' :#and Count == 1:
    board[4] = 'O'
    print("AI has chosen : 5")
    Display_Board()
   # Count = Count - 1
  elif board[4] == board[8] == 'O' and board[0] == '_' :#and Count == 1:
    board[0] = 'O'
    print("AI has chosen : 3")
    Display_Board()   
  #diagonal line check 2
  elif board[2] == board[6] == 'O' and board[4] == '_':# and Count == 1:
    board[4] = 'O'
    print("AI has chosen : 5")
    Display_Board()
   # Count = Count - 1
  elif board[2] == board[4] == 'O' and board[6] == '_' :#and Count == 1:
    board[6] = 'O'
    print("AI has chosen : 7")
    Display_Board()
   # Count = Count - 1
  elif board[4] == board[6] == 'O' and board[2] == '_' :#and Count == 1:
    board[2] = 'O'
    print("AI has chosen : 3")
    Display_Board()   
  
  #verticle line check 1
  elif board[0] == board[1] == 'X' and board[2] == '_':# and Count == 1:
    board[2] = 'O'
    print("AI has chosen : 3")
    Display_Board()
 #   Count = Count - 1
  elif board[0] == board[2] == 'X' and board[1] == '_':# and Count == 1:
    board[1] = 'O'
    print("AI has chosen : 2")
    Display_Board()
   # Count = Count - 1
  elif board[1] == board[2] == 'X' and board[0] == '_':# and Count == 1:
    board[0] = 'O'
    print("AI has chosen : 1")
    Display_Board()
  #  Count = Count - 1
  
  #verticle line check 2
  elif board[3] == board[4] == 'X' and board[5] == '_':# and Count == 1:
    board[5] = 'O'
    print("AI has chosen : 6")
    Display_Board()
#    Count = Count - 1
  elif board[3] == board[5] == 'X' and board[4] == '_':# and Count == 1:
    board[4] = 'O'
    print("AI has chosen : 5")
    Display_Board()
 #   Count = Count - 1
  elif board[4] == board[5] == 'X' and board[3] == '_':# and Count == 1:
    board[3] = 'O'
    print("AI has chosen : 4")
    Display_Board()
#    Count = Count - 1
 
  #verticle line check 3
  elif board[6] == board[7] == 'X' and board[8] == '_':# and Count == 1:
    board[8] = 'O'
    print("AI has chosen : 9")
    Display_Board()
 #   Count = Count - 1
  elif board[6] == board[8] == 'X' and board[7] == '_':# and Count == 1:
    board[7] = 'O'
    print("AI has chosen : 8")
    Display_Board()
#    Count = Count - 1
  elif board[7] == board[8] == 'X' and board[6] == '_':#and Count == 1:
    board[6] = 'O'
    print("AI has chosen : 7")
    Display_Board()
 #   Count = Count - 1
    
  #horizontal line check 1
  elif board[0] == board[3] == 'X' and board[6] == '_':# and Count == 1:
    board[6] = 'O'
    print("AI has chosen : 7")
    Display_Board()
 #   Count = Count - 1
  elif board[0] == board[6] == 'X' and board[3] == '_':# and Count == 1:
    board[3] = 'O'
    print("AI has chosen : 4")
    Display_Board()
  #  Count = Count - 1
  elif board[3] == board[6] == 'X' and board[0] == '_':# and Count == 1:
    board[0] = 'O'
    print("AI has chosen : 1")
    Display_Board()
 #   Count = Count - 1
 
  #horiontal line check 2
  elif board[1] == board[4] == 'X' and board[7] == '_':# and Count == 1:
    board[7] = 'O'
    print("AI has chosen : 8")
    Display_Board()
#    Count = Count - 1
  elif board[1] == board[7] == 'X' and board[4] == '_':# and Count == 1:
    board[4] = 'O'
    print("AI has chosen : 5")
    Display_Board()
  #  Count = Count - 1
  elif board[4] == board[7] == 'X' and board[1] == '_':# and Count == 1:
    board[1] = 'O'
    print("AI has chosen : 2")
    Display_Board()
#    Count = Count - 1
 
  #horizontal line check 3
  elif board[2] == board[5] == 'X' and board[8] == '_':# and Count == 1:
    board[8] = 'O'
    print("AI has chosen : 9")
    Display_Board()
 #   Count = Count - 1
  elif board[2] == board[8] == 'X' and board[5] == '_':# and Count == 1:
    board[5] = 'O'
    print("AI has chosen : 6")
    Display_Board()
#    Count = Count - 1
  elif board[5] == board[8] == 'X' and board[2] == '_':#and Count == 1:
    board[2] = 'O'
    print("AI has chosen : 3")
    Display_Board()
 #   Count = Count - 1
    
  #diagonal line check 1
  elif board[0] == board[8] == 'X' and board[4] == '_':# and Count == 1:
    board[4] = 'O'
    print("AI has chosen : 5")
    Display_Board()
#    Count = Count - 1
  elif board[0] == board[4] == 'X' and board[8] == '_':# and Count == 1:
    board[8] = 'O'
    print("AI has chosen : 9")
    Display_Board()
 #   Count = Count - 1
  elif board[4] == board[8] == 'X' and board[0] == '_':# and Count == 1:
    board[0] = 'O'
    print("AI has chosen : 1")
    Display_Board()
 #   Count = Count - 1
 
  #diagonal line check 2
  elif board[2] == board[4] == 'X' and board[6] == '_':# and Count == 1:
    board[6] = 'O'
    print("AI has chosen : 7")
    Display_Board()
 #   Count = Count - 1
  elif board[2] == board[6] == 'X' and board[4] == '_':# and Count == 1:
    board[4] = 'O'
    print("AI has chosen : 5")
    Display_Board()
 #   Count = Count - 1
  elif board[4] == board[6] == 'X' and board[2] == '_':# and Count == 1:
    board[2] = 'O'
    print("AI has chosen : 3")
    Display_Board()
 #   Count = Count - 1   
  else:
    Player2()
  

def check_for_tie():
    # Set global variables
    global game_continue
    # If board is full
    if  "_" not in board:
        game_continue = False
        print("🎉  ITS A TIE   🎉")
        return True
    else:
        return False
  
Play()