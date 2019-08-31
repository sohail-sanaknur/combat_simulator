#############################################################
# Basic version of the Combact game {Assignment1 of FIT9133}#
#############################################################

#############################################################
# Student name:         Sohail.Sankanur                     #
# Monash Student ID:    29996368                            #
# Start Date:           18 Aug 2018                         #
# Last Modified Date:   23 Aug 2018                         #
#############################################################

## Explaination of solution which has been implemented:
# >> There are 2 players who are called Commander 1 and Commander 2 in this game
# >> They have to make an army and the members of the army has to be selected by them.
# >> Based on the selection of the army members the fight happens. The army members are called units
# >> The units fight in an order in which they have been selected by the commanders
# >> The units which win stay on the battlefield and the loosing unit dies
# >> The Commander who looses all the units in the battle the fastest is the losing commander


## Explaination of the code structure:
# >> In the code we have a function "input_player" which takes input of the players
# >> After the player/commander chooses the army units an input validation is done to check weather proper inputs were supplied for selection of the army units
# >> In the initial part of the code there is inputPlayer function is called from the main code and this takes input of the 2 Commander armies
# >> The units of the armies are stored in a list
# >> The comparision of the list is done and based on the rules which is given in the problem statement the comparision is done and the loosong
#    army unit is popped off the list
# >> The list which gets empty the fastest is the loosing Player or Commander
# >> In the last part of the code there are comparision statement and based on the comparisions the winning Commander is decided and printed out

import time

player_units = [[], []]  # Units which commanders select to form army
player_num_of_units = [0, 0]  # This is the total money which is given to a commander
total_money = [10, 10]   # this is the money to buy medics


def input_player(player_number):
    while total_money[player_number] > 0:
        print("Please enter the unit which you would like to add to the army. Select from the following options\n")
        print("1. Archer    Type 'a' to select this")
        print("2. Soldier   Type 's' to select this")
        print("3. Knights   Type 'k' to select this")
        print("4. Exit      Type 'e' to select this\n")
        player_input = input("Please make your choice(a/s/k/e):         ")
        player_input = player_input.upper()
        if player_input == "A" or player_input == "S" or player_input == "K":
            if player_input == "A":
                print("\nAn Archer unit has been added into the army\n\n")
            elif player_input == "S":
                print("\nA Soldier unit has been added into the army\n\n")
            else:
                print("\nA Knights unit has been added into the army\n\n")
            total_money[player_number] -= 1
            player_units[player_number].append(player_input)
        elif player_input == "E":
            final_exit_promt = ''
            final_exit_promt = input(f"\nYou have {total_money[player_number]}$ money left. " + "Are you sure you want to exit the selection of units {y or n}\t")

            if final_exit_promt == 'y':
                print("Thanks for selecting army units")
                break
            else:
                continue


        else:
            print("\n\n\nUgh?? I didn't understand that choice. Please enter a valid input\n\n\n")
            time.sleep(2)
            continue


## Input for Player 1
print("\n\nHello Commander 1, Welcome to the game. You now have 10$ to form an army\n\n ")
input_player(0)
print("\n" * 100)
## Input for Player 2
print("\n\nHello Commander 2, Welcome to the game. You now have 10$ to form an army\n\n ")
input_player(1)

print(player_units[0])
print(player_units[1])
fight_round = 0
print("\n" * 100)
print("-------------------------------The fight begins now-------------------------------")
i = 0
# This part of the code to find out the winner of the game
while len(player_units[0]) != 0 and len(player_units[1]) != 0:
    # this loop keeps comparing the army units and eliminating the loosing unit

    fight_round += 1
    print("\n\nRound " + str(fight_round) + " fight begins:\n")

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

    print("\n\n\n")

# This part of the code recognises the winning army and prints it out

if len(player_units[0]) == 0 and len(player_units[1]) != 0:
    print("\n\n\nCommander 2 is the winner of this game.\n\n\n")
elif len(player_units[0]) != 0 and len(player_units[1]) == 0:
    print("\n\n\nCommander 1 is the winner of this game.\n\n\n")
else:
    print(
        "\n\n\nThis game is a tie between both the Commanders.\n\n\n")  # if the game is a tie then this is printed out
