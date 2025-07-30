import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def get_start_location():
    locations = ["Bywater", "The Old Forest", "Bree"]
    return random.choice(locations)


def enemy():
    enemies = ["an Orc", "a Troll", "Gollum"]
    return random.choice(enemies)


def intro():
    start_location = get_start_location()
    print_pause("You awaken beneath a twilight sky.")
    print_pause(f"You're in {start_location}.")
    print_pause("A man in gray robes and a tall"
                "pointed hat is watching you curiously.")
    print_pause("I am Gandalf the Grey.")
    print_pause("And you may be a fool of a different sort than I'm used to.")
    print_pause("But I sense...")
    print_pause("purpose in you.")
    print_pause("He offers his hand")
    print_pause("I'm on my way to meet someone in the Shire. Walk with me?")


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Don't be a fool and give a proper answer!")
    return response


def nowalk():
    enemies = enemy()
    response = valid_input("Choose what you will do next: "
                           "Do you take the left or the right path?\n",
                           "left", "right")
    if "left" in response:
        print_pause(f"You stumble upon {enemies}"
                    " and get devoured.")
    elif "right" in response:
        print_pause(f"You're being picked up by {enemies}"
                    " and find you way into his stomach.")
    print_pause("Either you go on an adventure or the adventure finds you.")


def checkornot():
    enemies = enemy()
    response = valid_input("Choose what you will do next: "
                           "Do you check out what it is? Yes or No. \n",
                           "yes", "no")
    if "yes" in response:
        print_pause(f"It's {enemies} looking for something precious...")
        print_pause("He has been looking for so long"
                    " that he's quite hungry...")
        print_pause("He attacks you and you get devoured.")
        restart_game()
    if "no" in response:
        print_pause("You reach Erebor - the final destination.")
        print_pause("Congratulations! You're one of the winners!")
        restart_game()


def yeswalk():
    response = valid_input("Choose what you will do next: "
                           "Do you join them? Yes or No. \n",
                           "yes", "no")
    if "yes" in response:
        print_pause("Thorin, son of Thrain, son of Thror"
                    " gives you a reassuring smile.")
        print_pause("With this encouragement the dwarves,"
                    " Bilbo, and you set out for Erebor")
        print_pause("You hear a weird whisper in the bushes...")
        checkornot()
    elif "no" in response:
        print_pause("Bilbo leaves his house under your"
                    "supervision while he's gone.")
        print_pause("End of your adventure...")


def get_response():
    response = valid_input("Choose what you will do next: "
                           "Do you accept his offer? Yes or No. \n",
                           "yes", "no")
    if "yes" in response:
        print_pause("The walk doesn't take long and"
                    " you're already in front Bilbo's house.")
        print_pause("There's a lot of sound coming out of the house")
        print_pause("Gandalf knocks the door...")
        print_pause("Bilbo Baggins, with an unamused"
                    " expression, lets you in.")
        print_pause("Dwarves are all around you.")
        print_pause("You learn that the dwarves and Bilbo"
                    " will set out on a journey.")
        yeswalk()
    elif "no" in response:
        print_pause("Gandalf shrugs: \"Then may the stars guide you\","
                    " he uses his wand and vanishes in smoke...")
        print_pause("You're left alone and start roaming around.")
        print_pause("There's diverting path ahead...")
        nowalk()
        restart_game()


def play_game():
    intro()
    get_response()


def restart_game():
    response = valid_input("Do you want to restart the game? Yes or No.\n",
                           "yes", "no")
    if "yes" in response:
        play_game()
    if "no" in response:
        print_pause("You have made your choice. Bye.")


play_game()
