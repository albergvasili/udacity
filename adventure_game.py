import time

progress = []


def printi(text):
    print(text)
    #time.sleep()

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
#"you run out of the tent" -> repeats twice.
    else:
        printi("'Do not run away from your destiny!'\n")
        valiant_question()


#Note to future self: Diverge chapters here.


    printi("You follow the long path to Naranya and enter through the gates")
    printi("You are surrounded by small white houses with orange roofs "
           "on both sides of the main road\n")
    
    printi("What would you like to do:")
    knock_or_road == input("Knock on a random door. (K)\n"
                          "Or follow the main road. (R) ").lower()
    
    if knock_or_road == "k":
        printi("You knock on a random door. Character answers.")
        printi("She looks at you with curiosity")
    #New function K??
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
            #Random messages for elses!

    elif knock_or_road != "k" and knock_or_road != "m":
        printi("A black cat approaches, meows at you, and leaves")
        #start function to ask again

    printi("You follow the main road 
