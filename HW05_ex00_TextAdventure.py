#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body

def name_replace(text):
    if text.find('You ') != -1:
        return print(text.replace('You',username))
    elif text.find('you ') != -1:
        return print(text.replace('you',username))
    elif text.find("you're") != -1:
        return print(text)
    elif text.find("your") != -1:
        return print(text)
    else:
        return print(text)


def infinite_stairway_room(count=0):
    name_replace("You walk through the door to see a dimly lit hallway.")
    name_replace("At the end of the hallway is a", count ,'long ', 'staircase going towards some light')
    next = input("> ")

    # infinite stairs option
    if next == "take stairs":
        name_replace('You take the stairs')
        if (count > 0):
            name_replace("but you're not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if count>5 and next == 'mercy':
        back_room()

    else:
        dead("You starve on the endless stairs.")


def gold_room():
    name_replace("This room is full of gold.  How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        name_replace("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy goose!")


def bear_room():
    name_replace("There is a bear here.")
    name_replace("The bear has a bunch of honey.")
    name_replace("The fat bear is in front of another door.")
    name_replace("How are you going to move the bear?")
    bear_moved = False

    #TODO: allow take or honey, open or door, and just taunt
    while True:
        next = input("> ")

        if bear_moved == True:
            if next.find("taunt") != -1 or next.find("bear") != -1:
                dead("The bear gets pissed off and chews your leg off.")

            elif next.find("open") != -1 or next.find("door") != -1:
                gold_room()

            else:
                name_replace("I got no idea what that means.")
        else:

            if next.find('take') != -1 or next.find('honey') != -1:
                dead("The bear looks at you then slaps your face off.")

            elif next.find("taunt") != -1 or next.find("bear") != -1 :
                name_replace("The bear has moved from the door. You can go through it now.")
                bear_moved = True

            else:
                name_replace("I got no idea what that means.")


def cthulhu_room():
    name_replace("Here you see the great evil Cthulhu.")
    name_replace("He, it, whatever stares at you and you go insane.")
    name_replace("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        infinite_stairway_room()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def back_room():
    name_replace("You stumble into a dark room filled people huddled around computers.")
    name_replace("The sound of typing on keyboards slowly recedes. They stare at you.")
    name_replace("You aren't sure what to do in the silence, so you decide to announce yourself.")
    name_replace("You say:")
    next = input("> ")
    name_replace("The crowd says all at once'", next ,"'and then returns to typing.")
    name_replace("You sit in a free chair and begin programming, forever.")
    exit(0)

def dead(why):
    name_replace("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    name_replace("Please enter your name.")
    global username
    username = input("> ")

    name_replace("You are in a dark room.")
    name_replace("There is a door to your right and left.")
    name_replace("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
