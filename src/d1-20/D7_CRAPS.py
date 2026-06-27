from random import randint


def make_bet(balance: int) -> int:
    try:
        bet: int = int(input("Please enter your bet: "))
    except ValueError as e:
        print(f"Error: {e}")
    if bet > balance:
        print(
            f"You only have ${balance}. Your bet has been changed to ${balance} automatically."
        )
        return balance
    else:
        return bet


balance: int = 1000
while balance > 0:
    bet: int = make_bet(balance)
    dices: int = randint(1, 6) + randint(1, 6)
    print(f"You rolled a {dices}.")
    if dices == 7 or dices == 11:
        print(f"You won ${bet}.")
        balance += bet
        continue
    elif dices == 2 or dices == 3 or dices == 12:
        print(f"You lost ${bet}.")
        balance -= bet
        continue
    else:
        first_dices = dices

    while True:
        bet: int = make_bet(balance)
        dices: int = randint(1, 6) + randint(1, 6)
        print(f"You rolled a {dices}.")
        if dices == first_dices:
            print(f"You won ${bet}.")
            balance += bet
        elif dices == 7:
            print(f"You lost ${bet}.")
            balance -= bet
        else:
            print("Tie! Game continues.")
            continue
        break

print("You bankrupted! Game over.")
