import math



from computer_functions import get_computer_move,HEAPS

lst = list(HEAPS)


def show_board(board):
    '''
    this is a func that prints the board, it takes the places from 0 until
    it finishes, i want it to print the places, but starting
    from 1, so i add +1 , and to print * as the number in the list.    
    '''    
    for i in range(len(board)):
        print(str(i+1)+':')
        if (lst[i]== 0):
            print ( )
        else:
            print((lst[i]-1)* '* '+'*')




def check_row(given_row):
    '''
    this func calculates the row with the given input. the player put the row
    and this func checks if the number row input is in the right limitations.
    '''
    while(given_row > len(lst) or given_row <= 0 or lst[given_row-1] == 0  ):
        if(given_row > len(lst) or given_row <= 0):
            given_row= int(input("Row?"))
        elif(lst[given_row-1] == 0):
            print("That row is empty")
            given_row= int(input("Row?"))
            continue
    return given_row
            

def amount_stars(row, how_many): 
    '''
    this func checks if the amount input is in the right limitaion, if its not
    keep asking for the amount, if it is then, reduce the right amount from 
    the right row, then return the amount
    '''  
    while(lst[row] < how_many or how_many < 0 or how_many == 0):
        how_many= int(input("How many?"))
        if(how_many < lst[row] and how_many > 0):
            break
    lst[row] = lst[row] - how_many #now this is the new list!         
    return how_many
    

def check_empty_board():
    '''
    this func checks if the board is empty, if its not then continue the game,
    if its true then the game finishes and it stops.
    '''  
    for i in lst:
        if(i != 0):
            is_board_empty = False
            break
        else:
            is_board_empty = True  
    return is_board_empty



def play_one_game(the_one_to_start):
    '''
    this func manage all the game.  
    '''
    empty= False
    while(empty == False):
        show_board(lst)
        #with the argument in the func, we choose who starts:
        if(the_one_to_start == 'You win' or the_one_to_start == name):
            print(name +", it's your turn:")
            row= int(input("Row?"))            
            row = check_row(row) #send us to the func
            row = row - 1  
            amount= int(input("How many?"))        
            amount = amount_stars(row, amount) #send us to the func

            #first player finished his turn now it goes or to the computer or
            #to the second player.
            if(number_of_players == 1):  
                the_one_to_start = 'Computer' 
            else:
                the_one_to_start = second_player_name 
            empty = check_empty_board()

            #after it checks if the board is empty,
            # if it is check who is the winner:
            if (number_of_players == '1'):   
                winner = 'You'
            else:
                winner = name
            if(empty):
                break

            
        #call computer and make him start playing
        elif(the_one_to_start == 'Computer' or number_of_players == '1'):
           
            comp_turn= get_computer_move(lst)

            value_row= comp_turn[0]
            value_stars= comp_turn[1]
       
            print("Computer takes", value_stars, "from row", value_row +1 )

            lst[value_row] = lst[value_row] - value_stars
            the_one_to_start = name  #after he finishes go to the first player                      
            empty= check_empty_board()
            #checks if the board is empty, if it is the winner is computer
            winner= 'Computer'
            

        #2 players play, and its the turn of player 2        
        elif(the_one_to_start == second_player_name):
            print(second_player_name +", it's your turn:")
            row= int(input("Row?"))
            row = check_row(row)
            row = row - 1  
            amount= int(input("How many?"))
            amount = amount_stars(row, amount)
            the_one_to_start = name  #after he finishes go to the first player          
            empty= check_empty_board()
            #checks if the board is empty, if it is the winner is 2nd player
            winner= second_player_name 
        
        empty= check_empty_board()
    show_board(lst) #the board is empty, show it

    #print the winners:
    if(winner == 'You'):
        print("You win")
    else:
        print(winner, "wins")
    return winner   


#set the players
number_of_players= input("Please enter the number of human players (1 or 2):")
name= ''
second_player_name= '' 
one_player = 1
two_players= 2

if (number_of_players == '1'):
    name= input("Please enter your name:")

    
elif (number_of_players == '2'):
    name= input("Name of first player:")
    second_player_name= input("Name of second player:")


#define my variables

answer= 'Y'
play_again=''



the_winner= play_one_game(name) #now the game begin, starting the first player

more_game = True #to get to the while loop

while(more_game == True):  #for more games  
    lst = list(HEAPS)             
    play_again= str(input("Play again? (Y/N)"))

    if(play_again == answer or play_again == answer.lower()):
        more_game = True 
        #now the func starts from the winning player                      
        the_winner= play_one_game(the_winner)          
        
    else: #end the game
        more_game = False
    
  
        
    

   









