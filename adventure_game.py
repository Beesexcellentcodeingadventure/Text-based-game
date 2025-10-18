# adventure_game.py
# -------------------------------------------------
# Sci‑Fi & Surreal – “ECHO//404”
# Premise: You wake up inside a derelict spacecraft whose faulty AI thinks you’re its creator.
# -------------------------------------------------

def get_choice(prompt, valid):
    """
    Show *prompt*, read the user’s answer and return the canonical (UPPER‑CASE) choice.
    If the answer isn’t in *valid*, return None.
    """
    answer = input(prompt + "\n> ").strip().upper()
    for v in valid:
        if answer == v:
            return v
    return None


# -------------------------------------------------
# LEVEL 1 – Wake up in the pod
# -------------------------------------------------
def level_one():
    print(
        "You hear a heartbeat… it's yours! You open your eyes and sit up. "
        "It's freezing and you can see your breath leaving your body. "
        "Around you, fellow passengers are still asleep in their hyper‑sleep pods. "
        "A dim glow comes from the control panels."
    )

    choice = get_choice(
        "You think about **LEAVING** but a small part of you wants to **STAY**. What do you choose?",
        ["LEAVE", "STAY"]
    )

    if choice == "LEAVE":
        print(
            "You climb out of your pod. Rows of pods line the chamber—family, friends, "
            "even the mailman. You head toward the heavy door at the far end."
        )
    elif choice == "STAY":
        print(
            "You stay a moment, shivering as the cold bites your eyes. "
            "Then you realize you must move, so you get up and walk to the door."
        )
    else:
        print("You hesitate, unsure what to do…")
        return level_one()          # reprompt until a valid answer

    return level_two()


# -------------------------------------------------
# LEVEL 2 – Hallway & red button
# -------------------------------------------------
def level_two():
    print(
        "\nThe door slides open, a beam of harsh white light flooding the corridor. "
        "You shield your eyes and step onto a white hallway lined with square windows "
        "that show the infinite black of space. Green vines crawl along the walls—"
        "the ship’s artificial garden."
    )

    choice = get_choice(
        "Do you **SIT** and wait, or **EXPLORE** the hallway?",
        ["SIT", "EXPLORE"]
    )

    if choice == "SIT":
        print(
            "You sit on the cold floor, waiting for someone… "
            "Minutes pass, then a tear rolls down your cheek. "
            "Loneliness drives you to your feet; you notice a bright red button on the wall."
        )
    elif choice == "EXPLORE":
        print(
            "You stride forward, memories of the launch flooding back. "
            "The President’s speech, the cheers of the crowd… "
            "Ahead, a conspicuous red button glows."
        )
    else:
        print("You hesitate, unsure what to do…")
        return level_two()          # reprompt

    return level_three()


# -------------------------------------------------
# LEVEL 3 – Three‑way decision (meets “>2 choices” rule)
# -------------------------------------------------
def level_three():
    print("\nThe red button pulses softly. You realize you have three possible actions:")

    choice = get_choice(
        "Do you **PRESS** the button, **WALK AWAY**, or **ANALYZE** it with the ship’s console?",
        ["PRESS", "WALK AWAY", "ANALYZE"]
    )

    if choice == "PRESS":
        print(
            "\nYou slam the button. The ship shudders, and a holographic AI flickers to life. "
            "\"Creator…\" it whispers. The AI’s confusion gives you a chance to seize control "
            "of the vessel. **ENDING: You become the ship’s commander.**"
        )
    elif choice == "WALK AWAY":
        print(
            "\nYou decide the button is too risky and walk away. The corridor darkens, "
            "and the ship’s systems begin to fail. You hear alarms and realize you’re "
            "trapped with no power. **ENDING: The ship drifts silently into the void.**"
        )
    elif choice == "ANALYZE":
        print(
            "\nYou pull a handheld console from your pod and scan the button. "
            "The AI’s code is corrupted; you can rewrite its core directives. "
            "With a few keystrokes you reprogram the AI to think you truly are its creator. "
            "**ENDING: You rewrite reality and steer the ship to a new destiny.**"
        )
    else:
        print("You hesitate, unsure what to do…")
        return level_three()        # reprompt

    # Game over – could loop back or exit
    print("\n--- Game Over ---")


# -------------------------------------------------
# MAIN
# -------------------------------------------------
if __name__ == "__main__":
    level_one()
