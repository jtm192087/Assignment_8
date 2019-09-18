#!/usr/bin/python3
game = [0,0,0,0,0,0,0,0,0]
occpos = [0, 0, 0,0, 0, 0,0, 0, 0]

player = 'p2'                 # starting with player p2

def display_board ():
    print ('|' ,game[0],'|',game[1] ,'|', game[2],'|')
   
    print ('|' ,game[3],'|',game[4] ,'|', game[5],'|')
    
    print ('|' ,game[6],'|',game[7] ,'|', game[8],'|')

def switch_player (name):              #function to switch the player
    print ('player name:'+ name )
    x = int (input ('enter the number: '))
    y = int (input ('insterting to the position: '))
    if player == 'p1':
        even_no (x, y)
    else: 
        odd_no (x, y)      

def steps(y,z):
    game[z] = y
    occpos[z] =1
    display_board()

def odd_no (x, z):            #to make sure player enters the odd no.
    while  (x%2==0):
        x = int(input ('enter an odd number'))
    
    steps (x ,z)      

def even_no (x ,z) :         # to make sure player enters the even no.
    while  (x%2!=0):
        x = int(input ('enter an even number'))
   
    steps (x ,z)        

def winner():
    if (occpos[0] + occpos[1] + occpos[2] == 3):   
      if (game[0]+game [1]+game[2]==15):           #condition for horizontal win
           print ('{0} is the winner' .format(player))
           return True
    if (occpos[0] + occpos[3] + occpos[6] == 3):   # condition for vertical win
      if (game[0]+game [3]+game[6]==15):
           print ('{0} is the winner' .format(player))
           return True
    if (occpos[1] + occpos[4] + occpos[7] == 3):      # condition for diagonal win
      if (game[1]+game [4]+game[7]==15):
           print ('{0} is the winner' .format(player))
           return True
    if (occpos[3] + occpos[4] + occpos[5] == 3):
      if (game[3]+game [4]+game[5]==15):
          print ('{0} is the winner' .format(player))
          return True
    if (occpos[2] + occpos[5] + occpos[8] == 3):
      if (game[2]+game [5]+game[8]==15):
          print ('{0} is the winner' .format(player))
          return True
    if (occpos[6] + occpos[7] + occpos[8] == 3):
      if (game[6]+game [7]+game[8]==15):
           print ('{0} is the winner' .format(player))
           return True

    else: return False


     

print( 'welcome to game')
print('-------------------')
print('-------------------')
print ('The player with the odd numbers start')
print('-------------------')
print('-------------------')
display_board ()
while (True):
    switch_player (player)
    if winner(): break
    else:
        if player == 'p1': player = 'p2'  
        else: player = 'p1'