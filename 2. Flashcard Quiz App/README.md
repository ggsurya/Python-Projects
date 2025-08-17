# 🃏 Flashcard Quiz App in Python

A simple command-line Python program to create and take flashcard quizzes.

## Features

- Add new flashcards with a question and answer.
- Take a quiz with randomly shuffled flashcards.
- Receive instant feedback for each answer (correct/incorrect).
- Keep track of your score at the end of each quiz.
- Handles empty flashcard sets and invalid menu inputs gracefully.

## Usage

1. Clone the repository or download the source code file.
2. Run the program with Python 3. For example:
   ```bash
   python flashcard_quiz.py
3. Follow the on-screen menu to add flashcards or take a quiz.

## Example

```
Flashcard Quiz App
1. Add Flashcard
2. Take Quiz
3. Exit
Enter your choice: 1

Enter the question: What is the capital of France?
Enter the answer: Paris
Flashcard added successfully!

Flashcard Quiz App
1. Add Flashcard
2. Take Quiz
3. Exit
Enter your choice: 2

Question: What is the capital of France?
Your answer: Paris
Correct!

Quiz finished! Your score: 1/1
```

## How the Program Works

- Flashcards are stored in a CSV file (flashcards.csv).
- Each flashcard has a question and an answer.
- When taking a quiz, flashcards are randomly shuffled.
- User answers are compared (case-insensitive) to the stored answer.
- Score is displayed at the end of the quiz.
   
## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ggsurya/Python-Projects/blob/main/LICENSE) file for details.

## 📩 Contact

**G.G. Surya**  
📧 Email: ggsuryaff@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/g-g-surya-5aa9312b4)
🔗 [GitHub](https://github.com/ggsurya)
