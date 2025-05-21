import random


def read_cards():
    try:
        with open("cards.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def ask_question(question, answer):
    user_input = input(f"{question}\n Answer: ")
    if user_input.lower() == answer.lower():
        return True
    else:
        print(f"The answer is {answer}")
        return False


def give_card(cards):
    random.shuffle(cards)
    score = 0
    for card in cards:
        question, answer = card.split("|", 1)
        if ask_question(question, answer):
            score += 1

    print(f"your score is {score}/{len(cards)}")


def main():
    while True:
        cards = read_cards()
        if not cards:
            break
        give_card(cards)
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
