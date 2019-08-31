################################################################
# Extended version of the Combact game {Assignment1 of FIT9133}#
################################################################

################################################################
# Student name:         Sohail.Sankanur                        #
# Monash Student ID:    29996368                               #
# Start Date:           19 Aug 2018                            #
# Last Modified Date:   23 Aug 2018                            #
################################################################


## Explaination of solution which has been implemented:
# >> There are 2 players who are called Commander 1 and Commander 2 in this game
# >> They have to make an army and the members of the army has to be selected by them.
# >> Based on the selection of the army members the fight happens. The army members are called units
# >> The units fight in an order in which they have been selected by the commanders
# >> The units which win stay on the battlefield and the loosing unit dies
# >> The Commander who looses all the units in the battle the fastest is the losing commander
# >> There are some units which are more powerful than normal units which can be purchased for a higher price
# >> At the end the money which is left over is used for purchase of medics. Cost of medics is 1$ per unit. Medic can heal an army unit completely only once.
# >> Hence when an army unit dies in the battle the unit would get healed and it would be added in the queue of army at the end


## Explaination of the code structure:
# >> In the code we have a function "input_player" takes input from the players
# >> After the Player chooses the army members there is a check to see weather proper inputs were supplied and also weather the money was
#    sufficient to buy the specified units for the army
# >> In the initial part of the code there is inputPlayer function is called from the main code and this takes input of the 2 Commander armies
# >> The units of the armies are stored in a list
# >> The comparision of the list is done and based on the rules which is given in the problem statement the comparision is done and the loosong
#    army is popped off the list
# >> Medics are looked at in the medicsBuy function and the army say for n medics n army units would be healed and added to the list at the end
# >> Hence the funciton works in such a way that for n medics bought in the game it would look at the initial n elements of the army list and add
#    it by replicating it toward the end of the list
# >> The list which gets empty the fastest is the loosing Player or Commander
# >> In the last part of the code there are comparision statement and based on the comparisions the winning Commander is decided and printed out
import time

player_units = [[],[]] # Units which commanders select to form army
total_money = [10,10]  # This is the total money which is given to a commander
medics_money=[0,0]  # this is the money to buy medics


# inputPlayer is the function which would take inputs from each player



# medicsBuy is the function which would buy medics in the game with the leftover money after buying units

def medicsBuy(player_Number):
    if total_money[player_Number] < 10:
        medics_money[player_Number] = total_money[player_Number]
        for i in range(0, medics_money[player_Number]):
            player_units[player_Number].append(player_units[player_Number][i])

def input_player(player_number):
    while total_money[player_number] > 0:
        print("Please enter the unit which you would like to add to the army. Select from the following options\n")
        print("1. Archer    Type 'a' to select this")
        print("2. Soldier   Type 's' to select this")
        print("3. Knights   Type 'k' to select this")
        print("\n\nThere are some Units with special powers which can be bought for a higher price. The special units are:\n")
        print("4. Siege Equipment   Type 'se' to select this unit, This is sold at 2$ per unit")
        print("5. Wizard            Type 'w' to select this unit,  This is sold at 3$ per unit")
        print("4. Exit              Type 'e' to select this\n")
        player_input = input("Please make your choice(a/s/k/se/w/e):         ")
        player_input = player_input.upper()
        if player_input == "A" or player_input == "S" or player_input == "K":
            if player_input == "A":
                print("\nAn Archer unit has been added into the army\n\n")
            elif player_input == "S":
                print("\nA Soldier unit has been added into the army\n\n")
            else:
                print("\nA Knights unit has been added into the army\n\n")
            total_money[player_number] -=1
            player_units[player_number].append(player_input)
        elif player_input == "SE":
            if total_money[player_number] >= 2:
                total_money[player_number]-=2
                player_units[player_number].append(player_input)
                print("\nA Siege Equipment unit has been added into the army\n\n")
            else:
                print("\n\nYou do not have the money to buy a Siege Equipment Unit\n\n\n")
                continue
        elif player_input == "W":
            if total_money[player_number] >= 3:
                total_money[player_number]-=3
                player_units[player_number].append(player_input)
                print("\nA Wizard unit has been added into the army\n\n")
            else:
                print("\n\nYou do not have the money to buy a Wizard Unit\n\n\n")
                continue
        elif player_input == "E":
            final_exit_promt = input(f"You have {total_money[player_number]}$ money left. "+"Are you sure you want to exit the selection of units {y or n}\t")


            if final_exit_promt == 'y':
                print("Thanks for selecting army units")
                break
            else:
                continue
        else:
            print("\n\n\nUgh?? I didn't understand that choice. Please enter a valid input\n\n\n")
            time.sleep(2)
            continue
    medicsBuy(player_number)


## Input for Player 1
print("\n\nHello Commander 1, Welcome to the game. You now have 10$ to form an army.\nAny money which is left over "
      "after formation of the army will be used for medics which is sold at 1$ per unit.\n\n ")
input_player(0)
print("\n"*100)
## Input for Player 2
print("\n\nHello Commander 2, Welcome to the game. You now have 10$ to form an army.\nAny money which is left over "
      "after formation of the army will be used for medics which is sold at 1$ per unit.\n\n ")
input_player(1)

i = 0  # initialising a value to 0 to check and pop the unit of the loosing army
print("\n"*100)
fight_round = 0
print("\n"*100)
print("-------------------------------The fight begins now-------------------------------")
# This part of the code to find out the winner of the game
while len(player_units[0]) != 0 and len(player_units[1]) != 0:
    # this loop keeps comparing the army units and eliminating the loosing unit
    fight_round += 1
    print("\n\nRound "+str(fight_round)+" fight begins:\n")
    """the loop keeps going on till commander 1 or commander 2 are out of army units and the commander which
    looses all the units of army first is the loosing commander of the game"""

    if player_units[0][i] == "A":
        ##
        print("Commander 1 has his Archer on the battle field")
        if player_units[1][i] == "A":
            print("Commander 2 has his Archer on the battle field")
            player_units[0].pop(i)
            player_units[1].pop(i)
            print("This match was a tie between the units")
            continue
        if player_units[1][i] == "S":
            print("Commander 2 has his Soldier on the battle field")
            player_units[1].pop(i)
            print("Commander 1's unit Archer wins this round.")
            continue
            ##
        if player_units[1][i] == "K":
            print("Commander 2 has his Knight on the battle field")
            player_units[0].pop(i)
            print("Commander 2's Knight wins this round")
            continue
            ##
        if player_units[1][i] == "SE":
            print("Commander 2 has his Siege Equipment on the battle field")
            player_units[0].pop(i)
            print("Commander 2's Siege Equipment wins this round")
            continue

        if player_units[1][i] == "W":
            print("Commander 2 has his Wizard on the battle field")
            player_units[1].pop(i)
            print("Commander 1's Archer wins this round")
            continue

    if player_units[0][i] == "S":
        print("Commander 1 has his Soldier on the battle field")
        if player_units[1][i] == "A":
            print("Commander 2 has his Archer on the battle field")
            player_units[0].pop(i)
            print("Commander 2's Archer wins this round")
            continue
        if player_units[1][i] == "S":
            print("Commander 2 has his Soldier on the battle field")
            player_units[0].pop(i)
            player_units[1].pop(i)
            print("The match is a tie between the units")
            continue
        if player_units[1][i] == "K":
            print("Commander 2 has his Knight on the battle field")
            player_units[1].pop(i)
            print("Commander 1's Soldier wins this round")
            continue
            ##
        if player_units[1][i] == "SE":
            print("Commander 2 has his Siege Equipment on the battle field")
            player_units[0].pop(i)
            print("Commander 2's Siege Equipment wins this round")
            continue
            ##
        if player_units[1][i] == "W":
            print("Commander 2 has his Wizard on the battle field")
            player_units[0].pop(i)
            print("Commander 2's Wizard wins this round")
            continue

        ##
    if player_units[0][i] == "K":
        print("Commander 1 has his Knight on the battle field")
        if player_units[1][i] == "A":
            print("Commander 2 has his Archer on the battle field")
            player_units[1].pop(i)
            print("Commander 1's Knight wins this round")
            continue
            ##
        if player_units[1][i] == "S":
            print("Commander 2 has his Soldier on the battle field")
            player_units[0].pop(i)
            print("Commander 2's Soldier wins this round")
            continue
        ##
        if player_units[1][i] == "K":
            print("Commander 2 has his Knight on the battle field")
            player_units[0].pop(i)
            player_units[1].pop(i)
            print("This match is a tie between the units")
            continue
        if player_units[1][i] == "SE":
            print("Commander 2 has his Siege Equipment on the battle field")
            player_units[1].pop(i)
            print("Commander 1's Knight wins this round")
            continue
        if player_units[1][i] == "W":
            print("Commander 2 has his Wizard on the battle field")
            player_units[0].pop(i)
            print("Commander 2's Wizard wins this round")
            continue

    if player_units[0][i] == "SE":
        print("Commander 1 has his Siege Equipment on the battle field")
        if player_units[1][i] == "A":
            print("Commander 2 has his Archer on the battle field")
            player_units[1].pop(i)
            print("Commander 1's Siege Equipment wins this round")
            continue
            ##
        if player_units[1][i] == "S":
            print("Commander 2 has his Soldier on the battle field")
            player_units[1].pop(i)
            print("Commander 1's Siege Equipment wins this round")
            continue
        ##
        if player_units[1][i] == "K":
            print("Commander 2 has his Knight on the battle field")
            player_units[0].pop(i)
            print("Commander 2's Knight wins this round")
            continue
        if player_units[1][i] == "SE":
            print("Commander 2 has his Siege Equipment on the battle field")
            player_units[0].pop(i)
            player_units[1].pop(i)
            print("This match is a tie between the units")
            continue
        if player_units[1][i] == "W":
            print("Commander 2 has his Wizard on the battle field")
            player_units[0].pop(i)
            print("Commander 2's Wizard wins this round")
            continue

    if player_units[0][i] == "W":
        print("Commander 1 has his Wizard on the battle field")
        if player_units[1][i] == "A":
            print("Commander 2 has his Archer on the battle field")
            player_units[0].pop(i)
            print("Commander 2's Archer wins this round")
            continue
            ##
        if player_units[1][i] == "S":
            print("Commander 2 has his Soldier on the battle field")
            player_units[1].pop(i)
            print("Commander 1's Wizard wins this round")
            continue
        ##
        if player_units[1][i] == "K":
            print("Commander 2 has his Knight on the battle field")
            player_units[1].pop(i)
            print("Commander 1's Wizard wins this round")
            continue
        if player_units[1][i] == "SE":
            print("Commander 2 has his Siege Equipment on the battle field")
            player_units[1].pop(i)
            print("Commander 1's Wizard wins this round")
            continue
        if player_units[1][i] == "W":
            print("Commander 2 has his Wizard on the battle field")
            player_units[0].pop(i)
            player_units[1].pop(i)
            print("This match is a tie between the units")
            continue


    print("\n\n\n")

# This part of the code recognises the winning army and prints it out

if len(player_units[0]) == 0 and len(player_units[1]) != 0:
    print("\n\n\n\nCommander 2 is the winner of this game.\n\n\n\n")
elif len(player_units[0]) != 0 and len(player_units[1]) == 0:
    print("\n\n\n\nCommander 1 is the winner of this game.\n\n\n\n")
else:
    print("\n\n\n\nThis game is a tie between both the Commanders.\n\n\n\n")  # if the game is a tie then this is printed out
