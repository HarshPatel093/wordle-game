import random

def load_words(filename="words.txt"):
    with open(filename, "r") as f:
        return [word.strip().lower() for word in f.readlines() if len(word.strip()) == 5]

def is_valid_guess(word, word_list):
    return len(word) == 5 and word in word_list

def display_result(guess, answer, correct_list, used_list):
    print("-------------")
    print(f"| {' '.join(guess)} |")
    print("| ", end="")

    correct = 0
    wrong_place = 0

    for i in range(5):
        if guess[i] == answer[i]:
            print("^", end=" ")
            correct += 1
            if guess[i] in used_list:
                used_list.remove(guess[i])
            if guess[i] not in correct_list:
                correct_list.append(guess[i])
        elif guess[i] in answer:
            print("*", end=" ")
            wrong_place += 1
            if guess[i] not in used_list and guess[i] not in correct_list:
                used_list.append(guess[i])
        else:
            print("-", end=" ")
            if guess[i] not in used_list:
                used_list.append(guess[i])

    print("|")
    print("|")
    print(f"| Correct spot (^): {correct}")
    print(f"| Wrong spot (*): {wrong_place}")
    print(f"| Correct letters: {', '.join(correct_list)}")
    print(f"| Used letters: {', '.join(used_list)}")
    print()

def play_wordle():
    word_list = load_words()
    answer = random.choice(word_list)

    print("\nWelcome to Wordle Clone!")
    print("Guess the 5-letter word in 6 tries.")
    print()

    correct_list = []
    used_list = []

    for attempt in range(1, 7):
        guess = input(f"Attempt {attempt}/6: ").strip().lower()

        while not is_valid_guess(guess, word_list):
            print("Invalid guess. Make sure it's a 5-letter word from the list.")
            guess = input(f"Attempt {attempt}/6: ").strip().lower()

        display_result(guess, answer, correct_list, used_list)

        if guess == answer:
            print(f"\n🎉 Solved in {attempt} tries! Well done!")
            return

    print(f"\nOut of attempts! The correct word was: {answer}")

if __name__ == "__main__":
    play_wordle()
