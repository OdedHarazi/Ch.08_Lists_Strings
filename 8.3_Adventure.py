'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random

Tanner = False
rock = False
dab = False
Money = False
sword = False
kidnap = False
Cash = False
Buy = False
Sell = False
Pawn = False
Monster = False
Sold = False
Tannersold = False
inventory = []
room_list = []

print("\n\033[1;36mWelcome to the Adventure Game! Look for items that will help you in different situations as you progress through the game! \nIn order to win you need to acquire $100, Buy Stocks, and Fight off a Monster!")
print("There is a max of 1 item per room, so keep moving once you acquire things\033[0;00m")
#room 0
room = ["Front Porch",2,None,None,None]
room_list.append(room)
#room 1
room = ["Bedroom 2",4,2,None,None]
room_list.append(room)
#room 2
room = ["South Hall",5,3,0,1]
room_list.append(room)
#room 3
room = ["Dining Room",6,None,None,2]
room_list.append(room)
#room 4
room = ["Bedroom 1",None,5,1,None]
room_list.append(room)
#room 5
room = ["North Hall",7,6,2,4]
room_list.append(room)
#room 6
room = ["Kitchen",None,None,3,5]
room_list.append(room)
#room 7
room = ["Balcony",None,None,5,None]
room_list.append(room)
current_room = 0
done = False
while not done:
    print("")
    print("\033[1;34mYou're in the " + room_list[current_room][0] + "\033[0;00m")
    print("")
    direction = input("\033[1;33mWhich way would you like to go?\033[0;00m\n\"N\" for North\n\"E\" for East\n\"S\" for South\n\"W\" for West\n\"I\" to Check your inventory\nor press \"Q\" to quit:")

#quit
    if direction.lower() == "q":
        done = True
        print("\033[1;32mThanks for playing!")
    elif direction.lower() == "i":
        print("Inventory", inventory)
#North
    elif direction.lower() == "n" or direction.lower() == "north":
        next_room = room_list[current_room][1]
        if room_list[current_room][1] == None:
            print("\033[1;31mYou can't go that way!")
        else:
            current_room = next_room
#East
    elif direction.lower() == "e" or direction.lower() == "east":
        next_room = room_list[current_room][2]
        if room_list[current_room][2] == None:
            print("\033[1;31mYou can't go that way!")
        else:
            current_room = next_room
#South
    elif direction.lower() == "s" or direction.lower() == "south":
        next_room = room_list[current_room][3]
        if room_list[current_room][3] == None:
            print("\033[1;31mYou can't go that way!")
        else:
            current_room = next_room
#West
    elif direction.lower() == "w" or direction.lower() == "west":
        next_room = room_list[current_room][4]
        if room_list[current_room][4] == None:
            print("\033[1;31mYou can't go that way!")
        else:
            current_room = next_room
#Invalid Responses
    else:
        print("\033[1;31mPlease type a valid response.\033[0;00m")


#Second time we see Tanner
    if room_list[current_room][0] == "Balcony" and Tanner == True and Tannersold == False:
        print("\033[1;33mIf you have already acquired Tanner, go sell him to the pawn machine. Otherwise read below:")
        interact = input("Tanner is still here. Would you like to interact with him now:\033[0;00m")
        if interact.lower() == "yes" or interact.lower() == "y" or interact.lower() == "yeah":
            acquire = input("\033[1;32mWould you like to assert your dominance on him? (Press Y):")
            if dab == False and acquire.lower() == "y" or acquire.lower() == "dominance":
                print("\033[1;31mTanner wants to fight\033[0;00m")
                if inventory == []:
                    loss = input("\033[1;33mYour inventory is empty!\nDo you want to fight Tanner bare handed?\033[0;00m")
                    if loss.lower() == "yes" or loss.lower() == "y" or loss.lower() == "yeah":
                        print("\033[1;31mTanner beat you up... You Lose!")
                        done = True
                    if loss.lower() == "no" or loss.lower() == "n":
                        print("\033[1;33mSmart Move...We'll get him next time\033[0;00m")
                    else:
                        print("Not an option!")
                else:
                    print("Choose an item from your inventory", inventory)
                    if attack.lower() == "sword":
                        print("Tanner saw your sword an ran away! Way to go!")
                    else:
                        print("Not an Option")
        else:
            print("Alright! Leave and reenter the room or check your inventory while in this room to see this message again")

#First time we see Tanner
    if room_list[current_room][0] == "Balcony" and Tanner == False and Tannersold == False:
        print("\033[1;34mYou're in the " + room_list[current_room][0] + "\033[0;00m")
        print("\033[1;33mYou've found Tanner! A \033[1;37m useful \033[1;33mitem!\033[0;00m")
        acquire = input("\033[1;32mWould you like to\033[1;33m\nKidnap Him (Press X)\033[0;00m\nor\n\033[1;33mScare him off (Press Y):\033[0;00m")
        if acquire.lower() == "kidnap him" or acquire.lower() == "x":
            inventory.append("Tanner")
            Tanner = True
            kidnap = True
            print("Inventory",inventory)
            print("")
            print("\033[1;31mThe Police are on their way!\033[0;00m")
            police = input("\033[1;32mWould you like to\033[1;33m\nJump off the Balcony (Press X)\033[0;00m\nor\n\033[1;33mChallenge the police (Press Y):\033[0;00m")
            if police.lower() == "jump off" or police.lower() == "x":
                print("\033[1;31mYou jumped off the balcony and broke your leg... you lose!\033[0;00m")
                done = True
            elif police.lower() == "challenge" or police.lower() == "y":
                print("\033[1;32mYou decided to challenge the police to a math off!")

#Police MiniGame

                print("\033[1;35mMiniGame: Police Math Off\033[0;00m")
                plays = 0
                win = 0
                lose = 0
                while plays <= 2:
                    num1= random.randrange(50)
                    num2= random.randrange(50)
                    print("\033[0;00mRound 1: What is ",num1, "+" ,num2, "?")
                    math = int(input("Type your answer here:"))
                    if math == num1+num2:
                        print("\033[1;32mCorrect!\033[0;00m")
                        win += 1
                        plays += 1
                    else:
                        print("\033[1;31mIncorrect!\033[0;00m")
                        lose += 1
                        plays += 1
                if lose >= win:
                    print("You got", lose, "incorrect answers!")
                    print("\033[1;31mYou lose! The police arrested you!\033[0;00m")
                    done = True
                else:
                    print("You got", win, "correct answers!")

                    print("\033[1;34mYou showed the police your epic math skills and succeeded in kidnapping Tanner\033[0;00m")



        elif dab == False and acquire.lower() == "y" or acquire.lower() == "dominance":
            print("\033[1;31mTanner wants to fight\033[0;00m")
            if inventory == []:
                loss = input("\033[1;35mYour inventory is empty!\nDo you want to fight Tanner bare handed? (Yes or No)\033[0;00m")
                if loss.lower() == "yes" or loss.lower() == "y" or loss.lower() == "yeah":
                    print("\033[1;31mTanner beat you up... You Lose!")
                    done = True
                elif loss.lower() == "no" or loss.lower() == "n":
                    print("\033[1;33mSmart Move...We'll get him next time\033[0;00m")
                else:
                    print("\033[1;31mNot an option!")
            else:
                print("Choose an item from your inventory below:")
                attack = input(inventory)
                if attack.lower() == "sword":
                    print("\033[1;32mTanner saw your sword an ran away! But you still need him to win the game!\033[0;00m")
                    print("\033[1;31mYou Lose!\033[0;00m")
                    done = True
                else:
                    print("\033[1;31mNot an Option\033[0;00m")
        else:
            print("\033[1;31mNot an Option!\033[0;00m")

#Finding Money
    if room_list[current_room][0] == "Bedroom 2" and Money == False:
        print("\033[1;34mYou're in the " + room_list[current_room][0] + "\033[0;00m")
        print("You've 20 dollars on your parents desk!")
        acquire = input("\033[1;32mWould you like to\033[0;00m\n\033[1;33mPocket the Money (Press X)\033[0;00m\nor\n\033[1;33mLeave it Alone (Press Y):\033[0;00m")
        if acquire.lower() == "pocket the money" or acquire.lower() == "x":
            Money = True
            print("\033[1;31mYour Mom enters the room as you are taking the money!\033[0;00m")
            mom = input("\033[1;32mWould you like to\033[0;00m\nApologize to your Mom  (Press X)\nor\nFight your Mom  (Press Y):")
            if mom.lower() == "apologize" or mom.lower() == "x":
                print("\033[1;32mYour Mom forgives you, but she took all of your prized possessions!\033[0;00m")
                sword = False
                Buy = False
                sell = False
                sold = False
                inventory = []
                print("Inventory", inventory)
            if mom.lower() == "fight" or mom.lower() == "y":
                print("\033[1;31mYou got woop'd by your mom...You Lose")
                done = True
        if acquire.lower() == "y" or acquire.lower() == "leave it alone":
            print("\033[1;31mYou get a phone call from your mom:\033[0;00m")
            call = input("\033[1;35m\nDo you want to pick up the phone? (Yes or No)\033[0;00m")
            if call.lower() == "yes" or call.lower() == "y" or call.lower() == "yeah":
                input("\033[1;32mHi Honey, I think I left a few dollars on my desk...   (Press Enter to Continue)")
                input("\033[1;33mYeah, I think you did Mom. I saw them earlier today.   (Press Enter to Continue)")
                input("\033[1;32mAnd you didn't take them...?   (Press Enter to Continue)")
                input("\033[1;33mOf Course Not Mom!...  (Press Enter to Continue)")
                input("\033[1;32mYou are such a trustworthy kid. Keep the money as a thanks! (Press Enter to Continue)\033[0;00m")
                inventory.append("20 Dollars")
                Money = True
                Cash = True
                print("Inventory", inventory)
            else:
                print("Phone Call Declined")
                print("Hint: Come back to this room to pickup the phone and acquire the money!")
#First time seeing the Pawn Machine
    if room_list[current_room][0] == "Dining Room" and Pawn == False:
        print("\033[1;34mYou're in the " + room_list[current_room][0] + "\033[0;00m")
        print("\033[1;32mYou see a pawn machine!")
        pawn = input("Would you like to interact with the pawn machine?\033[0;00m")
        if pawn.lower() == "y" or pawn.lower() == "yes":
            acquire = input("\033[1;34mWould you like to\033[0;00m\n\033[1;33mBuy Something(Press X)\033[0;00m\nor\n\033[1;33mSell Tanner(Press Y):\033[0;00m")
            if acquire.lower() == "buy something" or acquire.lower() == "x" and Buy == False and Cash == True:
                Buy = True
                print("You bought Stocks with your $20! Good Job!")
                inventory.append("Stocks")
                inventory.remove("20 Dollars")
                print("Inventory", inventory)
                print("Leave and reenter the room to interact with the pawn machine again!")

            elif acquire.lower() == "buy something" or acquire.lower() == "x" and Buy == False and Cash == False:
                print("\033[1;34mYou don't have any money!\033[0;00m")
            elif acquire.lower() == "buy something" or acquire.lower() == "x" and Buy == True:
                print("You already bought what was in the pawn machine!")
            elif acquire.lower() == "sell something" or acquire.lower() == "y":
                    sell = input("\033[1;33mWould you like to sell Tanner for \033[1;37m100 \033[1;33mdollars?\033[0;00m")
                    if kidnap == True and sell.lower() == "y" or sell.lower() == "yes":
                        Sold = True
                        Tannersold = True
                        inventory.append("$100 Dollars")
                        inventory.remove("Tanner")
                        print("Inventory", inventory)
                        print("You earned a lot of money!")
                        print("Leave and reenter the room to interact with the pawn machine again!")
                    elif sell.lower() == "y" or sell.lower() == "yes" and kidnap == False:
                        print("You don't have a Tanner in your inventory!")
                    elif sell.lower() == "n" or sell.lower() == "no":
                        print("Ok! Come back if you change your mind!")
                    else:
                        print("Not an option!")
        elif pawn.lower() == "n" or pawn.lower() == "no":
            print("Ok, come back to this room if you change your mind!")
        else:
            print("\033[1;31mNot an Option\033[0;00m")
    #Sword
    if room_list[current_room][0] == "Bedroom 1" and sword == False:
        print("\033[1;34mYou're in the " + room_list[current_room][0] + "\033[0;00m")
        print("\033[1:36mYou've found a sharp sword laying in your room! Very effective weapon\033[0:00m")
        sword = True
        inventory.append("Sword")
        print("Inventory", inventory)

        # Monster:
    if room_list[current_room][0] == "Kitchen" and Monster == False:
        print("\033[1;34mYou're in the " + room_list[current_room][0] + "\033[0;00m")
        print("\033[1;33mYou've found A Monster! A BOSS!\033[0;00m")
        battle = input("\033[1;32mWould you like to\033[1;33m\nRun Away (Press X)\033[0;00m\nor\n\033[1;33mFight The Monster(Press Y):\033[0;00m")
        if battle.lower() == "Run Away" or battle.lower() == "x":
            print("")
            print("\033[1;31mYou got away, but the Monster is still there in the corner!\033[0;00m")
        elif battle.lower() == "y" or battle.lower() == "fight":
            if inventory == []:
                loss = input("\033[1;35mYour inventory is empty!\nDo you want to fight the Monster bare handed? (Yes or No)\033[0;00m")
                if loss.lower() == "yes" or loss.lower() == "y" or loss.lower() == "yeah":
                    print("\033[1;31mThe Monster Beat You... You Lose!")
                    done = True
                elif loss.lower() == "no" or loss.lower() == "n":
                    print("\033[1;33mSmart Move...We'll get him next time\033[0;00m")
                    Tanner = True
                else:
                    print("\033[1;31mNot an option!")
            else:
                print("Choose an item from your inventory below to fight the monster with:")
                attack = input(inventory)
                if attack.lower() == "sword":
                    print("\033[1;32mYou beat the monster away with your sword! \033[0;00m")
                    Monster = True
                elif attack.lower() == "tanner":
                    print("\033[1;31mYou sacrificed Tanner and lost the game! \033[0;00m")
                    done = True
                elif attack.lower() == "stocks":
                    print("\033[1;32mYou ranted on about stocks and gave the monster a killer headache! \033[0;00m")
                    Monster = True
                else:
                    print("\033[1;31mNot an Option\033[0;00m")
#Winning
    if Monster == True and Buy == True and Sold == True:
        print("Congratulations! You've won the game!")
        import arcade;

        arcade.open_window(500, 500, "Oded's Amongaso"), arcade.set_background_color(
            arcade.color.EERIE_BLACK), arcade.start_render()

        x = -75
        a = 255
        b = 0
        c = 0

        while x <= 200:
            arcade.draw_circle_filled(x + 250, 250, 50, (a, b, c), )
            arcade.draw_ellipse_filled(x + 204, 203, 15, 130, (a, b, c), )
            arcade.draw_ellipse_filled(x + 288, 200, 20, 80, (a, b, c), )
            arcade.draw_ellipse_filled(x + 245, 175, 25, 90, (a, b, c), 100, )
            arcade.draw_ellipse_filled(x + 270, 250, 40, 80, arcade.color.COOL_GREY, 90, )
            arcade.draw_ellipse_filled(x + 270, 255, 40, 80, arcade.color.COOL_GREY, 90, )
            arcade.draw_ellipse_filled(x + 270, 260, 40, 80, arcade.color.COOL_GREY, 90, )
            arcade.draw_rectangle_filled(x + 245, 200, 95, 60, (a, b, c), )
            arcade.draw_ellipse_outline(x + 270, 255, 53, 83, arcade.color.BLACK, 3, 90, )
            arcade.draw_rectangle_filled(x + 195, 212, 15, 54, (a, b, c), )
            arcade.draw_circle_filled(x + 203, 242, 15, (a, b, c), )
            arcade.draw_circle_filled(x + 202, 192, 15, (a, b, c), )

            arcade.draw_rectangle_filled(x + 225, 160, 32.5, 40, (a, b, c), )
            arcade.draw_ellipse_filled(x + 221.5, 145, 30, 37.5, (a, b, c), 90, )

            arcade.draw_rectangle_filled(x + 275, 160, 37.5, 40, (a, b, c), 355)
            arcade.draw_ellipse_filled(x + 276.5, 145, 30, 37.5, (a, b, c), 85, )
            arcade.draw_text("Player", 100, 375, arcade.color.GREEN, 30)
            arcade.draw_text("Sussy", 100, 425, arcade.color.PINK_SHERBET, 15)
            arcade.draw_text("You've won the game!", 120, 65, arcade.color.YELLOW, 15)

            x += 200
            a = 0
            c = 255

        arcade.finish_render(), arcade.run()

        done = True
