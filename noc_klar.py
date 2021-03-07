import random
import time
# Color handling reference
# https://stackoverflow.com/questions/12492810/python-how-can-i-make-the-ansi-escape-codes-to-work-also-in-windows
import os
os.system("")

COLOR = {
    "MAGENTA": "\033[95m",
    "ENDC": "\033[97m",
    "BLUE": "\033[94m",
    "RED": "\033[91m",
    "GREEN": "\033[92m",
}

items = []
noise = []
bleeding = []

def startGame():
    print("""
    
███╗░░██╗██╗░██████╗░██╗░░██╗████████╗  ░█████╗░███╗░░██╗  ░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░██╗░██████╗
████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝  ██╔══██╗████╗░██║  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░██║██╔════╝
██╔██╗██║██║██║░░██╗░███████║░░░██║░░░  ██║░░██║██╔██╗██║  ██║░░╚═╝███████║██╔████╔██║██████╔╝██║░░░██║╚█████╗░
██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░  ██║░░██║██║╚████║  ██║░░██╗██╔══██║██║╚██╔╝██║██╔═══╝░██║░░░██║░╚═══██╗
██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░  ╚█████╔╝██║░╚███║  ╚█████╔╝██║░░██║██║░╚═╝░██║██║░░░░░╚██████╔╝██████╔╝
╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░░╚══╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░░╚═════╝░╚═════╝░""")
# Header reference
# https://fsymbols.com/text-art/
    print("\n\"Progress through the game by typing your commands in the console.\"")
    print("\n[START GAME]")

    choice = userChoice(["START GAME", "start game", "Start game"])

    if choice == "start game":

        sleep_function("\nYou wake up gasping as if you\'ve had the most terrible of dreams." 
                + "\nOnly you didn\'t."
                + "\nOr atleast you don\'t have any recollection of it. You\'re surprised not to find yourself in the comfort of your own bed."
                + "\nInstead you\'re sitting infront of a screensaver, the only thing shedding a light in the schools computer lab."
                + "\nYou\'ve been feeling particularly tired these last few days...\n")
        sleep_function_quote("\n\"I should probably make my way home\"\n")

        time.perf_counter()
        
        firstChoice()

def secretEnding():
    sleep_function("\nWhile playing with Charlie you, completely forget the situation that you\'re in."
        + "\nYou play with him throughout the night and as the day breaks you hear a voices and trucks rolling up outside."
        + "\n\"Citizens! Do not be alarmed! The surrounding area has been cleared! A rescue team is comming in!\"\n")
    sleep_function("\nCongratulations! You found the secret ending!´\n"
        + "\nWith your new found friend you feel ready to tackle the dystopian future of a zombie outbreak!\n")
    gameOver()

def sleep_function(string):
    for i in (string):
        time.sleep(0.045)
        # Color handling reference: https://stackoverflow.com/questions/12492810/python-how-can-i-make-the-ansi-escape-codes-to-work-also-in-windows
        print(COLOR["MAGENTA"] + i + COLOR["ENDC"], end="", flush = True) 
        
def sleep_function_quote(string):
    for i in (string):
        time.sleep(0.045)
        # Color handling reference: https://stackoverflow.com/questions/12492810/python-how-can-i-make-the-ansi-escape-codes-to-work-also-in-windows
        print(COLOR["BLUE"] + i + COLOR["ENDC"], end="", flush = True)

def userChoice(listaval):
    while True:
        userInput = input("\n: ")
        userInput = userInput.lower()
        if userInput in listaval:
            return userInput
        else:
            print("Invalid input")

def tryPassword():
    while True:        
        print("\nUSER: Admin")
        PCpassword = input("PASSWORD: ")
        if PCpassword == "password":
            return True
        else:
            print(COLOR["RED"] + "\nACCESS DENIED\n" + COLOR["ENDC"], end="", flush = True)
            sleep_function_quote("\n\"Hmm... worth a try. I really doubt the security is that tight.\"\n")
            print("\n[Try again]")
            print("\n[Go back]")
            
            choice = userChoice(["Try again", "try again", "Go back", "go back"])

            if choice == "Try again" or choice == "try again":
                temp = tryPassword()
                if temp == True:
                    return True
            else:
                firstChoice()
                return False

def gameOver():

    tid = time.perf_counter()
    minut = (tid / 60)
    p = int(minut)

    sek = ((minut - p) * 60)
    
    print(COLOR["GREEN"] + "\nThanks for playing!\n" + COLOR["ENDC"], end="", flush = True)

    print("This run took you " + str(p) + " minutes and ", end= '')
    print(str("%.2f" % sek) + " seconds!")

    print(COLOR["GREEN"] + "\nThere are 13 different outcomes of this game and one secret ending.\n" + COLOR["ENDC"], end="", flush = True)

    print("\n[Play again]")
    print("\n[Exit]")
    
    choice = userChoice(["play again", "exit"])

    if choice == "play again":
        items.clear()
        bleeding.clear()
        noise.clear()
        startGame()
    
    else:
        exit()

def flashlight():
    sleep_function("\nFumbling with your phone in all the panic you manage to get the flashlight on."
        + "\nA bright blue light illuminates the floor beneath your feet."
        + "\nBlood!"
        + "\nBloody prints, all over the floor, leading out towards the hallway."
        + "\nDisgusted and terrified by the sight of all the blood, you muster a bit of courage and realise you have to make it to the door.\n")
    if "Key" not in items:
        sleep_function("\nStaring down at the floor on your way, you find a key."
            + "\nThere\'s a piece of laminated paper on the key with \"password\" written on it.\n")
    print("\n[SCREAM]")
    print("\n[Go back and unlock door]")

    items.append("Flashlight")
    
    choice = userChoice(["scream", "go back and unlock door"])

    if choice == "scream":
        sleep_function("\nThe horrific sight of all the blood is too much. You let out a loud scream.\n")
        
        if (len(noise)) == 1:
            sleep_function("\nYou force your hand over your mouth as you hear footsteps approaching the door from the hallway."
                + "\nThe tiny bit of relief thinking they were friendly is abruptly interupted by the deafening sound of the door blasting open"
                + "\nSplinters fly across the room and you quickly dodge for cover under the desk"
                + "\nHow could you know anyone was there to hear you?"
                + "\nCurled up under the desk you can only blame yourself for not being more careful..."
                + "..."
                + "\nA drop of blood lands right infront of you"
                + "\nYou let out one last scream\n")
            gameOver()

        else:
            noise.append(1)
            sleep_function_quote("\n\"I have to get out of here\"\n")
            print("\n[Go back and open door]")
            
            choice = userChoice(["go back and open door"])

            if choice == "go back and open door":
                openDoor()
            
    else:
        openDoor()

def logOnPc():
    sleep_function_quote("\nComputers must\'ve rebooted while I was sleeping... Might aswell try a password.\n")
    accessGranted = tryPassword()

    if accessGranted == True:
        print(COLOR["GREEN"] + "\nACCESS GRANTED\n" + COLOR["ENDC"], end="", flush = True)
        sleep_function("\nYour eyes are met with the blinking of bold letters on the screen.")
        print(COLOR["RED"] + "\nPUBLIC ANNOUNCEMENT!\n" + COLOR["ENDC"], end="", flush = True)
        sleep_function("\nYou\'re to tired to take all the information in, but it\'s obvious something serious just happened.")
        sleep_function_quote("\n\"Virus... Explosive outbreak...\""
            + "\n\"How long have I been sleeping?\"")
        sleep_function("\nDo not go out under any circumstances."
            + "\nThe military is being deployed."
            + "\nYou can feel your heart pumping. This might have been a tiny bit exciting, had you not been all alone, locked in a dark room..."
            + "\nSymptoms include: Nausea, fattigue, vomiting, bleeding (nose and eyes)... aggression..."
            + "\nYou\'re franticly speeding through the text, when suddenly...\n")
        print(COLOR["RED"] + "\n*CRACK*\n" + COLOR["ENDC"], end="", flush = True)
        sleep_function("\nThe power cuts out. Complete darkness.\n")
        print("\n[SCREAM]")
        print("\n[Take out flashlight]")

        choice = userChoice(["scream", "take out flashlight"])

        if choice == "scream":
            
            if "Key" not in items:
                sleep_function("\nIn shock you let out a loud scream!."
                    + "\nIf anyone is still here, they might've heard you.\n")
                noise.append(1)
                print("\n[Take out flashlight]")
                print("\n[Go back to door]")

                choice = userChoice(["take out flashlight", "go back to door"])

                if choice == "take out flashlight":
                    flashlight()
                else:
                    tryMainDoor()
            
            elif "Key" in items:
                sleep_function("\nIn shock you let out a loud scream!."
                + "\nIf anyone is still here, they might've heard you.\n")

                noise.append(1)

                print("\n[Go back and unlock door]")
                print("\n[Take out flashlight]")

                choice = userChoice(["go back and unlock door", "take out flashlight"])

                if choice == "go back and unlock door":
                    openDoor()
                else:
                    flashlight()
            
            choice = userChoice(["take out flashlight", "go back to door"])
        
        else:
            flashlight()

def tryMainDoor():
    if "Key" in items:
        sleep_function_quote("\n\"I\'ve got the key now. I could open the door.\"\n")
        print("\n[Open the door] ")
        print("\n[Go back] ")

        choice = userChoice(["open the door", "go back"])

        if choice == "open the door":
            openDoor()
        
        else:
            firstChoice()
    else:
        sleep_function("\nIt\'s locked... There must be a way out.\n")
        print("\n[Go back]")
        print("\n[Look through window]")

        choice = userChoice(["go back", "look through window"])

        if choice == "go back":
            sleep_function("\nAs you turn away from the door you feel something scratch the floor underneath your shoe.\n")
            sleep_function_quote("\n\"The key!\"\n")
            sleep_function("\nThere\'s a piece of laminated paper with \"password\" written on it. You pick it up.\n")
            items.append("Key")
            print("\n[Go back to PC]")
            print("\n[Open the door]")

            choice = userChoice(["go back to pc", "open the door"])

            if choice == "go back to pc":
                logOnPc()
            else:
                openDoor()
        else:
            lookWindow()

def firstChoice():
    print("\n[Try main door]")
    print("\n[Log on computer]")

    choice = userChoice(["try main door", "log on computer"])

    if choice == "Try main door" or choice == "try main door":
        tryMainDoor()
    
    else:
        logOnPc()

def openDoor():
    sleep_function("\nYou step out into the dark hallway.")
    if "Flashlight" in items:
        sleep_function("\nThe only light source is your flashlight and you see only a few meters in front of you. ")
        sleep_function("\nHaving to rely on your other senses you realise you can hear something in both ends of the hallway." 
            + "\nTo the left, towards the exit is a sort of sloshing sound. As if someone was walking in mud up to their ankles."
            + "\nTo the right, towards the university clinic you hear a faint scratching.\n")
        print("\n[Go left]")
        print("\n[Go right]")

        choice = userChoice(["Go left", "go left", "Go right", "go right"])

        if choice == "Go left" or choice == "go left":
            goLeft()

        else:
            goRight()

    else:
        sleep_function("\nHaving to rely on your other senses you realise you can hear something in both ends of the hallway." 
            + "\nTo the left, towards the exit is a sort of sloshing sound. As if someone was walking in mud up to their ankles."
            + "\nTo the right, towards the university clinic you hear a faint scratching.\n")
        print("\n[Go left]")
        print("\n[Go right]")

        choice = userChoice(["Go left", "go left", "Go right", "go right"])

        if choice == "Go left" or choice == "go left":
            goLeft()
        
        else:
            goRight()

def lookWindow():
    sleep_function("\nYou see the dark, seemingly empty hallway."
        + "\nAt least you can\'t spot anything moving about."
        + "\nBut you do spot the handle on the other side of the door.\n")
    sleep_function_quote("\n\"I could probably reach the handle if I can\'t find another way.\"\n")
    print("\n[Go back]")
    print("\n[Smash window]")

    choice = userChoice(["Go back", "go back", "Smash window", "smash window"])

    if choice == "Go back" or choice == "go back":
        if "Key" not in items:
            sleep_function("\nAs you turn away from the door you feel something scratch the floor underneath your shoe.")
            sleep_function_quote("\n\"The key!\"")
            sleep_function("\nThere\'s a piece of laminated paper with \"password\" written on it. You pick it up.\n")
            items.append("Key")

            firstChoice()
        else:
            firstChoice()
    else:
        smashWindow()

def smashWindow():
    sleep_function("\nIn sheer panic you power your fist through the glass."
        + "\nIt makes a loud noise as the shards land on the hallway floor."
        + "\nA sharp piece of glass cuts deep into your arm, and the blood begins to flow. The pain is almost to much to bare."
        + "\nYou manage to reach the handle. You turn it and the door opens.\n")
    sleep_function_quote("\n\"No turning back now. I have to get out\"\n")
    noise.append(1)
    bleeding.append(1)
    print("\n[Walk out the door]")

    choice = userChoice(["Walk out the door", "walk out the door"])

    if choice == "Walk out the door" or choice == "walk out the door" and (len(noise)) != 2:
        openDoor()

    else:
        sleep_function("\nThe sounds of crashing glass or your screams might have gone unnoticed had you just been more careful."
            + "\nAs you step out into the hallway you find yourself to not be as lonely as you thought you were."
            + "\nThough now that you know what was hiding, listening to your carelessness."
            + "\nYou really wish you were alone.\n")
        gameOver()
                
def goLeft():
    sleep_function("\nYou turn towards the exit and start moving."
        + "\nA sense of hope fills you as you get closer to the exit, though still dreading what is making that awful sound."
        + "\nThirty meters from the exit is the cafeteria. You hear the sounds growing louder as you come closer."
        + "\nWith your new found hope and curiosity you peek inside to see whats making all that noise."
        + "\nMoonlight from the windows strikes precicely on the source of the sloshing."
        + "\nYou freeze."
        + "\nAs if the air inside you just vanished, you stare at the sight."
        + "\nA creature. Humanlike, but with skin of gray and blue, hairless and thin. Veins covering the body, pulsating as if they\'re just about to pop."
        + "\nCrouching over an unrecognizable body. It\'s fist is buried in the chest of whoever is laying there."
        + "\nSensing your pressense the thing looks up at you.\n")
    print("\n[SCREAM]")
    print("\n[RUN]")

    if "Charlie" in items:
        print("\n[Sacrifice Charlie]")
    
    choice = userChoice(["SCREAM", "scream", "Scream", "RUN", "run", "Run", "Sacrifice Charlie", "sacrifice charlie", "sacrifice Charlie"])

    if choice == "run":
        run()

    elif choice == "sacrifice charlie" and "Charlie" in items:
        sleep_function("\nYou push Charlie towards the thing to save yourself. But the beast doesn\'t want it."
            + "\nPossibly even the monster is disgusted by the choice you\'ve made."
            + "\nThe last thing you see is Charlie running for the exit as a fist breaks through your face.\n")
        gameOver()
    
    else:
        sleep_function("\nYou let out a scream that only a person knowing they are about to face death can make."
            + "\nThe thing pounces at you.\n")
        gameOver()


def goRight():
    sleep_function("\nSlowly and softly you creep closer to the scratching sounds."
        + "\nFearing the worst you peer around the corner and you\'re met with two eyes staring at you.\n")
    sleep_function_quote("\n\"Charlie!\"\n")
    sleep_function("\nIt\'s the school mascot, Charlie."
        + "\nThe six year old golden retriever, playing with something on the ground.\n")
    print("\n[Pet Charlie]")
    print("\n[Go back the other way]")

    choice = userChoice(["Pet charlie", "pet charlie", "Pet Charlie", "pet Charlie", "Go back the other way", "go back the other way"])

    if choice == "Pet charlie" or choice == "pet charlie" or choice == "Pet Charlie" or choice == "Pet Charlie":
        sleep_function("\nYou find incredible comfort in not being completely alone and you kneel down to stroke Charlie\'s back.\n")
        sleep_function_quote("\n\"What have you got there boy?\"\n")
        sleep_function("\nCharlie\'s been scratching away on a soft case emergency kit.\n")
        if (len(bleeding)) == 1:
            sleep_function("\nYou take the kit and patch yourself up."
                + "\nYou were lucky to find it in time.")
            bleeding.remove(1)
            playCharlie()
        else:
            sleep_function_quote("\n\"This kit could come in handy, might aswell bring it.\"")
            items.append("Kit")
            playCharlie()
    
    else:
        goLeft()

def playCharlie():
    sleep_function_quote("\n\"I should be going now, I\'m almost out of here\"\n")
    print("\n[Bring Charlie]")
    print("\n[Leave Charlie]")
    print("\n[Play with Charlie]")

    choice = userChoice(["Bring Charlie", "bring charlie", "bring Charlie", "Leave Charlie", "leave charlie", "leave Charlie", "Play with charlie", "play with charlie", "play with Charlie"])

    if choice == "Bring Charlie" or choice == "bring charlie" or choice == "bring Charlie":
        sleep_function_quote("\n\"I can\'t leave you here all alone boy.\"\n")
        sleep_function("\nYou look at Charlie and wave at him to follow you."
            + "\nYou tell yourself it\'s for his sake. But you really don\'t want to be alone."
            + "\nCharlie happily follows you.\n")
        items.append("Charlie")
        goLeft()
    elif choice == "Leave Charlie" or choice == "leave charlie" or choice == "leave Charlie":
        print("\nYou know Charlie will make it out of here on his own."
            + "\nYou watch him wiggle his tail as he strolls away from you, down towards the basement.\n")
        goLeft()
        
    else:
        i = 0
        while True:
            sleep_function("\nYou quietly play around a bit with charlie, he\'s really enjoying it."
                + "\nSo are you\n")
            print("\n[Keep playing]")
            print("\n[Stop playing]")

            choice = userChoice(["Keep playing", "keep playing", "Stop playing", "stop playing"])

            if i == 2:
                secretEnding()
                break

            if choice == "Keep playing" or choice == "keep playing":
                i = i + 1
                continue
            else:
                playCharlie()

def run():
    if (len(bleeding)) == 1:
        sleep_function("\nYou lost a lot of blood punching through the window."
            + "\nThe adrenalin only makes it pump out of you quicker."
            + "\nAlmost reaching the door your sight starts to fade and you fall to the ground." 
            + "\nYou can feel the thing breathing down your neck...\n")
        gameOver()

    elif (len(bleeding)) != 1 and "Kit" in items:
        sleep_function("\nYou\'re almost at the exit, but so is the thing.\n")
        print("\n[MacGyver a bomb using the kit]")
        print("\n[Run faster]")
        
        choice = userChoice(["macgyver a bomb using the kit", "run faster"])

        if choice == "macgyver a bomb using the kit":
            bomb()

        else:
            tripAndFall()
    
    else:
        tripAndFall()

def tripAndFall():
    
    rand = random.randint(0, 1)

    if rand == 1 and "Charlie" in items:

        fight = random.randint(0, 9)

        if fight == 0 or fight == 1 or fight == 2 or fight == 3 or fight == 4 or fight == 5 or fight == 6:
            sleep_function("\nA pool of blood right in front of you."
                + "\nSpeeding over it you loose your grip and fall face first on the ground."
                + "\nFearing the end Charlie attacks the thing giving you the opportunity to get out."
                + "\nYou have to leave him behind, but you're certain he'll make it on his own.\n")
            gameOver()
        
        else:
            sleep_function("\nA pool of blood right infront of you."
            + "\nSpeeding over it you loose your grip and fall face first on the ground."
            + "\nReaching for the door, the thing puts its blood soaked foot on your back... and stomps through you.\n")
            gameOver()
    
    elif rand == 1 and "Charlie" not in items:
        sleep_function("\nA pool of blood right infront of you."
            + "\nSpeeding over it you loose your grip and fall face first on the ground."
            + "\nReaching for the door, the thing puts its blood soaked foot on your back... and stomps through you.\n")
        gameOver()
    
    elif rand == 0 and "Charlie" in items:
        sleep_function("\nDespite your terrible physique, you manage to get to the door and slam it in the things face."
            + "\nYou watch it break its hands on the thick glass before returning to the dark hallway."
            + "\nYou turn to look at Charlie, but he\'s already gone."
            + "\nYou\'re alone again, but you\'re safe."
            + "\nFor now.\n")
        gameOver()
    
    else:
        sleep_function("\nDespite your terrible physique, you manage to get to the door and slam it in the things face."
            + "\nYou watch it break its hands on the thick glass before returning to the dark hallway."
            + "\nYou\'re alone again, but you\'re safe."
            + "\nFor now.\n")
        gameOver()

def bomb():

    rand = random.randint(0, 1)

    if rand == 1 and "Charlie" in items:
        sleep_function("\nAll those nights watching Richard Dean Anderson instead of studying pays off."
            + "\nSomehow you manage to construct a makeshift bomb and throw it at the thing."
            + "\nIt lights up and in a deafening screach it collapses on the floor.")
        sleep_function("\nYou and Charlie finally reach the door."
            + "\nThe cold air is refreshing and for a moment you forget what has just happend"
            + "\nYou turn to see the thing burning on the hallway floor."
            + "\nYou look at Charlie, he looks at you."
            + "\nYou smile and nod your head at him before the two of you make your way home"
            + "\nYou\'re safe."
            + "\nFor now.\n")
        gameOver()

    elif rand == 1 and "Charlie" not in items:
        sleep_function("\nAll those nights watching Richard Dean Anderson instead of studying pays off."
            + "\nSomehow manage to construct a makeshift bomb and throw it at the thing."
            + "\nIt lights up and in a deafening screach it collapses on the floor.")
        sleep_function("\nYou finally reach the door."
            + "\nThe cold air is refreshing and for a moment you forget what has just happend"
            + "\nYou turn to see the thing burning on the hallway floor."
            + "\nYou\'re safe."
            + "\nFor now.\n")
        gameOver()
    
    elif rand == 0 and "Charlie" in items:
        sleep_function("\nYou quickly empty some of the painkillers in a bottle of rubbing alcohol and throw it at the thing."
            + "\nObviously nothing happens and in the last seconds of your life you\'ve never felt more stupid.")
        print("\nAtleast you know Charlie will be safe, he runs past you and out the door.\n")
        gameOver()
    
    else:
        sleep_function("\nYou quickly empty some of the painkillers in a bottle of rubbing alcohol and throw it at the thing."
            + "\nObviously nothing happens and in the last seconds of your life you\'ve never felt more stupid.\n")
        gameOver()


##############################################################################################################################

startGame()