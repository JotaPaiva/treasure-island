print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

left_or_right = input("\nYou are at a cross road. Where do you want to go? [left/right]: ")

if left_or_right == "Left" or left_or_right == "left" or left_or_right == "LEFT":
    print("\nYou have come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input("Do you want to wait for a boat or swim across? [wait/swim]: ")
    
    if wait_or_swim == "Wait" or wait_or_swim == "wait" or wait_or_swim == "WAIT":
        print("\nYou arrive at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow and one blue. Which colour do you choose: ")

        if door == "Yellow" or door == "yellow" or door == "YELLOW":
            print("\nYou found the treasure! YOU WIN!")
        elif door == "Blue" or door == "blue" or door == "BLUE":
            print("\nYou were eaten by beasts. Game over!")
        elif door == "Red" or door == "red" or door == "RED":
            print("\nIt's a room full of fire. Game over!")
        else:
            print("\nGame over!")

    else:
        print("\nYou get attacked by an angry trout. Game over!")

else:
    print("\nYou fell into a hole. Game over!")
