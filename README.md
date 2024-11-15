# guessing-game
This is an interactive number guessing game built using Streamlit. The game provides two modes: User Guessing and Machine Guessing.

User Guessing Mode: The user tries to guess a number that the program has randomly selected within a specified range. After each guess, the program will give feedback (too high, too low, or correct) and will track how many attempts the user makes. It also calculates the optimal number of attempts based on the range and challenges the user to guess the number within that optimal range.

Machine Guessing Mode: In this mode, the user thinks of a number within a specified range, and the program attempts to guess it. The user provides feedback on whether the guess is too high, too low, or correct, and the program narrows down the range accordingly.

Features
Dynamic Range: Users can specify the minimum and maximum values for the number range.
Optimal Attempts: The program calculates the optimal number of attempts based on the given range using a binary search strategy.
Feedback System: Whether you're guessing or the machine is guessing, the program provides feedback to help you move closer to the correct answer.
Game Reset: You can reset the game at any time to start a fresh round.
Game Modes:
User Guessing: The user tries to guess the number.
Machine Guessing: The machine tries to guess the number.
