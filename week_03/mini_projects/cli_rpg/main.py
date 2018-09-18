from rpg import Hero, Opponent
import random
import time
from tqdm import tqdm



def main():
    print("Hi, Welcome to the game! \n")
    play_game()


def play_game():

    opponents = [
        Opponent("Messi", 99),
        Opponent("Ratikic", 94),
        Opponent("Pique", 89),
    ]

    hero = Hero("Caden", 95)

    while True:
        # end the game if all opponets are defeated
        if len(opponents) <= 0:
            print("you won the game!")
            exit()
        cmd = input("enter [a] for attack or [q] to quit:")

        while cmd not in ["a", "q"]:
            cmd = input("enter [a] for attack or [q] to quit:")

        if cmd == "q":
            print("bye!")
            exit()

        elif cmd == "a":
            opponent = random.choice(opponents)
            if hero.attack(opponent):
                opponents.remove(opponent)
                print("you win!")
            else:
                print("you lost!  You have to wait 5 sec")
                bar = ""
                for i in range(10):
                    bar = bar + "██████████"
                    print(bar, end="\r")
                    time.sleep(0.5)
                print("you are refreshed again")


if __name__ == '__main__':
    main()
