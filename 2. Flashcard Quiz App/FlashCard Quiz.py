import csv
import os
import random

FILE_NAME = "flashcards.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Answer"])

def add_flashcard():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([question, answer])

    print("Flashcard added successfully!\n")

def take_quiz():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        flashcards = list(reader)

    if not flashcards:
        print("No flashcards found. Add some first.\n")
        return

    random.shuffle(flashcards)
    score = 0

    for q, a in flashcards:
        user_answer = input(f"Question: {q}\nYour answer: ")
        if user_answer.strip().lower() == a.strip().lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {a}\n")

    print(f"Quiz finished! Your score: {score}/{len(flashcards)}\n")

def main():
    while True:
        print("Flashcard Quiz App")
        print("1. Add Flashcard")
        print("2. Take Quiz")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_flashcard()
        elif choice == '2':
            take_quiz()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()