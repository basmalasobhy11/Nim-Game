

def main():
    # set the sum
    sum = 0
    # the beginning
    print("Welcome to nim game")
    print("Your target is 100")

    # THE GAME
    while sum < 100:
        # add is the number which the players enter
        # To get exactly 100 and not more than it

        if sum >= 91:
            add = int(input(f"Player 1: please add a number from 1-{10-(sum % 10)}"))
            while add < 1 or add > 10-(sum % 10):
                add = int(input(f"Player 1: please add a number from 1-{10-(sum % 10)}"))
        else:
            add = int(input("Player 1: please add a number from 1-10"))
            while add < 1 or add > 10:
                add = int(input("Player 1: please add a number from 1-10"))

        sum += add
        print(f"Your sum is: {sum}")
        if sum == 100:
            print("Player 1 wins!")
            break

        if sum >= 91:
            add = int(input(f"Player 2: please add a number from 1-{10-(sum % 10)}"))
            while add < 1 or add > 10-(sum % 10):
                add = int(input(f"Player 2: please add a number from 1-{10-(sum % 10)}"))
        else:
            add = int(input("Player 2: please add a number from 1-10"))
            while add < 1 or add > 10:
                add = int(input("Player 2: please add a number from 1-10"))

        sum += add
        print(f"Your sum is: {sum}")
        if sum == 100:
            print("Player 2 wins! ")
            break


main()

