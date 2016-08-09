#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body

def name_replace(text):
    return print(text.replace('You' or 'you',username))

def infinite_stairway_room(count=0):
    print("You walk through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count ,'long ', 'staircase going towards some light')
    next = input("> ")

    # infinite stairs option
    if next == "take stairs":
        print('You take the stairs')
        if (count > 0):
            print("but you're not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if count>5 and next == 'mercy':
        back_room()

    else:
        dead("You starve on the endless stairs.")


def gold_room():
    print("This room is full of gold.  How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy goose!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
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
                print("I got no idea what that means.")
        else:

            if next.find('take') != -1 or next.find('honey') != -1:
                dead("The bear looks at you then slaps your face off.")

            elif next.find("taunt") != -1 or next.find("bear") != -1 :
                print("The bear has moved from the door. You can go through it now.")
                bear_moved = True

            else:
                print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        infinite_stairway_room()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def back_room():
    print("You stumble into a dark room filled people huddled around computers.")
    print("The sound of typing on keyboards slowly recedes. They stare at you.")
    print("You aren't sure what to do in the silence, so you decide to announce yourself.")
    print("You say:")
    next = input("> ")
    print("The crowd says all at once'", next ,"'and then returns to typing.")
    print("You sit in a free chair and begin programming, forever.")
    exit(0)

def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print("Please enter your name.")
    global username
    username = input("> ")

    name_replace("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
