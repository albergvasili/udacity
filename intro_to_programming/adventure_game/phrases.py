"""Phrases lists to randomize characters answers."""
import random
import time


def wronganswer():
    """Choose random phrase for wrong input."""
    random_else = ["A black cat approaches, meows at you, and leaves.",
                   "A fly buzzes in your ear.",
                   "You feel a bird poop landing on your shoulder.",
                   "A rude kid throws a rotten egg at you and "
                   "runs away.", "The narrator gives you a threatening look.",
                   "You hear Celadon's voice in your head: 'Don't run away "
                   "from your destiny!'"]
    random_else = random.choice(random_else)
    print(random_else + "\n")


def advice():
    """Random words for character advices."""
    words = ["time", "heart", "desires", "goals", "fears", "enemies",
             "pets", "wisdom", "crystals", "master", "insanity", "words",
             "temper", "feelings", "decisions", "dexterity", "destiny",
             "passion", "neighbors", "hunger", "complexity", "shoes"]
    word1 = random.choice(words)
    word2 = random.choice(words)
    print(f"'Don't let your {word1} control your {word2}.'\n")
    time.sleep(2)
