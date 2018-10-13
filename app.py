# Below, I've created a game using statements to practice logic in Python.
# Currently in build1

def main():
    game()
    while True:
        restart = input("Try again?").lower()
        if restart == "yes":
            main()
        else:
            exit()


def game():
    print("Please choose a character (enter a number):\n")
    character_name = float(input("1. Mike\n2. Gary\n3. Mohammed\n"))
    if character_name == 1:
        character_name = "Mike"
    bio = "that was a very good choice"
    print("You've chosen", + character_name, bio)
    if character_name == 2:
        character_name = "Gary"
    bio = "That was a very bad choice "
    print("You've chosen", + character_name, bio)
    if character_name == 3:
        character_name = "Mohammed"
    bio = " he happens to be the developer for your journey...\nthis could either be a good choice or a bad one" \
          "\n\n(i just started learning how to code python so BE CAREFUL)\n? "
    print("You've chosen", + character_name, bio)


game()
main()
