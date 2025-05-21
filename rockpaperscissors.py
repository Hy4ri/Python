import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (rock 👊🏻, paper 📄, scissors ✂️): ")

print(f"player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("🟰🟰🟰 You tie! 🟰🟰🟰")
elif player == "rock" and computer == "scissors":
    print("✅✅✅ You Won! ✅✅✅")
elif player == "scissors" and computer == "paper":
    print("✅✅✅ You Won! ✅✅✅")
elif player == "paper" and computer == "rock":
    print("✅✅✅ You Won! ✅✅✅")
elif player == "rock" and computer == "paper":
    print("❌❌❌ You lost! ❌❌❌")
elif player == "paper" and computer == "scissors":
    print("❌❌❌ You lost! ❌❌❌")
elif player == "scissors" and computer == "rock":
    print("❌❌❌ You lost! ❌❌❌")
else:
    print("Enter a valid choice!")
