import random
import time

class TextTruthGame:
    def __init__(self):
        self.friends = []
        self.truth_questions = [
            "What's your biggest fear?",
            "What's the most embarrassing thing you've ever done?",
            "If you could have any superpower, what would it be and why?",
            "What's your biggest regret?",
            "If you could swap lives with anyone for a day, who would it be?",
            "What's the weirdest dream you've ever had?",
            "What's your most prized possession?",
            "If you could travel anywhere in the world, where would you go?",
            "What's the best piece of advice you've ever received?",
            "What's your most unusual talent?"
        ]

    def print_header(self):
        print("\n" + "=" * 50)
        print("🔮 Welcome to the Mystic Truth Revealer 🔮".center(50))
        print("=" * 50)

    def print_menu(self):
        print("\n📜 Main Menu 📜")
        print("1. ➕ Add a friend")
        print("2. ➖ Remove a friend")
        print("3. 🎭 Play a round of Truth")
        print("4. 👥 Show all friends")
        print("5. 🚪 Quit")

    def add_friend(self):
        name = input("\n👤 Enter friend's name (or press Enter to finish adding): ").strip()
        if name:
            self.friends.append(name)
            print(f"✅ {name} has joined the circle of truth!")
            return True
        return False

    def remove_friend(self):
        if not self.friends:
            print("\n❌ The circle is empty. There are no friends to remove.")
            return

        self.show_friends()
        while True:
            choice = input("\n🔢 Enter the number of the friend to remove (or press Enter to cancel): ").strip()
            if not choice:
                print("🔙 Returning to main menu...")
                return
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.friends):
                    removed_friend = self.friends.pop(index)
                    print(f"🚫 {removed_friend} has been removed from the circle of truth.")
                    return
                else:
                    print("❌ Invalid number. Please try again.")
            except ValueError:
                print("❌ Please enter a valid number.")

    def play_round(self):
        if not self.friends:
            print("\n❌ The circle is empty. Invite some friends first!")
            return

        print("\n🎲 The wheel of fate is spinning...")
        time.sleep(1)  # Add a slight delay for dramatic effect
        selected_friend = random.choice(self.friends)
        question = random.choice(self.truth_questions)

        print(f"\n🌟 {selected_friend}, the spirits have chosen you!")
        time.sleep(1)
        print(f"\n❓ Your truth question is: {question}")

        input("\nPress Enter when the truth has been revealed...")

    def show_friends(self):
        if self.friends:
            print("\n👥 Friends in the circle of truth:")
            for i, friend in enumerate(self.friends, 1):
                print(f"  {i}. {friend}")
        else:
            print("\n👥 The circle awaits its first truth-seeker.")

    def play_game(self):
        while True:
            self.print_header()
            self.print_menu()

            choice = input("\n🔢 Enter your choice (1-5): ")

            if choice == '1':
                while self.add_friend():
                    pass
            elif choice == '2':
                self.remove_friend()
            elif choice == '3':
                self.play_round()
            elif choice == '4':
                self.show_friends()
            elif choice == '5':
                print("\n🙏 Thank you for seeking the truth. Until we meet again!")
                break
            else:
                print("\n❌ Invalid choice. The spirits are confused. Try again.")

            input("\nPress Enter to continue...")

if __name__ == "__main__":
    game = TextTruthGame()
    game.play_game()