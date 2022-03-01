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


def valiant_question():
    valiant_explorer = input("'Are you the Valiant Explorer of the Soul?'"
                             " (Y, N)").lower()

    if valiant_explorer == "y":
        printi("'Indeed! There is no time to waste...")
        printi("Find the three crystals before midnight!'\n")
        printi("You walk out of the tent and look at the bright blue sky.")
        progress.append("Valiant")

    elif valiant_explorer == "n":    
        printi("'Coward! Leave this tent and never come back!'\n")
        printi("You run out of the tent and look at the bright blue sky.")
        progress.append("Coward")

    else:
        printi("'Do not run away from your destiny!'\n")
        valiant_question()
