def start_game():
    name = input("Type your name: ")
    print(f"Welcome {name} to this adventure!")

    invalid_option = "Not a valid option. Please try again. "

    while True:
        answer = input(
            "You are on a dirt road, it has come to an end and you can go 'left' or 'right'. Which way would you like to go? "
        ).lower()

        # Path 1. Left / Right
        if answer == "left":
            # Path 2a. Walk / Swim
            answer = input(
                "You come to a river, you can walk around it or swim across? Type 'walk' to walk around the river and 'swim' to swim across: "
            ).lower()
            # Walk Path
            if answer == "walk":
                print(
                    "You walk for many miles, ran out of water and you lost the game. YOU DIED!"
                )
                break
            # Swim Path
            elif answer == "swim":
                print("You swam across and were eaten by an alligator. YOU DIED!")
                break
            else:
                print(invalid_option)
                continue
        elif answer == "right":
            # Path 2b.
            answer = input(
                "You come to a bridge, it looks wobbly, do you want to cross it or head back? (Cross/Back)? "
            ).lower()
            # Cross Path
            if answer == "cross":
                answer = input(
                    "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? "
                )
                if answer == "yes":
                    print(
                        "You talk to the stranger and suddenly they stab you in the stomach repeatedly. YOU DIED!"
                    )
                    break
                elif answer == "no":
                    print(
                        "You walk past them and suddenly you felt a sharp object in your back. YOU DIED!"
                    )
                    break
                else:
                    print(invalid_option)
                    continue
            # Back Path
            elif answer == "back":
                print("You go back to the main road.")
                continue  # Go back to the start of the decision-making process
            else:
                print(invalid_option)
                continue
        else:
            print(invalid_option)
            continue  # Re-prompt the user for a valid answer


start_game()
