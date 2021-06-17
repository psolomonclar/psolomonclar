from random import randint

for x in range(10):
    value = randint(1, 10)

restart_game = True
def start():
    answer = input("""I'm thinking of a number between 1 and 10. You will get three attempts.
    With each wrong guess, you will receive a hint and your score will be reduced by one point.\n>>>""")

    if int(answer) == value:
        print("Correct! Impressive.")
        endgame = input("New game? (Y/N)\n>>>")
        if endgame == "Y":
            restart_game = True
        #Fix this (also occurs lines 27, 36, and 43):
        else:
            print("Goodbye!") ; restart_game = False
    else:
        print(f"Wrong. You have two attempts remaining. \nHint: This number times itself equals {value **2}")
        answer2 = input(">>>")
        if int(answer2) == value:
            print("You're correct!")
            endgame = input("New game? (Y/N)\n>>>")
            if endgame == "Y":
                restart_game = True
            else:
                print("Goodbye!") ; restart_game = False
        else:
            answer3 = input(f"Wrong again. You get one more try...\nHint: Is this number smaller than five? {value < 5}")
            if int(answer3) == value:
                print("Correct!")
                endgame = input("New game? (Y/N)\n>>>")
                if endgame == "Y":
                    restart_game = True
                else:
                    print("Goodbye!") ; restart_game = False
            else:
                print("Tough luck pal. \nYour score: 0.")
                endgame = input("New game? (Y/N)\n>>>")
                if endgame == "Y":
                    restart_game = True
                else:
                    print("Goodbye!") ; restart_game = False
while restart_game:
    start()
