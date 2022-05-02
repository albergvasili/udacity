"""Text based adventure game."""
import phrases
import time
import sys


def printi(text):
    """Create special print function with sleep time."""
    print(text)
    time.sleep(2)


def intro(progress):
    """Begin game."""
    printi("The mighty Celadon grabbed the old mysterious book.")
    printi("He deliberately opened a random page and read:")
    printi("'When the Moon covered the Sun, the Valiant Explorer "
           "of the Soul gathered the mystic crystal and presented "
           "it to his master before midnight.'\n")
    printi("Celadon stared at the infinite space in front of him.")
    printi("He suddendly closed the book and looked at you:\n")
    valiant_question(progress)


def valiant_question(progress):
    """Check answer to proceed."""
    valiant_explorer = input("'Are you the Valiant Explorer of the Soul?'"
                             " (Y)/(N)").lower()

    if valiant_explorer == "y":
        printi("'Indeed! There is no time to waste...")
        printi("Find the crystal before midnight!'\n")
        printi("You walk out of the tent and look at the bright blue sky.")
        progress.append("Valiant")
        path(progress)

    elif valiant_explorer == "n":
        printi("'Coward! Leave this tent and never come back!'\n")
        printi("You run out of the tent and look at the bright blue sky.")
        progress.append("Coward")
        path(progress)

    else:
        printi("'Do not run away from your destiny!'\n")
        valiant_question(progress)


def path(progress):
    """Check items to choose next step."""
    if "Bag" in progress:
        printi("You feel an ominous spirit surrounding Celadon's dark "
               "and massive tent.\n")
        Celadon(progress)

    if "Crystal" in progress:
        printi("Celadon's massive tent makes you feel relieved.\n")
        Celadon(progress)

    else:
        printi("The beautiful landscape of the Verdiul forest is divided "
               "by the path that leads to Naranya.\n")
        Naranya(progress)


def Naranya(progress):
    """Introduce the town of Naranya."""
    printi("You follow the long path to Naranya and enter through the gates.")
    printi("You are surrounded by small white houses with orange roofs "
           "on both sides of the main road.\n")
    Naranya_knock_road(progress)


def Naranya_knock_road(progress):
    """Check input to determine first decision in Naranya."""
    printi("What would you like to do:")
    knock_or_road = input("Knock on a random door. (K)\n"
                          "Or follow the main road. (R)\n").lower()

    if knock_or_road == "k":
        printi("You knock on a random door. An old woman answers.")
        printi("She looks at you with curiosity.")
        printi("What do you do?")
        villager_answer(progress)

    elif knock_or_road == "r":
        follow_road(progress)

    else:
        phrases.wronganswer()
        Naranya_knock_road(progress)


def villager_answer(progress):
    """Talk to villager in house by the road."""
    villager_talk = input("Talk about mystic crystals. (C)\n"
                          "Or ask for water. (W)\n").lower()

    if villager_talk == "c":
        printi("'CRYSTALS! Do NOT talk to me about Crystals!"
               " Are you insane!'\n")
        printi("She slams the door. The people around stare at you.\n")
        progress.append("Kicked")
        follow_road(progress)

    elif villager_talk == "w":
        printi("'Here is some water, poor wanderer.'")
        printi("'You must be coming from the dark forest of Verdiul...'")
        printi("'They say the dark wizard of oblivion lives there.'")
        phrases.advice()
        progress.append("Water")
        follow_road(progress)

    else:
        phrases.wronganswer()
        villager_answer(progress)


def follow_road(progress):
    """Follow the road towards the plaza."""
    printi("You follow the road to the main plaza.")
    printi("A young man is reading sitting by a tree nearby.")
    printi("There is a tall statue of a woman holding a small "
           "shiny object...")
    printi("It looks like a crystal.")
    plaza(progress)


def plaza(progress):
    """Make a decision in the plaza."""
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
        phrases.wronganswer()
        plaza(progress)


def plaza_steal(progress):
    """Steal the crystal."""
    printi("You start climbing the statue and realize that the shiny "
           "object is indeed a crystal.")
    printi("As you reach and grab the crystal, a guard sees you and "
           "alerts the town.")
    progress.append("Crystal")
    printi("You put the crystal in your bag and quickly climb down.")
    printi("You run into an alley to avoid being seen.")
    plaza_alley(progress)


def plaza_alley(progress):
    """Check progress list to choose events in the alley."""
    if "Water" in progress:
        printi("The friendly woman that gave you water is in front of you.")
        plaza_alley_villager(progress)

    if "Kicked" in progress:
        printi("The old woman is standing in the middle of the alley, "
               "hands on her hips. She is still mad at you.")
        plaza_alley_villager(progress)

    else:
        plaza_alley_death()


def plaza_alley_villager(progress):
    """Make decision in alley."""
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
        plaza_alley_villager(progress)


def plaza_alley_death():
    """Death in the alley."""
    printi("As you get ready to proceed, you have a cold feeling "
           "on your chest.")
    printi("An arrow pierced your heart. You feel the blood "
           "coming out of your body.")
    printi("You look up.")
    printi("The moon gets close to the sun as your life gets "
           "eclipsed by the darkness.")
    play_again()


def plaza_alley_villager_help(progress):
    """Check progress list when asking for help in the alley."""
    if "Water" in progress:
        printi("The villager recognizes you and grabs your hand.")
        printi("She guides you through the alleys and takes you "
               "to the city wall.")
        printi("There is a tall tree that you can climb "
               "to escape.")
        path(progress)

    else:
        printi("The villager starts yelling and tackles you.")
        printi("The guards arrive. You get arrested.")
        play_again()


def plaza_talk(progress):
    """Answers from young man by the plaza."""
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
        printi("'That's just me saying, anyways.'\n")
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
        printi("'What brings you to this town, stranger?'\n")
        plaza_talk_intention(progress)

    else:
        phrases.wronganswer()
        plaza_talk(progress)


def plaza_talk_intention(progress):
    """Conversation with the young man if answer from plaza_talk was "w"."""
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
        phrases.advice()
        printi("The young man grabs his belongings and walk towards "
               "the main road.")
        printi("You hear the voice of the crystal calling you.")
        plaza_steal(progress)

    else:
        phrases.wronganswer()
        plaza_talk_intention(progress)


def plaza_talk_intention_bag(progress):
    """Make decision about bag to proceed."""
    take_or_leave = input("Do you take the bag and run? (T)\n"
                          "Or do you help the young man? "
                          "(H)\n").lower()

    if take_or_leave == "t":
        printi("You take the bag and find a way out of the town.")
        progress.append("Bag")
        path(progress)

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
        path(progress)

    else:
        phrases.wronganswer()
        plaza.talk_intention_bag(progress)


def Celadon(progress):
    """Check progress list to determine Celadon's reaction."""
    printi("You go inside. Celadon is standing in front of you.")

    if "Valiant" in progress:
        Celadon_valiant(progress)

    if "Coward" in progress:
        Celadon_coward(progress)


def Celadon_valiant(progress):
    """Celadon's reaction to 'valiant' in progress list."""
    crystal_valiant = input("'Valiant Explorer! Do you come back to "
                            "offer the crystal to your master?'"
                            "(Y)/(N)\n").lower()

    if crystal_valiant == "y":
        bag_or_crystal(progress)

    elif crystal_valiant == "n":
        printi("'Hurry up! There is no time to waste!'\n")
        path(progress)

    else:
        phrases.wronganswer()
        Celadon_valiant(progress)


def Celadon_coward(progress):
    """Celadon's reaction to 'coward' in progress list."""
    printi("'Coward! How dare you come to mighty Celadon's tent?'\n")
    printi("Celadon threatens you with his staff")
    crystal_coward = input("Do you give Celadon the crystal? (C)\n"
                           "Or do you run away? (R)\n").lower()

    if crystal_coward == "c":
        bag_or_crystal(progress)

    elif crystal_coward == "r":
        run_away()

    else:
        phrases.wronganswer()
        Celadon_coward(progress)


def bag_or_crystal(progress):
    """Check progress to reveal bag's contents or proceed to victory."""
    if "Bag" in progress:
        printi("You proudly hand the bag to Celadon and start imagining "
               "your great reward, and many years of prosperity.")
        printi("Celadon grabs the crystal inside the bag and present it "
               "to you.")
        printi("But it's not a crystal! It's just a rock!")
        printi("The young man must have replaced it in the commotion.")
        printi("Celadon looks furious. He draws his sword to attack you")
        run_away()

    elif "Crystal" in progress:
        mission_accomplished()


def run_away():
    """Game over after bag's content is revealed."""
    printi("You attempt to run away but the rug where you stand "
           "becomes a hollow surface.")
    printi("You fall in a never ending dark and cold tunnel until "
           "your body vanishes.")
    play_again()


def mission_accomplished():
    """Victorious ending."""
    printi("You hand the crystal to your Master.")
    printi("'Wonderful! You really are a valiant explorer after all!'\n")
    printi("Congratulations! You won!")
    play_again()


def play_again():
    """Prompt user to play againi or exit."""
    restart = input("Would you like to play again? (Y)/(N)\n").lower()

    if restart == "y":
        play_game()

    elif restart == "n":
        sys.exit()

    else:
        play_again()


def play_game():
    """Start game with an empty progress list."""
    progress = []
    intro(progress)


if __name__ == '__main__':
    play_game()
