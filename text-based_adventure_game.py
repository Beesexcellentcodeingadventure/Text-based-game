#Sci-Fi & Surreal
#ECHO//404
#Premise: You wake up inside a derelict spacecraft with a faulty AI that thinks you’re its creator.
#Goal: Repair the ship—or use the AI’s confusion to rewrite your identity.
#Twist: The AI “remembers” choices you didn’t make.
# 3 Levels

#Level 1 
#Waking up after a mowfunkion in the system, you (player) were suppose to be in hyper sleep. There system rests itself your pod 
# mowfunkions during the reset. The AI co captin thinks you are the captin and stops flying the space ship. You (player) need to
# fix it. 

print("You hear a heart beat...It's yours! You open your eyes and sit up. It's freezing and you can see your breath leaving your" \
"body. You look around. You see your fellow passengers still a sleep in the their hyper sleep pods. It's dark but there is some " \
"illumination coming from the buttons on other hyper sleep pods.")

#First chose get up from the pod or stay. 
chose_1 = input("You think about LEAVING but a small part of you wants to STAY. What do you choose? ").strip().upper()

if chose_1 == "LEAVE" or chose_1 == "LEAVING":
    print("You get out of your pod. As you walk, you look at rows of pods—you see your family, friends, your mailman, and hundreds of others."
          " You question if this is all a dream. You continue walking until you reach the door.")
elif chose_1 == "STAY":
    print("You sit there, feeling how cold your eyeballs get when you blink. You shiver. You know you have to leave. So you leave and reach the door.")
else:
    print("You hesitate, unsure what to do...")

print("As you open the door beem of light blinds you. You walk through using your arm as a sheld to block the light." \
"Once your eyes have ajusted to the light you see a big white hallway with square benthes, windows that show the infafant of space, and the only " \
"color is green from the trees and hedges. You remember this place it's lobby where you boarded. You remeamber how happy everyone was to apart of this" \
"new experance. A small few who would get to experance space travel to the pulic. A space curse.")    
print("But what happened? Why are you awake? How long has it been. Your suppose to be asleep for 7 months unitl you get to mars." \
"Has it been 7 months? You look back at the door you came through. Maybe your the first one awake and everyone would be out any minute.")

chose_2 = input("Should you SIT and wait or should you EXPLORE? ").strip().upper()

if chose_2 == "SIT":
    print("You sit there... and sit there... waiting... no one is coming. A tear streams down your face. You're alone."
          " You decide to get up and explore. You find a red button.")
elif chose_2 == "EXPLORE":
    print("While exploring, memories flood back of being in this lobby—the smiles, laughter, and excitement."
          " The President of the United States was at the opening ceremony, giving a speech about how this was a historic moment."
          " He said people like you were lucky, and how he wished he could go with you. You find a red button.")
else:
    print("You hesitate, unsure what to do...")

print("Should you PRESS the button or WALK AWAY?")

#If they press the you meet AI and go to level 2 if they walk away they don't progress. 






