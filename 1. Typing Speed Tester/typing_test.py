import time

def typing_test():
    sentence = "The quick brown fox jumps over the lazy dog."
    
    print("\n" + "="*60)
    print("Type the following sentence as fast as you can:\n")
    print(f"\"{sentence}\"\n")
    print("="*60)
    
    input("Press Enter when you are ready to start...\n")

    start_time = time.time()
    user_input = input("Start typing here: ")
    end_time = time.time()

    time_taken = end_time - start_time

    word_count = len(user_input.split())
    wpm = (word_count / time_taken) * 60

    sentence_words = sentence.split()
    correct_words = 0
    user_words = user_input.split()
    
    for i in range(min(len(user_words), len(sentence_words))):
        if user_words[i] == sentence_words[i]:
            correct_words += 1

    accuracy = (correct_words / len(sentence_words)) * 100

    print("\n" + "="*60)
    print("Typing Test Results")
    print("-"*60)
    print(f"Time taken       : {time_taken:.2f} seconds")
    print(f"Typing speed     : {wpm:.2f} words per minute")
    print(f"Accuracy         : {accuracy:.2f}%")
    print("="*60 + "\n")

def main():
    while True:
        print("="*60)
        print("Typing Speed Tester")
        print("1. Start Typing Test")
        print("2. Exit")
        print("="*60)
        choice = input("Enter your choice: ")

        if choice == '1':
            typing_test()
        elif choice == '2':
            print("Exiting... Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
