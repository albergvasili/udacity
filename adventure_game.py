import time

progress = []


def printi(text):
    print(text)
    time.sleep(1)


def intro():
    printi("The mighty Celadon grabbed the old mysterious book.")
    printi("He deliberately opened a random page and read:")
    printi("'When the Moon covered the Sun, the Valiant Explorer "
           "of the Soul gathered three mystic crystals and presented "
           "them to his master before midnight.'")
    printi("Celadon stared at the infinite space in front of him.")
    printi("Suddenly, he closed the book and looked at you:\n")
    valiant_question()


def valiant_question():
    valiant_explorer = input("'Are you the Valiant Explorer of the Soul?'"
                             " (Y)/(N)").lower()

    if valiant_explorer == "y":
        printi("'Indeed! There is no time to waste...")
        printi("Find the three crystals before midnight!'\n")
        printi("You walk out of the tent and look at the bright blue sky.")
        progress.append("Valiant")
        Naranya()

    elif valiant_explorer == "n":
        printi("'Coward! Leave this tent and never come back!'\n")
        printi("You run out of the tent and look at the bright blue sky.")
        progress.append("Coward")
        Naranya()
# "you run out of the tent" -> repeats twice.
    else:
        printi("'Do not run away from your destiny!'\n")
        valiant_question()


# Note to future self: Diverge chapters here.


def Naranya():
    printi("You follow the long path to Naranya and enter through the gates.")
    printi("You are surrounded by small white houses with orange roofs "
           "on both sides of the main road.\n")
    Naranya_knock_road()



def Naranya_knock_road():
    printi("What would you like to do:")
    knock_or_road = input("Knock on a random door. (K)\n"
                          "Or follow the main road. (R)").lower()

    if knock_or_road == "k":
        printi("You knock on a random door. Character answers.")
        printi("She looks at you with curiosity")
        printi("What do you do?")
        villager_talk = input("Talk about mystic crystals. (C)\n"
                              "Or ask for water. (W)\n ").lower()
        villager_answer(villager_talk)

    elif knock_or_road != "k" and knock_or_road != "r":
        printi("A black cat approaches, meows at you, and leaves") # Random
        Naranya_knock_road()

    else:
        follow_road()



def villager_answer(villager_talk):
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
        
    follow_road()


def follow_road():
    printi("You follow the road to the main plaza.")
    printi("A young man is reading sitting by a tree nearby.")
    printi("There is a tall statue of a woman holding a small "
           "shiny object...")
    printi("It looks like a crystal.")
    plaza(progress)


def plaza(progress):
    printi("What would you like to do:")
    plaza_choice = input("Approach young man. (Y)\n"
                         "Or steal the shiny object. (S)\n").lower()

    if plaza_choice == "s":
        plaza_steal(progress)

    elif plaza_choice == "y":
        printi("You walk towards the young man. You notice he is writing "
               "some poetry.")
        plaza_talk(progress)
    
    else:
        printi("random") #add random


def plaza_steal(progress):
    printi("You start climbing the statue and realize that the shiny "
           "object is indeed a crystal.")
    printi("As you reach and grab the crystal, a guard sees you and "
           "alerts the town.")
    progress.append("Crystal")
    printi("You put the crystal in your bag and quickly climb down.")
    printi("You run into an alley to avoid being seen.")
    plaza_alley(progress)


def plaza_alley(progress):    
    if "Water" or "Kicked" in progress:
        printi("The villager is in front of you.")
        plaza_alley_villager()

    else:
        plaza_alley_death()


def plaza_alley_villager():
    alley = input("Do you run back to the plaza. (B)\n"
    "Or do you ask the villager for help. (H)\n").lower()

    if alley == "b":
        printi("You turn back and stop. The guards are getting close.")
        printi("There is an open window to your left.")
        printi("What would you like to do:")
        input("Fight the guards (F)\n"
        "Or enter the house through the window (W)\n")
        plaza_alley_death()

    elif alley == "h":
        plaza_alley_villager_help(progress)

    else:
        printi("The narrator gives you a threatening look")
        plaza_alley_villager()


def plaza_alley_death():

    printi("As you get ready to proceed, you have a cold feeling "
            "on your chest.")
    printi("An arrow pierced your heart. You feel the blood "
           "coming out of your body.")
    printi("You look up.")
    printi("The moon gets close to the sun as your life gets " 
           "eclipsed by the darkness.")
    #game over


def plaza_alley_villager_help(progress):
    if "Water" in progress:
        printi("The villager recognizes you and grabs your hand.")
        printi("She guides you through the alleys and takes you "
               "to the city wall.")
        printi("There is a tall tree that you can climb "
               "to escape.")
    else:
        printi("The villager starts yelling and tackles you.")
        printi("The guards arrive. You get arrested.")
        # game over


def plaza_talk(progress):
    young_man_talk = input("Do you ask him about the crystal? (C)\n"
                           "Or do you ask him about " 
                           "his writings (W)\n").lower()

    if young_man_talk == "c":
        printi("'The crystal? Watch out stranger, don't let anybody "
               "hear you mentioning it.")
        printi("It contains all the powers of this town.")
        printi("It is said that the statue is cursed so it feels "
               "the power of the crystal on her hands.")
        printi("I say the statue can only sense some weight, "
               " and that the cystal could be easily replaced "
               "with a small object... like that rock!'")
        printi("'That's just me saying, anyways.'")
        progress.append("Rock")
        printi("The young man grabs his belongings and walk towards "
               "the main road.")
        plaza_steal(progress)
        
    elif young_man_talk == "w":
        printi("'Time")
        printi("   the space of a thousand")
        printi("Circles")
        printi("   transitioning one by one\n")
        printi("To eternally run")
        printi("   away")
        printi("From successive chains")
        printi("To return")
        printi("Time'\n")
        printi("'What brings you to this town, stranger?'")
        plaza_talk_intention(progress)


def plaza_talk_intention(progress):
    your_intention = input("Reveal your intentions about the "
                           "crystal (C)\n"
                           "Or you are just another wanderer "
                           "(W)\n").lower()
    if your_intention == "c":
        printi("'Oh noble stranger, let me help you in your quest.")
        printi("For years I have observed this plaza.")
        printi("I know how to avoid the spell!")
        printi("Stay here, I will take the crystal and end all "
               "the magical nonsense that torments this town.'\n")
        printi("The young man grabbed a rock and climbed the statue.")
        printi("He quickly swapped the crystal with the rock and "
               "puts it in his bag...")
        printi("But three guards spot him, one of them alarms "
               "the town while the other two capture the young man.")
        printi("His bag falls to the ground while he struggles to "
               "escape.")
        plaza_talk_intention_bag(progress)

    elif your_intention == "w":
        printi("'I will give you some good advice:'")
        printi("'Advice'") # Add advice
        printi("The young man grabs his belongings and walk towards "
               "the main road.")
        printi("You hear the voice of the crystal calling you.")
        plaza_steal(progress)


def plaza_talk_intention_bag(progress):
    take_or_leave = input("Do you take the bag and run? (T)\n"
                          "Or do you help the young man? "
                          "(H)\n").lower()
    
    if take_or_leave == "t":
        printi("You take the bag and find a way out of the town.")
        progress.append("Bag")

    elif take_or_leave == "h":
        printi("You push one of the guards, and the young man "
               "manages to escape.")
        printi("You try to follow him but some guards appear "
               "from an alley and capture you.\n")
        printi("In the prison, you keep grumbling about your "
               "decisions when you hear a murmur.")
        printi("The young man came to rescue you, and he "
               "managed to steal the keys of your cell.")
        printi("You escape the prison and leave the town "
               "without being spotted.")
        progress.append("Crystal")


def Celadon():
    printi("You are back at Celadon's tent")
    if "Valiant" in progress:
        crystal_valiant = input("'Valiant Explorer! Do you come back to "
                               "offer the crystal to your master?'"
                               "(Y)/(N)").lower()
        if crystal_master == "y":
            if "Bag" in progress:
                #Traitor
           #else:
                #Mission accomplished
        #elif crystal_master == "n":
                printi("'Hurry up! There is no time to waste!")
        #else:
            #random
    if "Coward" in progress:
        printi("'Coward! How dare you come to mighty Celadon's tent?'")
        printi("Celadon threatens you with a sword")
        crystal_coward = input("Do you give Celadon the crystal? (C)"
                               "Or do you run away? (R)").lower()
        if crystal_coward == "c":
            printi("Celadon cannot believe it! You are not a coward "
                   "after all")
            #Mission accomplished
        #elif crystal_coward == "r":
            #printi("You attempt to run away but the rug where you stand "
                   #"becomes a hollow surface.")
            #printi("You fall in a never ending dark and cold tunnel until "
                   #"your body vanishes".)
        
            #randomelse
plaza_talk_intention_bag(progress)
