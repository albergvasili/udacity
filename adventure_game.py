import time

progress = []


def printi(text):
    print(text)
    # time.sleep()


def intro():
    printi("The mighty Celadon grabbed the old mysterious book.")
    printi("He deliberately opened a random page and read:")
    printi("When the Moon covered the Sun, the Valiant Explorer "
           "of the Soul gathered three mystic crystals and presented "
           "them to his master before midnight.")
    printi("Celadon stared at the infinite space in front of him.")
    printi("Suddenly, he closed the book and looked at you:\n")
    valiant_question()


def valiant_question():
    valiant_explorer = input("'Are you the Valiant Explorer of the Soul?'"
                             " (Y, N) ").lower()

    if valiant_explorer == "y":
        printi("'Indeed! There is no time to waste...")
        printi("Find the three crystals before midnight!'\n")
        printi("You walk out of the tent and look at the bright blue sky.")
        progress.append("Valiant")

    elif valiant_explorer == "n":
        printi("'Coward! Leave this tent and never come back!'\n")
        printi("You run out of the tent and look at the bright blue sky.")
        progress.append("Coward")
# "you run out of the tent" -> repeats twice.
    else:
        printi("'Do not run away from your destiny!'\n")
        valiant_question()

# Note to future self: Diverge chapters here.

    printi("You follow the long path to Naranya and enter through the gates")
    printi("You are surrounded by small white houses with orange roofs "
           "on both sides of the main road\n")

    printi("What would you like to do:")
    knock_or_road = input("Knock on a random door. (K)\n"
                          "Or follow the main road. (R) ").lower()

    if knock_or_road == "k":
        printi("You knock on a random door. Character answers.")
        printi("She looks at you with curiosity")
    # New function K??
        printi("What do you do?")
        villager_talk = input("Talk about mystic crystals. (C)\n"
                              "Or ask for water. (W)\n ").lower()

        if villager_talk == "c":
            printi("'CRYSTALS! Do NOT talk to me about Crystals!"
                   " Are you insane!'")
            printi("She slams the door. The people around stare at you.")
            progress.append("Kicked")

        elif villager_talk == "w":
            printi("'Here is some water, poor wanderer.'")
            printi("'You must be coming from the dark forest of Verdiul...")
            printi("'They say the dark wizard of oblivion lives there.'")
            progress.append("Water")

        else:
            printi("A fly buzzes in your ear.")
            # Random messages for elses!

    elif knock_or_road != "k" and knock_or_road != "r":
        printi("A black cat approaches, meows at you, and leaves")
        # start function to ask again

printi("You follow the road to the main plaza.")
printi("A young man is reading sitting by a tree nearby")
printi("There is a tall statue of a woman holding a shiny object...")
printi("It looks like a crystal.")
printi("What would you like to do:")


def plaza():
    progress = ["Water"]
    plaza_choice = input("Talk to young man. (T)\n"
                         "Or steal the shiny object. (S)\n").lower()

    if plaza_choice == "s":
        printi("You start climbing the statue and realize that the shiny "
               "object is indeed a crystal.")
        printi("As you reach and grab the crystal, a guard sees you and "
               "alerts the town.")
        printi("You put the crystal in your bag and quickly climb down.")
        printi("You run into an alley to avoid being seen")
        
        if "Water" or "Kicked" in progress:
            printi("The villager is in front of you")
            alley = input("Do you run back to the plaza. (B)\n"
                          "Or do you ask the villager for help. (H)\n").lower()
            
            if alley == "b":
                printi("You turn back and stop. The guards are getting close.")
                printi("There is an open window to your left.")
                printi("What would you like to do:")
                input("Fight the guards (F)\n"
                      "Or enter the house through the window (W)\n")
        
            elif alley == "h":
                if "Water" in progress:
                    printi("The villager recognizes you and grabs your hand.")
                    printi("She guides you through the alleys and takes you "
                           "to the city wall.")
                    printi("There is a tall tree that you can climb "
                           "to escape.")
                else:
                    printi("The villager starts yelling and tackles you")
                    printi("The guards arrive. You get arrested.")

            else:
                printi("The narrator gives you a threatening look")
            # call function to repeat question.
        else:
            printi("Lelolelo") # add death ending

   elif plaza_choice == "t":
       printi("WHa")

        printi("As you get ready to proceed, you have a cold feeling "
                "on your chest.")
        printi("An arrow pierced your heart. You feel the blood "
               "coming out of your body.")
        printi("You look up.")
        printi("The moon gets close to the sun as your life gets " 
               "eclipsed by the darkness.")

plaza()
