#Author: Alden DeMello
#File Name: DeMello_rps_rainbow.py
#Date: 4/23/2019
#Description: A simple game of rock paper scissors, with a twist!

from easygui import * #Import everything from easygui
import sys #Import sys
import random #Import random
#import PIL #Import PIL

flag_program = True #Boolean flag so the program runs infinitely
#RPS , rps = Rock Paper Scissors

while flag_program == True: #Infinite Loop, until the user quits

    def get_player_name(): #Get the player's name

        msg_name = 'Enter your Display Name' #Message to display to tell the user what to enter

        title = 'Rock Paper Scissors: Rainbow Edition' #Title of the widget

        user_name = enterbox(msg_name, title) #Call the enterbox function

        return user_name #Return user name

    def turns(): #Turns function

        turns = ['ONE', 'THREE', 'YOUR CHOICE'] #Game Choices #ADD RANDOM?
        welcome_msg = '                 CHOOSE THE NUMBER OF TURNS BELOW!          ' #Inform the user what to do
        title = 'Rock Paper Scissors: Rainbow Edition'
        turn_choice = buttonbox(welcome_msg, title, choices=turns) #Gane choice menu

        turn_choices = 0 #Set turns default to 0
        
        if turn_choice == 'ONE': #If condition is met 

            turn_choices = 1 #Set turns choice to 1

        elif turn_choice == 'THREE': #If condition is met 

            turn_choices = 3 #Set turns choice to 3 

        elif turn_choice == 'YOUR CHOICE': #If condition is met 

            turn_choices = user_choice_turns()  #Set turns choice to user's choice

        return turn_choices #Return game choice
        

    def rps_game(turns): #Game function

        flag_draw_1 = True

        flag_draw_2 = True

        flag_draw_3 = True

                #COMP #USER
        scores = [0, 0] #Local list to get scores

        comp_score = 0 #Computer score incrementor

        user_score = 0 #User score incrementor

        draw_score = 0 #Draw score incrementor

        for game_loop in range(turns): #Loop for the number of turns

            pc_choice = rand_comp_choice() #Call the random computer choice function

            usr_choice = usr_choice_screen() #


            

            if pc_choice == 1 and usr_choice == 1: #ROCK ROCK

                print('Draw') #Print ============================ FOR TESTING, REMOVE AFTER

                draw_score += 1 #Increment draw_score by 1

                #IMAGE OF DRAW 

                while flag_draw_1 == True:

                    pc_choice = rand_comp_choice() #Call the random computer choice function

                    usr_choice = usr_choice_screen() # Call the user choice screen

                    if pc_choice == 2 and usr_choice == 1: #PAPER ROCK

                        print('Winner: Computer') #Print ============================ FOR TESTING, REMOVE AFTER

                        comp_score += 1 #Increment comp_score by 1

                        flag_draw = False
          
                    elif pc_choice == 3 and usr_choice == 1: #SCISSOR ROCK

                        print('Winner: User') #Print ============================ FOR TESTING, REMOVE AFTER

                        user_score += 1 #Increment user_score by 1

                        flag_draw = False

                    else:

                        print('draw')




                

            elif pc_choice == 2 and usr_choice == 1: #PAPER ROCK

                print('Winner: Computer') #Print ============================ FOR TESTING, REMOVE AFTER

                comp_score += 1 #Increment comp_score by 1
  
            elif pc_choice == 3 and usr_choice == 1: #SCISSOR ROCK

                print('Winner: User') #Print ============================ FOR TESTING, REMOVE AFTER

                user_score += 1 #Increment user_score by 1



                

            elif pc_choice == 2 and usr_choice == 2: #PAPER PAPER

                print('Draw') #Print ============================ FOR TESTING, REMOVE AFTER

                draw_score += 1 #Increment draw_score by 1

                while flag_draw_2 == True:

                    pc_choice = rand_comp_choice() #Call the random computer choice function

                    usr_choice = usr_choice_screen() # Call the user choice screen
                    
                    if pc_choice == 2 and usr_choice == 3: #PAPER SCISSOR

                        print('Winner: User') #Print ============================ FOR TESTING, REMOVE AFTER

                        user_score += 1 #Increment user_score by 1

                        flag_draw_2 = False
                
                    elif pc_choice == 3 and usr_choice == 2: #SCISSOR PAPER

                        print('Winner: Computer') #Print ============================ FOR TESTING, REMOVE AFTER

                        comp_score += 1 #Increment comp_score by 1

                        flag_draw_2 = False

                    else:

                        print('draw')


                

            elif pc_choice == 2 and usr_choice == 3: #PAPER SCISSOR

                print('Winner: User') #Print ============================ FOR TESTING, REMOVE AFTER

                user_score += 1 #Increment user_score by 1
                
            elif pc_choice == 3 and usr_choice == 2: #SCISSOR PAPER

                print('Winner: Computer') #Print ============================ FOR TESTING, REMOVE AFTER

                comp_score += 1 #Increment comp_score by 1



                

            elif pc_choice == 3 and usr_choice == 3: #SCISSOR SCISSOR

                print('Draw') #Print ============================ FOR TESTING, REMOVE AFTER

                draw_score += 1 #Increment draw_score by 1

                while flag_draw_3 == True:
                    pc_choice = rand_comp_choice() #Call the random computer choice function

                    usr_choice = usr_choice_screen() # Call the usser choice screen

                    if pc_choice == 1 and usr_choice == 2: #ROCK PAPER

                        print('Winner: User') #Print ============================ FOR TESTING, REMOVE AFTER

                        user_score += 1 #Increment user_score by 1

                        flag_draw_3 = False

                    elif pc_choice == 1 and usr_choice == 3: #ROCK SCISSOR

                        print('Winner: Computer') #Print ============================ FOR TESTING, REMOVE AFTER

                        comp_score += 1 #Increment comp_score by 1

                        flag_draw_3 = False

                    else:

                        print('draw')
                        

            elif pc_choice == 1 and usr_choice == 2: #ROCK PAPER

                print('Winner: User') #Print ============================ FOR TESTING, REMOVE AFTER

                user_score += 1 #Increment user_score by 1

            elif pc_choice == 1 and usr_choice == 3: #ROCK SCISSOR

                print('Winner: Computer') #Print ============================ FOR TESTING, REMOVE AFTER

                comp_score += 1 #Increment comp_score by 1
                

        scores.insert(0, comp_score) #Insert the computer score into the score list
        
        scores.insert(1, user_score) #Insert the users score into the score list

        scores.insert(2, draw_score) #Insert the draw score into the score list

        comp_score = int(comp_score) #Cast comp_score to an int

        user_score = int(user_score) #Cast user_score to an int

        draw_score = int(draw_score) #Cast user_score to an int

        print(scores) #Print the Scores List ======================= FOR DEBUGGING, REMOVE AFTER
        
        return scores #Return Scores

    def welcome(): #Welcome function

        rainbow = 'rainbows_new.jpg' #Image        
        
        choices = ['HELP','PLAY','QUIT'] #Choices
       
        welcome_msg = '                 Welcome to RPS!           '#Welcome Message

        title = 'Rock Paper Scissors: Rainbow Edition'
       
        welcome_menu = buttonbox(welcome_msg, title, image=rainbow, choices=choices) #Welcome menu

        return welcome_menu #Return welcome menu
    
    def usr_choice_screen(): #User choice screen

        rainbow_img = r'C:\Users\alden\Desktop\Software Development\rps_rainbow.jpg'

        title = 'Rock Paper Scissors: Rainbow Edition'

        choices = ['SUNSHINE', 'STORM', 'RAIN', 'RANDOM'] #Game Choices #ADD RANDOM?
        
        welcome_msg = '                             CHOOSE a rainbow below!           ' #Inform the user what to do
        
        usr_choice = buttonbox(welcome_msg,title, image=rainbow_img, choices=choices) #Game choice menu

        user_choice = 0 #Set user choice to equal 0

        if usr_choice == 'SUNSHINE': #If condition is met 

            user_choice = 1
            
        elif usr_choice == 'STORM': #If condition is met

            user_choice = 2

        elif usr_choice == 'RAIN': #If condition is met

            user_choice = 3

        elif usr_choice == 'RANDOM': #If condition is met

            user_choice = usr_rand_choice() #Call the user random function
  
        return user_choice #Return game choice


    def rand_comp_choice(): #Random computer choice function

        rand_choice = random.randint(1,3) #Generate a random number from 1-3

        return rand_choice #Return rand choice

    def usr_rand_choice(): #Random user choice function

        usr_rand_choice = random.randint(1,3) #Generate a random number from 1-3

        return usr_rand_choice #Return the user's random choice

    def user_choice_turns(): #User choice turns function

        flag_odd = True

        msg_turns = 'Choose your own number of turns, ONLY ODD NUMBERS(ex. 1,3,5,7,9 etc)! \nEnter ONLY the number value below!' #Turns message

        title = 'Rock Paper Scissors: Rainbow Edition' #Title of the widget

        user_turns = enterbox(msg_turns, title) #Call the enter box function

        if user_turns == '' or user_turns == ' ': #If condition is met

            user_turns = 1 #Set the default value to 1

        user_turns = int(user_turns) #Cast the turns into an integer

        if user_turns % 2 == 0:

            while flag_odd == True:

                user_turns = enterbox(msg_turns, title) #Call the enter box function

                user_turns = int(user_turns) #Cast the turns into an integer

                if user_turns % 2 == 0:

                     user_turns = enterbox(msg_turns, title) #Call the enter box function

                elif user_turns % 2 == 1:

                    flag_odd = False

        return user_turns #Return user turns
        

    def check_choice(reply): #Check Choice function

        if reply == 'PLAY': #If condition is met

            user_name = get_player_name() #Call the get player name function

            user_turns = turns() #Call turns function

            play_game = rps_game(user_turns) #Call the rps game function

            scoreboard(play_game, user_name) #Call the scoreboard function

        elif reply == 'HELP': #If condition is met

            help_menu() #Call Help Menu

        #elif reply == 'STATS': #If condition is met
            
            #stats() #Call the stats function

        elif reply == 'QUIT': #If condition is met

            msg_quit = 'Are you sure you want to quit?' #Message to inform the user what is happening
            
            quit_box = ynbox(msg_quit, 'Rock Paper Scissors: Rainbow Edition') #Call the y/n box function

            if quit_box: #If condition is met

                sys.exit(0) # Exit the program
    
    def scoreboard(score, user_name): #Scireboard function 

        comp_score =  str(score[0]) #Set comp score to be the 0 index of score and cast it to a string

        usr_score = str(score[1]) #Set user score to be the 1 index of score and cast it to a string

        draws = str(score[2]) #Set draw score to be the 2 index of score and cast it to a string

        if user_name == '' or user_name == ' ': #If condition is met

            user_name = 'Player' #Set the user name to Player

        scoreboard_str = '                          Thanks for playing!\n \n Computer Score: ' + comp_score + '\n \n ' + user_name + "'s Score" + ': ' + usr_score + '\n \n Draws: ' + draws #Scoreboard string

        title = 'Rock Paper Scissors: Rainbow Edition' #Title of widget
        
        menu = msgbox(scoreboard_str, title) #Help Menu
    

    def help_menu(): #Help Menu Function

        image = r'C:\Users\alden\Desktop\Software Development\help_menu.jpg' #Image

        help_m = 'HELP MENU' #Help Menu

        help_string = ' '

        title = 'Rock Paper Scissors: Rainbow Edition' #Title of widget
        
        menu = msgbox(help_string, title, image=image) #Help Menu
      
    wel_reply = welcome() #Call the welcome function
    
    choice_check = check_choice(wel_reply) #Call the check choice function


########################
        #NOTES

    # CHECK IF A NUMBER IS ENTERED 
    
#Settings Page?

########################


