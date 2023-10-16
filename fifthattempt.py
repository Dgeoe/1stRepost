import random
import time
import csv

#introduction to game
print("Welcome to SPEED: a card game")

# Hypothesis 1- smth abt starting deck
# Hypothesis 2- smth abt time
# Hypothesis 3- smth about starting or seconding user

#ask for if player requires rules
r=0
while r == 0:
    rules = input("Do you want to learn the rules?:").lower()
    e=("===========================================================")
    f=("-----------------------------------------------------------")
    if rules == 'yes' or rules =='y':

        print(e)
        print("HOW TO PLAY")
        print(e)
        print("1. Speed is card game with three modes: pvp (multiplayer), pve (vs computer) and simulation.\n2. Both players are provided a hand consisting of _ cards.")
        print("3. The objective of the game is to be the first player to get rid of all your cards.")
        print("4. On each turn, you must play a card that is one higher or one lower than a card in the middle pile.")
        print("5. Cards are represented by their number values with Ace=1, Jack=11, Queen=12 and King=13.")
        print("6. If you cannot play a card you can type 0 to randomly shuffle half the middle pile but also skip your turn.")
        print("  *Time is displayed at end*")
        print(e)
        print("GAME START")
        print(e)
        r= r+1
        
    elif rules== 'no' or rules== 'n':
        print("Goodluck")
        print(e)
        print("GAME START")
        print(e)
        r= r+1

    else:
        print(e)
        print("invalid input, try again")
        print("enter yes/no")
        print(e)
        continue
#define card values
deck= [1,2,3,4,5,6,7,8,9,10,11,12]
fix = [15,16]

#lists representing the cards in each players or computers hand
user = []
luser=[]
computer = []
computer2 = []

#list representing middle pile
middle = []
 
#deal cards
def dealcards():
    global user, computer, middle
    random.shuffle(deck)
    user= deck[:5]
    computer= deck[5:10]
    middle= deck[10:13]

def dealcardsMULTI():
    global user, luser, middle
    random.shuffle(deck)
    user= deck[:5]
    luser= deck[5:10]
    middle= deck[10:13]
    
def dealcardsSIM():
    global computer, computer2, middle
    random.shuffle(deck)
    computer= deck[:5]
    computer2= deck[5:10]
    middle= deck[10:13]
    
#write data to csv

#check if variables are exactly one higher or one lower than another variable   
def detect_adjacent(a,b):
    if abs(a-b) ==  1 or abs(a-b) == -1:
        return True
    else:
        return False
#allows for continued paly and testing
sync = 0
while sync == 0:
    #timer
    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins= mins % 60
        print("*Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
    Select=input("SELECT YOUR MODE:")
    if Select == "pve" or Select== "PvE" or Select== "PVE":
        def play():
            global user, computer, middle
            dealcards()
            while (len(user)>0) and (len(computer)>0):
                print("Middle pile:", middle)
                print("Your hand:", user)
                print("--------------------------")
            #timer start
                start_time = time.time()
            
            #user input
                uinput= int(input("Which card would you like to play?:"))
                #       ^value error occurs if non int value entered^
            
            #check input meets requirements ,then append or ask to repeat
                if uinput in user and detect_adjacent(middle[0],uinput):
                    middle.append(uinput)
                    user.remove(uinput)
                    middle.remove(middle[0])
            
                elif uinput in user and detect_adjacent(middle[1],uinput):
                    middle.append(uinput)
                    user.remove(uinput)
                    middle.remove(middle[1])
            
            #skip operation as detailed in rules above
                elif uinput == 0:
                    random.shuffle(deck)
                    random.shuffle(fix)
                    if fix[0] == 15:
                        middle[0] = deck[10]
                    else:
                        middle[1] = deck[10]
               
                else:
                    print("invalid move, try again")
                    print("--------------------------")
                    continue
        
                cinput = random.choice(computer)
                if detect_adjacent(middle[0],cinput):
                    print("Computer plays", cinput)
                    middle.append(cinput)
                    computer.remove(cinput)
                    middle.remove(middle[0])
               
                elif detect_adjacent(middle[1],cinput):
                    print("Computer plays", cinput)
                    middle.append(cinput)
                    computer.remove(cinput)
                    middle.remove(middle[1])
               
                else:
                    print("Computer skips")
                    random.shuffle(deck)
                    random.shuffle(fix)
                    if fix[0] == 15:
                        middle[0] = deck[10]
                    else:
                        middle[1] = deck[10]
                
        #winstate
            if len(user) == 0:
                print(e)
                print("Player wins!")
                print(e)
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_convert(time_lapsed)
                print(f)
            elif len(computer) ==0:
                print(e)
                print("You lose.")
                print(e)
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_convert(time_lapsed)
                print(f)
            elif len(user) == 0 and len(computer) ==0:
                print(e)
                print ("Draw")
                print(e)
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_convert(time_lapsed)
                print(f)

        play()

    elif Select == "pvp" or Select == "PvP" or Select == "PVP":
        def pvplay():
            global user, luser, middle
            dealcardsMULTI()
            while (len(user)>0) and (len(luser)>0):
                print("--------------------------")
                print("Middle pile:", middle)
                print("Player 1 hand:", user)
                print("Player 2 hand:", luser)
                print("--------------------------")
                
                #timer start
                start_time = time.time()

                uinput= int(input("Which card would you like to play?:"))
                u2input=int(input("Which card would you like to play?:"))
     
        #check input meets requirements ,then append or ask to repeat
                
                if uinput in user and detect_adjacent(middle[0],uinput):
                    middle.append(uinput)
                    user.remove(uinput)
                    middle.remove(middle[0])

                elif uinput in user and detect_adjacent(middle[1],uinput):
                    middle.append(uinput)
                    user.remove(uinput)
                    middle.remove(middle[1])
            
        #skip operation as detailed in rules above

                elif uinput == 0:
                    random.shuffle(deck)
                    random.shuffle(fix)
                    if fix[0] == 15:
                        middle[0] = deck[10]
                    else:
                        middle[1] = deck[10]

                else:
                    print("invalid move, try again")
                    print("--------------------------")
                    continue
        
                if u2input in luser and detect_adjacent(middle[0],u2input):
                    middle.append(u2input)
                    luser.remove(u2input)
                    middle.remove(middle[0])

                elif u2input in luser and detect_adjacent(middle[1],u2input):
                    middle.append(u2input)
                    luser.remove(u2input)
                    middle.remove(middle[1])

                elif u2input == 0:
                    random.shuffle(deck)
                    random.shuffle(fix)
                    if fix[0] == 15:
                        middle[0] = deck[10]
                    else:
                        middle[1] = deck[10]

                else:
                    print("invalid move, try again")
                    print("--------------------------")
                    continue
                
        #winstate
            if len(user) == 0:
                print(e)
                print("Player 1 wins!")
                print(e)
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_convert(time_lapsed)
                print(f)
            elif len(luser) ==0:
                print(e)
                print("Player 2 wins")
                print(e)
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_convert(time_lapsed)
                print(f)
            elif len(user) == 0 and len(luser) ==0:
                print(e)
                print ("Draw")
                print(e)
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_convert(time_lapsed)
                print(f)

        pvplay()

    elif Select == "sim" or Select == "simulation" or Select == "SIM":
        def simplay():
            global computer, computer2, middle
            wone = 0
            wtwo = 0
            dealcardsSIM()
            print("Middle pile:",middle)
            print(e)
            print("1st computer's hand:\n",computer)
            print(f)
            print("2nd computer's hand:\n",computer2)
            print(f)
            time.sleep(1)
            
            start_time = time.time()
        
            while (len(computer)>0) and (len(computer2)>0):
                cinput = random.choice(computer)
                if detect_adjacent(middle[0],cinput):
                    print("Computer 1 plays", cinput)
                    print(f)
                    middle.append(cinput)
                    computer.remove(cinput)
                    middle.remove(middle[0])
                
                elif detect_adjacent(middle[1],cinput):
                    print("Computer 1 plays", cinput)
                    print(f)
                    middle.append(cinput)
                    computer.remove(cinput)
                    middle.remove(middle[1])
            
                else:
                    print("Computer 1 skips")
                    wone = wone + 1
                    print(f)
                    random.shuffle(deck)
                    random.shuffle(fix)
                    if fix[0] == 15:
                        middle[0] = deck[10]
                    else:
                        middle[1] = deck[10]
                
                c2input = random.choice(computer2)
                if detect_adjacent(middle[0],c2input):
                    print("Computer 2 plays", c2input)
                    print(f)
                    middle.append(c2input)
                    computer2.remove(c2input)
                    middle.remove(middle[0])
            
                elif detect_adjacent(middle[1],c2input):
                    print("Computer 2 plays", c2input)
                    print(f)
                    middle.append(cinput)
                    computer2.remove(c2input)
                    middle.remove(middle[1])

                else:
                    print("Computer 2 skips")
                    wtwo = wtwo +1
                    print(f)
                    random.shuffle(deck)
                    random.shuffle(fix)
                    if fix[0] == 15:
                        middle[0] = deck[10]
                    else:
                        middle[1] = deck[10]
                
        #winstate
            if len(computer) == 0:
                print(e)
                print("Computer 1 win!")
                print(e)
                print("wone:",wone," wtwo:",wtwo)
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_convert(time_lapsed)
                #
                print(f)
            elif len(computer2) ==0:
                print(e)
                print("Computer 2 victory!")
                print(e)
                print("wone:",wone," wtwo:",wtwo)
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_convert(time_lapsed)
                print(f)
            elif len(computer) == 0 and len(computer2) ==0:
                print(e)
                print("Draw")
                print(e)
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_convert(time_lapsed)
                print(f)
            
        simplay()

    else:
        print("Invalid Input")
        print(f)
        print("Select PVP or PVE or SIM")
        print(e)
        continue