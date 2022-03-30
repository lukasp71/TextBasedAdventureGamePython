import random

#make a battle loop for when the user encounters an enemy
def battle_loop_beginner(user_damage, max_user_health):
    winner = 1
    user_health = max_user_health
    #set up different damage values for the enemy
    enemy_damage_lvl1 = 5
    enemy_damage_lvl2 = 6
    enemy_damage_lvl3 = 7
    enemy_damage_lvl4 = 8
    enemy_damage_lvl5 = 9
    enemy_damage_lvl6 = 10
    enemy_health = 35
    #randomly generate different enemy levels to determine the enemies damage output
    enemy_damage = random.randint(1, 6)
    if enemy_damage == 1:
        enemy_damage = enemy_damage_lvl1

    elif enemy_damage == 2:
        enemy_damage = enemy_damage_lvl2
        
    elif enemy_damage == 3:
        enemy_damage = enemy_damage_lvl3
        
    elif enemy_damage == 2:
        enemy_damage = enemy_damage_lvl4
        
    elif enemy_damage == 2:
        enemy_damage = enemy_damage_lvl5
        
    else:
        enemy_damage = enemy_damage_lvl6
    
    print("You've encountered an goblin")
    #set up a loop while the user and enemy both have above 0 health
    while user_health > 0 and enemy_health > 0:
        #print out both the users and enemies health
        print("\nUser health: {}".format(user_health))
        print("Enemy health: {}\n".format(enemy_health))
        #have the user choose an option whether to attack or heal
        print("What would you like to do(attack, heal): ",end = "")
        user_choice = input()
        while True:
            #set up a loop for choice verification
            if user_choice == "attack":
                #if the user chose attack the enemy loses health
                enemy_health -= user_damage
                print("You attacked the enemy. The enemy lost {} health.\n".format(user_damage))
                break
            elif user_choice == "heal":
                #if the user chooses heal their health increases by 25 and they cannot go over max health
                #if the users health is full have them enter another option
                if user_health == max_user_health:
                    print("You have max health. You cannot heal.\n")
                    print("Please try a different option: ", end = "")
                    user_choice = input()
                elif max_user_health - user_health < 25:
                    user_health = max_user_health
                    break
                else:
                    user_health += 25
                    break                
            else:
                #have the user re-enter a choice if they enter an invalid option
                print("Please enter a valid option(attack, heal): ",end = "")
                user_choice = input()
        if enemy_health > 0:
            #if the enemies health is greater than 0 than they attack you
            print("The enemy attacked you. You lost {} health.\n".format(enemy_damage))
            user_health -= enemy_damage
    #return the winner
    if user_health > enemy_health:
        winner = 0
        return winner
    elif enemy_health > user_health:
        winner = 1
        return winner

def battle_loop_monster(user_damage, max_user_health):
    winner = 1
    user_health = max_user_health
    enemy_damage = 15
    enemy_health = 70
    
    print("You've encountered a monster")
    
    while user_health > 0 and enemy_health > 0:
        print("\nUser health: {}".format(user_health))
        print("Enemy health: {}\n".format(enemy_health))
        print("What would you like to do(attack, heal): ",end = "")
        user_choice = input()
        while True:
            if user_choice == "attack":
                enemy_health -= user_damage
                print("You attacked the enemy. The enemy lost {} health.\n".format(user_damage))
                break
            elif user_choice == "heal":
                if user_health == max_user_health:
                    print("You have max health. You cannot heal.\n")
                    print("Please try a different option: ", end = "")
                    user_choice = input()
                elif max_user_health - user_health < 25:
                    user_health = max_user_health
                    break
                else:
                    user_health += 25
                    break
            else:
                print("Please enter a valid option(attack, heal): ",end = "")
                user_choice = input()
        if enemy_health > 0: 
            print("The enemy attacked you. You lost {} health.\n".format(enemy_damage))
            user_health -= enemy_damage
    if user_health > enemy_health:
        winner = 0
        return winner
    elif enemy_health > user_health:
        winner = 1
        return winner        

def battle_loop_troll(user_damage, max_user_health):
    winner = 1
    user_health = max_user_health
    enemy_damage = 20
    enemy_health = 200
    
    while user_health > 0 and enemy_health > 0:
        print("\nUser health: {}".format(user_health))
        print("Enemy health: {}\n".format(enemy_health))
        print("What would you like to do(attack, heal): ",end = "")
        user_choice = input()
        while True:
            if user_choice == "attack":
                enemy_health -= user_damage
                print("You attacked the enemy. The enemy lost {} health.\n".format(user_damage))
                break
            elif user_choice == "heal":
                if user_health == max_user_health:
                    print("You have max health. You cannot heal.\n")
                    print("Please try a different option: ", end = "")
                    user_choice = input()
                elif max_user_health - user_health < 35:
                    user_health = max_user_health
                    break
                else:
                    user_health += 35
                    break
            else:
                print("Please enter a valid option(attack, heal): ",end = "")
                user_choice = input()
        if enemy_health > 0: 
            print("The enemy attacked you. You lost {} health.\n".format(enemy_damage))
            user_health -= enemy_damage
    if user_health > enemy_health:
        winner = 0
        return winner
    elif enemy_health > user_health:
        winner = 1
        return winner
    
#set up variables     
user_health = 50
max_user_health = 50
user_damage = 10
map = 0
key = 0
#have you user know to hit "enter" after each line
print("Follow the directions from the text and hit \"Enter\" after each line to reveal a new line of printed code")
#have the user enter a name 
print("Please enter your name: ",end = "")
user_name = input()
print()
print("It's time, {}, for you to begin your adventure.".format(user_name))
#make the code a loop so it breaks when the users health drops below 0
while user_health > 0:
    print("After a long nights sleep you wake up with a sense of adventure.")
    input()
    print("Luckily for you, you live near a cave that is great to explore, so you take you sword, some healing potions, and a flashlight and put them in your bag")
    input()
    print("You then head out to explore the cave")
    input()
    print("As you leave your house you head towards the cave.")
    input()
    print("However, on your way you get attacked by a goblin.")
    input()
    print("It looks like the only way to pass is to beat him in battle.")
    input()
    print("You draw your sword and prepare to fight.")
    input()
    winner = battle_loop_beginner(user_damage, max_user_health)
    #after the battle if the user lost break out of the loop and end the program   
    if winner == 1:
        print("The enemy won. You lost.")
        break
    #if the user won increase their attack and health by 1
    elif winner == 0:
        print("{} won!".format(user_name))
        max_user_health += 1
        user_damage += 1
        print("Your health and damage increased by 1")
    input()
    print("You continue making your way to the cave")
    input()
    print("As you approach the enterance you feel a strong gust of wind as well as a voice saying enter at your own risk.")
    input()
    print("Ignoring the warning you enter the cave.")
    input()
    print("Once you enter boulders fall down blocking the enterance and your only way out")
    input()
    print("With the enterance blocked the cave is pitch black, you pull out you flashlight to help you find your way through the cave.")
    input()
    print("The only option seems to be to move forward")
    input()
    print("You shine your flashlight around to hope to find your way through")
    input()
    print("As you shine your flahslight against the walls of the cave you see a hole in the wall")
    input()
    print("Would you like the enter the hole?(y/n): ",end = "")
    user_option = input()
    #use a loop for input verification to make sure the user enters the right input
    while True:
        if user_option == "y":
            break
        elif user_option == "n":
            break
        else:
            print("\nPlease enter a valid option")
            print("\nWould you like the enter the hole?(y/n): ",end = "")
            user_option = input()
    #display different messages depending on what option the user chooses
    if user_option == "y":
        print()
    elif user_option == "n":
        print("\nWhat would you like to do?(explore/enter hole): ",end = "")
        user_choice = input()
        while True:
            if user_choice == "enter hole":
                print()
                break
            elif user_choice == "explore":
                break
            else:
                print("\nPlease enter a valid option\n")
                print("What would you like to do?(explore/enter hole): ",end = "")
                user_choice = input()
            
        if user_choice == "explore":
            print("\nInstead of going through the hole you continue through the beginning section of the cave")
            input()
            print("While exploring your find a chest, would you like to open it?(y/n): ",end = "")
            chest_option = input()
            while True:
                if chest_option == "y":
                    break
                elif chest_option == "n":
                    break
                else:
                    print("\nPlease enter a valid option\n")
                    print("While exploring your find a chest would you like to open?(y/n): ",end = "")
                    chest_option = input()
            
            if chest_option == "y":
                #if the user opens the chest increase their attack by 2
                print("\nYou decide to open the chest, inside you find an upgrade to your weapon.")
                input()
                user_damage += 2
                print("Your attack power increased by 2.")
                input()
                print("As you turn around a goblin pops out and attacks you.")
                input()
                winner = battle_loop_beginner(user_damage, max_user_health)
                #after the battle end the code if the user lost
                if winner == 1:
                    print("The enemy won. You lost.")
                    break
                #if the user won increase their health by 1
                elif winner == 0:
                    print("{} won!".format(user_name))
                    max_user_health += 1
                    print("Your health increased by 1")
                    print("Would you like to continue to keep exploring or enter the hole?(explore/enter hole): ",end = "")
                    user_choice = input()
                    while True:
                        if user_choice == "explore":
                            print("It seems like there nothing left here the only option seems to be to keep moving forward.")
                            break
                        elif user_choice == "enter hole":
                            break
                        else:
                            print("\nPlease enter a valid option\n")
                            print("Would you like to continue to keep exploring or enter the hole?(explore/enter hole): ",end = "")
                            user_choice = input()
            if chest_option == "n":
                print("Would you like to continue to keep exploring or enter the hole?(explore/enter hole): ",end = "")
                user_choice = input()
                while True:
                    if user_choice == "explore":
                        print("It seems like there nothing left here the only option seems to be to keep moving forward.")
                        break
                    elif user_choice == "enter hole":
                        break
                    else:
                        print("Please enter a valid option\n")
                        print("Would you like to continue to keep exploring or enter the hole?(explore/enter hole): ",end = "")
                        user_choice = input()
    print("As you enter the hole you see a faint flicker of light at the end of a long hallway")
    input()
    print("You decide to make your way towards it")
    input()
    print("As you walk towards the light you feel your foot step on pannel on the ground")
    input()
    print("Suddenly a trap door opens up underneath you and you fall through the opening")
    input()
    print("Once you hit the group you look up and see the trap door close trapping you down where you fell")
    input()
    print("As you look around an notice you're in an arena")
    input()
    print("Skattered in different spots around the arena are what appear to be bones")
    input()
    print("It looks the people they belonged to had been attacked by something")
    input()
    print("You decide it's best to get out of this place before something happens to you")
    input()
    print("As you scan the room you see a gate on the far end of the arena")
    input()
    print("You make your way over the it but it is locked and you can get through")
    input()
    print("Before you can try and find a way to unlock the gate you're attacked by something")
    input()
    winner = battle_loop_monster(user_damage, max_user_health)
    if winner == 1:
        print("The enemy won. You lost.")
        break
    elif winner == 0:
        print("{} won!".format(user_name))
        max_user_health += 2
        print("Your total health increased by 2")
    print("After beating the monster you make you way over to the gate")
    input()
    print("After attempting to open it you realise the gate is locked")
    input()
    print("Maybe you can find a key around to help unlock it")
    input()
    print("You should try exploring the arena you're in to see if you can find something")
    input()
    print("Where would you like to search(bones/monster remains)? ",end = "")
    user_choice = input()
    while True:
        if user_choice == "bones":
            print()
            print("As you search around the bones you find a map that shows a vaugely familiar area")
            input()
            print("You can tell that it is a map of the cave by the big arena portion and the enterance is exactly the same as the enterance to the cave")
            input()
            print("This map might be able to help you escape and get out")
            input()
            print("However, you can't use the map until you find a key to unlock the gate and keep going")
            input()
            print("You should probably keep exploring to find a key to unlock the gate")
            input()
            #if the user finds the map increase the map variable to 1
            map = 1
            print("What would you like the explore now(bones/monster remains)? ",end = "")
            user_choice = input()
            while True:
                #set up different test options depending on what the user has and hasnt't explored yet
                if user_choice == "bones":
                    print("There doesn't seem much else in the pile of bones that is helpful")
                    input()
                    print("Maybe you should try exploring something else")
                    input()
                    print("What would you like the explore(monster remains)? ",end = "")
                    user_choice = input()
                    while True:
                        if user_choice == "monster remains":
                            #if the user hasn't found the key yet display the following
                            if key == 0:
                                print("As you search around the beast you slayed you find a chain wrapped around it's neck")
                                input()
                                print("The chain appears to be attached to a small brass key")
                                input()
                                print("You remove the chain and walk over to the gate to see if the key will fit")
                                input()
                                print("When you enter the key it fits perfectly and the gate opens")
                                input()
                                print("Would you like to pass through the gate or keep exploring(pass through/explore)? ",end = "")
                                user_choice = input()
                                #break the user out of the loop depending on what they choose
                                #set up a loop for input verification
                                while True:
                                    if user_choice == "pass through":
                                        break
                                    elif user_choice == "explore":
                                        print("After searching around a bit more you realise there's nothing else here and decide to pass through the gate")
                                        break
                                    else:
                                        print("\nPlease enter a valid option")
                                        print("Would you like to pass through the gate or keep exploring(pass through/explore)? ",end = "")
                                        user_choice = input()
                            break
                        
            
                        else:
                            #if the user enters an invalid option remind them of the options and have them re-enter an input
                            print("\nPlease enter a valid option")
                            print("What would you like the explore(monster remains)? ",end = "")
                            user_option = input()
                    break
                        
                elif user_choice == "monster remains":
                    if key == 0:
                        print("As you search around the beast you slayed you find a chain wrapped around it's neck")
                        input()
                        print("The chain appears to be attached to a small brass key")
                        input()
                        print("You remove the key and walk over to the gate to see if it will fit")
                        input()
                        print("When you enter the key it fits perfectly and the gate opens")
                        input()
                        print("Would you like to pass through the gate or keep exploring(pass through/explore)? ",end = "")
                        user_choice = input()
                        while True:
                            if user_choice == "pass through":
                                break
                            elif user_choice == "explore":
                                print("After searching around a bit more you realise there's nothing else here and decide to pass through the gate")
                                break
                            else:
                                print("\nPlease enter a valid option")
                                print("Would you like to pass through the gate or keep exploring(pass through/explore)? ",end = "")
                                user_choice = input()
                    break
                
                else:
                    print("\nPlease enter a valid option")
                    print("What would you like the explore now(bones/monster remains)? ",end = "")
                    user_choice = input()
            break
                
                    
                    
        elif user_choice == "monster remains":
            print("As you search around the beast you slayed you find a chain wrapped around it's neck")
            input()
            print("The chain appears to be attached to a small brass key")
            input()
            print("You remove the chain and walk over to the gate to see if the key will fit")
            input()
            print("When you enter the key it fits perfectly and the gate opens")
            input()
            print("Would you like to pass through the gate or keep exploring(pass through/explore)? ",end = "")
            key = 1
            user_choice = input()
            while True:
                if user_choice == "pass through":
                    break
                elif user_choice == "explore":
                    print("What would you like the explore(bones/monster remains)? ",end = "")
                    user_choice = input()
                    while True:
                        if user_choice == "bones":
                            if map == 0:
                                print()
                                print("As you search around the bones you find a map that shows a vaugely familiar area")
                                input()
                                print("You can tell that it is a map of the cave by the big arena portion and the enterance is exactly the same as the enterance to the cave")
                                input()
                                print("This map might be able to help you escape and get out")
                                input()
                                print("Using the map might be able to help you find your way once you pass through the gate")
                                input()                                    
                                map = 1
                                print("What would you like the do now(explore/enter gate)? ",end = "")
                                user_choice = input()
                                while True:
                                    if user_choice == "explore":
                                        print("There doesn't seem like there's anything else to explore here")
                                        input()
                                        print("You enter the gate and decide to continue forward")
                                        input()
                                        break
                                    elif user_choice == "enter gate":
                                        break
                                    else:
                                        print("\nPlease enter a valid option")
                                        print("What would you like the do now(explore/enter gate)? ",end = "")
                                        user_choice = input()
                            break

                                                 
                        elif user_choice == "monster remains":
                            print("There doesn't seem much else to the monster")
                            input()
                            print("Where would you like to go(bones/through gate)? ",end = "")
                            user_choice = input()
                            while True:
                                if user_choice == "through gate":
                                    break
                                elif user_choice == "bones":
                                    print()
                                    print("As you search around the bones you find a map that shows a vaugely familiar area")
                                    input()
                                    print("You can tell that it is a map of the cave by the big arena portion and the enterance is exactly the same as the enterance to the cave")
                                    input()
                                    print("This map might be able to help you escape and get out")
                                    input()
                                    print("Using the map might be able to help you find your way once you pass through the gate")
                                    input()                                    
                                    map = 1
                                    print("What would you like the do now(explore/enter gate)? ",end = "")
                                    user_choice = input()
                                    while True:
                                        if user_choice == "explore":
                                            print("There doesn't seem like there's anything else to explore here")
                                            input()
                                            print("You enter the gate and decide to continue forward")
                                            input()
                                            break
                                        elif user_choice == "enter gate":
                                            break
                                        else:
                                            print("\nPlease enter a valid option")
                                            print("What would you like the do now(explore/enter gate)? ",end = "")
                                            user_choice = input()
                                        break
                                    break
                                else:
                                    print("\nPlease enter a valid option")
                                    print("Where would you like to go(bones/through gate)? ",end = "")
                                    user_choice = input()
                            break
                        else:
                            print("\nPlease enter a valid option")
                            print("What would you like the explore(bones/monster remains)? ",end = "")
                            user_choice = input()
                    break
                            
                else:
                    print("\nPlease enter a valid option")
                    print("Would you like to pass through the gate or keep exploring(pass through/explore)? ",end = "")
                    user_choice = input()
                    
            break
        else:
            print("\nPlease enter a valid option")
            print("Where would you like to search(bones/monster remains)? ",end = "")
            user_choice = input()
            

                                    
    print("As you pass thorugh the gate you see 2 sets of stairs one leading down and deeper into the cave and the other leading upwards")
    input()
    #if the user found the map ask them if they want to use it
    if map == 1:
        print("Would you like the use the map to help you find your way(y/n)? ",end = "")
        user_choice = input()
        #set up a loop for input verification
        while True:
            if user_choice == "y":
                print("You pull out the map you found to see which way to go")
                input()
                print("It seems as if the set of stairs leading upwards will take you to the direction of the cave you entered in from")
                input()
                print("However, the lower section seems to lead to some kind of treasure")
                input()
                print("Which set of stairs would you like the take(up/down)? ",end = "")
                user_choice = input()
                while True:
                    if user_choice == "up":
                        break
                    
                    elif user_choice == "down":
                        break
                        
                    else:
                        print("\nPlease enter a valid option")
                        print("Which set of stairs would you like the take(up/down)? ",end = "")
                        user_choice = input()
                break
            elif user_choice == "n":
                print("You decide to go forward without using the map")
                input()
                print("Which set of stairs would you like the take(up/down)? ",end = "")
                user_choice = input()
                while True:
                    if user_choice == "up":
                        break
                    
                    elif user_choice == "down":
                        break
                    
                    else:
                        print("\nPlease enter a valid option")
                        print("Which set of stairs would you like the take(up/down)? ",end = "")
                        user_choice = input()
                    
                break
            else:
                print("\nPlease enter a valid option")
                print("Would you like the use the map to help you find your way(y/n)? ",end = "")
                user_choice = input()
    else:
        print("Which set of stairs would you like the take(up/down)? ",end = "")
        user_choice = input()
        while True:                
            if user_choice == "up":
                break
            elif user_choice == "down":
                break
            else:
                print("\nPlease enter a valid option")
                print("Which set of stairs would you like the take(up/down)? ",end = "")
                user_choice = input()
    
    if user_choice == "up":
        print("You decide to travel up the stairs")
        input()
        print("As you get closer to the top you can see a light")
        input()
        print("Once you reach the top you find yourself in a torch lit room")
        input()
        print("Underneath one of the torches is a lever")
        input()
        print("Would you like the pull the lever(y/n)? ",end = "")
        user_choice = input()
        while True:
            if user_choice == "y":
                break
            elif user_choice == "n":
                break
            else:
                print("\nPlease enter a valid option")
                print("Would you like the pull the lever(y/n)? ",end = "")
                user_choice = input()
                
        if user_choice == "n":
            print("If you don't want to pull the lever you can head back down the stairs")
            input()
            print("Would you like to head down the stairs or pull the lever(stairs/pull lever)? ",end = "")
            user_choice = input()
            while True:
                if user_choice == "stairs":
                    break
                elif user_choice == "pull lever":
                    print("You decide to pull the lever")
                    input()
                    print("You hear a lound BOOM in the distance")
                    input()
                    print("Would you like the head in the direction of the noise(y/n)? ",end = "")
                    user_choice = input()
                    while True:
                        if user_choice == "y":
                            break
                        elif user_choice == "n":
                            break
                        else:
                            print("\nPlease enter a valid option")
                            print("Would you like the head in the direction of the noise(y/n)? ",end = "")
                            user_choice = input()
                    break
                        
                if user_choice == "y":                        
                    print("You decide the head towards the noise")
                    input()
                    print("As you head towards the direction of the sound you find yourself in a long hallway")
                    input()
                    print("Soemthing about it seems familiar")
                    input()
                    print("As you get closer to the other end you see a hole in the wall")
                    input()
                    print("Thats when you realise this was the hallway you were walking down before you fell into the arena")
                    input()
                    print("This time you make sure to avoid the trap door when you walk by it")
                    input()
                    print("As you enter the hole you see that the boulders blocking your exit are gone")
                    input()
                    print("Deciding you've had enough adventure for one day you exit the cave and head back home")
                    input()
                    break
                
                elif user_choice == "n":
                    print("You can head back down the stairs and go down the other set of stairs from before or head towards the dirction of the noise")
                    input()
                    print("Which direction do you want to head in(stairs/noise)? ",end = "")
                    user_choice = input()
                    while True:
                        if user_choice == "stairs":
                            break
                        elif user_choice == "noise":
                            break
                        else:
                            print("\nPlease enter a valid option")
                            print("Which direction do you want to head in(stairs/noise)? ",end = "")
                            user_choice = input()
                        
                    if user_choice == "noise":
                        print("You decide the head towards the noise")
                        input()
                        print("As you head towards the direction of the sound you find yourself in a long hallway")
                        input()
                        print("Soemthing about it seems familiar")
                        input()
                        print("As you get closer to the other end you see a hole in the wall")
                        input()
                        print("Thats when you realise this was the hallway you were walking down before you fell into the arena")
                        input()
                        print("This time you make sure to avoid the trap door when you walk by it")
                        input()
                        print("As you enter the hole you see that the boulders blocking your exit are gone")
                        input()
                        print("Deciding you've had enough adventure for one day you exit the cave and head back home")
                        input()
                        break
                    if user_choice == "stairs":
                        print()

                
        if user_choice == "y":
            print("You decide to pull the lever")
            input()
            print("You hear a lound BOOM in the distance")
            input()
            print("Would you like the head in the direction of the noise(y/n)? ",end = "")
            user_choice = input()
            while True:
                if user_choice == "y":
                    break
                elif user_choice == "n":
                    break
                else:
                    print("\nPlease enter a valid option")
                    print("Would you like the head in the direction of the noise(y/n)? ",end = "")
                    user_choice = input()

            if user_choice == "y":
                    
                print("You decide the head towards the noise")
                input()
                print("As you head towards the direction of the sound you find yourself in a long hallway")
                input()
                print("Soemthing about it seems familiar")
                input()
                print("As you get closer to the other end you see a hole in the wall")
                input()
                print("Thats when you realise this was the hallway you were walking down before you fell into the arena")
                input()
                print("This time you make sure to avoid the trap door when you walk by it")
                input()
                print("As you enter the hole you see that the boulders blocking your exit are gone")
                input()
                print("Deciding you've had enough adventure for one day you exit the cave and head back home")
                input()
                break
            
            elif user_choice == "n":
                print("You can head back down the stairs and go down the other set of stairs from before or head towards the dirction of the noise")
                input()
                print("Which direction do you want to head in(stairs/noise)? ",end = "")
                user_choice = input()
                while True:
                    if user_choice == "stairs":
                        break
                    elif user_choice == "noise":
                        break
                    else:
                        print("\nPlease enter a valid option")
                        print("Which direction do you want to head in(stairs/noise)? ",end = "")
                        user_choice = input()
                    
                if user_choice == "noise":
                    print("You decide the head towards the noise")
                    input()
                    print("As you head towards the direction of the sound you find yourself in a long hallway")
                    input()
                    print("Soemthing about it seems familiar")
                    input()
                    rint("As you get closer to the other end you see a hole in the wall")
                    input()
                    print("Thats when you realise this was the hallway you were walking down before you fell into the arena")
                    input()
                    print("This time you make sure to avoid the trap door when you walk by it")
                    input()
                    print("As you enter the hole you see that the boulders blocking your exit are gone")
                    input()
                    print("Deciding you've had enough adventure for one day you exit the cave and head back home")
                    input()
                    break
                if user_choice == "stairs":
                    print()
                        
    if user_choice == "down":
        print()
    
    print("After heading down the stairs")
    input()
    print("You find yourself in a large torch lit room")
    input()
    print("At the end of the room you see a large jewl next to a treasure chest")
    input()
    print("You make your way over to the other end of the room")
    input()
    print("Once you get to the jewl and chest you can't seem to help yourself and decide to open the chest")
    input()
    print("Luckily for you there was a better sword inside the chest")
    input()
    user_damage += 5
    print("Your damage increased by 5")
    input()
    print("Before you can take the jewel you a someone approaching from behind you")
    input()
    print("Before you can turn around you hear something behind you say \"Do not touch the treasure\" ")
    input()
    print("When you turn around you see a giant troll standing behind you")
    input()
    print("He pulls out his club and swing it at you")
    input()
    print("However, you quickly dodge the club before it hits you")
    input()
    print("Just like before the only way past seems to be to defeat him")
    input()
    print("However, it doesn't seem like he will be going down easily at all")
    input()
    winner = battle_loop_troll(user_damage, max_user_health)
    if winner == 1:
        print("The enemy won. You lost.")
        break
    elif winner == 0:
        print("{} won!".format(user_name))    
        
    print("You have succesfully slain the troll")
    input()
    print("Would you like the grab the jewel(y/n)? ",end = "")
    user_choice = input()
    while True:
        if user_choice == "y":
            break
        elif user_choice == "n":
            break
        else:
            print("\nPlease enter a valid option")
            print("Would you like the grab the jewel(y/n)? ",end = "")
            user_choice = input()
    if user_choice == "y":
        print("As soon as you take the jewel you hear the cave around you begin to rumble")
        input()
        print("You suddenly start to feel small rocks fall down from the ceiling and bounce off you")
        input()
        print("It seems as if the cave is starting to collapse")
        input()
        print("The only way out is back up the stairs")
        input()
        print("You quickly put the jewel in the bag and bolt up the stairs")
        input()
        print("When you reach the top of the stairs you see the arena from where you had slain the monster")
        input()
        print("The only other way to go is up the other set of stairs")
        input()
        print("You quickly run of the stairs as the cave begins to collapse even more")
        input()
        print("When you reach the top of the stairs you come at a torch lit room with a long hallway extending out of the side of the room")
        input()
        print("Wuthout have enough time to look around the room you run into the hallway")
        input()
        print("As you run down the hallway it seems familiar, but you can't think as you only have limited time before the cave collapses on top of you")
        input()
        print("As you get closer to the end you see a small hole in the wall")
        input()
        print("that's when you realise that this is the hallway that you came accross earlier before you fell down the trap door")
        input()
        print("Remembering this you quickly avoid the trap door this time around and dash through the hole")
        input()
        print("As you enter the hole you see that the boulders blocking the enteracne have shifted and you can barely squeeze your way through")
        input()
        print("You barely make it through the exit before you heard the cave collaspe behind you")
        input()
        print("You succesfully made it out!")
        input()
        print("You take your jewel and head back home deciding you've had enough adventure for the day")
        break
    
    elif user_choice == "n":
        print("Instead of taking the jewel the only way out seems to be up the stair case you desceneded to get here")
        input()
        print("What would you like the do(take jewel/up staircase)? ",end = "")
        user_choice = input()
        while True:
            if user_choice == "take jewel":
                break
            elif user_choice == "up staircase":
                break
            else:
                print("\nPlease enter a valid option")
                print("What would you like the do(take jewel/up staircase)? ",end = "")
                user_choice = input()
                
        if user_choice == "take jewel":
            print("As soon as you take the jewel you hear the cave around you begin to rumble")
            input()
            print("You suddenly start to feel small rocks fall down from the ceiling and bounce off you")
            input()
            print("It seems as if the cave is starting to collapse")
            input()
            print("The only way out is back up the stairs")
            input()
            print("You quickly put the jewel in the bag and bolt up the stairs")
            input()
            print("When you reach the top of the stairs you see the arena from where you had slain the monster")
            input()
            print("The only other way to go is up the other set of stairs")
            input()
            print("You quickly run of the stairs as the cave begins to collapse even more")
            input()
            print("When you reach the top of the stairs you come at a torch lit room with a long hallway extending out of the side of the room")
            input()
            print("Wuthout have enough time to look around the room you run into the hallway")
            input()
            print("As you run down the hallway it seems familiar, but you can't think as you only have limited time before the cave collapses on top of you")
            input()
            print("As you get closer to the end you see a small hole in the wall")
            input()
            print("that's when you realise that this is the hallway that you came accross earlier before you fell down the trap door")
            input()
            print("Remembering this you quickly avoid the trap door this time around and dash through the hole")
            input()
            print("As you enter the hole you see that the boulders blocking the enteracne have shifted and you can barely squeeze your way through")
            input()
            print("You barely make it through the exit before you heard the cave collaspe behind you")
            input()
            print("You succesfully made it out!")
            input()
            print("You take your jewel and head back home deciding you've had enough adventure for the day")
            break
            
        elif user_choice == "up staircase":
            print("You head back up the way you came")
            input()
            print("When you reach the top you can either enter the arena or go up the other set up stairs")
            input()
            print("What do you want to do(enter arena/up stairs)? ",end = "")
            user_choice = input()
            while True:
                if user_choice == "enter arena":
                    break
                elif user_choice == "up stairs":
                    break
                else:
                    print("\nPlease enter a valid option")
                    print("What do you want to do(enter arena/up stairs)? ",end = "")
                    user_choice = input()
                    
            if user_choice == "enter arena":
                print("When you enter the arena you begin the explore the see if you can find anything new")
                input()
                print("After looking around a bit you realise nothing has changed since you were last in here")
                input()
                print("You head back through the gate")
                input()
                print("Where would you like the go(up stairs/enter arena)? ",end = "")
                user_choice = input()
                while True:
                    if user_choice == "up stairs":
                        break
                    elif user_choice == "enter arena":
                        print("When you enter the arena you begin the explore the see if you can find anything new")
                        input()
                        print("After looking around a bit you realise nothing has changed since you were last in here")
                        input()
                        print("You head back through the gate")
                        input()
                        print("Where would you like the go(up stairs/enter arena)? ",end = "")
                        user_choice = input()
                    
                    else:
                        print("\nPlease enter a valid option")
                        print("What do you want to do(enter arena/up stairs)? ",end = "")
                        user_choice = input()
                        
            if user_choice == "up stairs":
                print("You decide to travel up the stairs")
                input()
                print("As you get closer to the top you can see a light")
                input()
                print("Once you reach the top you find yourself in a torch lit room with a long hallway extending of the side of the room")
                input()
                print("Underneath one of the torches is a lever")
                input()
                print("Indulging your curiosity you decide the pull the lever")
                input()
                print("You hear a large BOOM noise off in the direction of the hallway")
                input()
                print("Contuing to indulge your curiosity you head down the hallway in the direction of the noise")
                input()
                print("As you walk down the hallway something about it seems familiar")
                input()
                print("As you get closer to the other end you see a hole in the wall")
                input()
                print("Thats when you realise this was the hallway you were walking down before you fell into the arena")
                input()
                print("This time you make sure to avoid the trap door when you walk by it")
                input()
                print("As you enter the hole you see that the boulders blocking your exit are gone")
                input()
                print("Deciding you've had enough adventure for one day you exit the cave and head back home")
                input()
                break              
    
    
    
                    
                        
        
                

        
    
    


    
    