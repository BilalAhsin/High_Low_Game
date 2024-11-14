
# Higher or Lower Number Guessing Game

## Description
Welcome to the **Higher or Lower Number Guessing Game**! This is a simple guessing game where a player has to guess if their randomly generated number is higher or lower than the computer's number.

## How to Play
1. When the game starts, you will be prompted to enter your name.
2. For each round, a random number between 1 and 100 is assigned to both you and the computer.
3. You have to guess whether your number is **higher** or **lower** than the computer’s number.
4. After each guess, the computer’s number is revealed, and you win or lose points based on your guess.
5. The game continues for 3 rounds, and your score is displayed after each round.

## Installation
To play the game:
1. Make sure you have Python installed on your computer.
2. Clone this repository to your local machine:
    ```bash
    git clone <repository-url>
    ```
3. Run the game script:
    ```bash
    python game.py
    ```

## Example Gameplay
```
Enter your name: Alice

Welcome!
Description:
You have to guess if your number is higher or lower than the computer's number.

Round 1
Your number: 45
Do you think your number is 'higher' or 'lower' than the computer's number?: higher
Computer's number: 23
You win this round! Your guess was correct.
Alice's current score: 1
```

## Project Structure
- **`Player`**: Represents a player with a name and a score.
- **`Game`**: Handles game rounds, scoring, and provides instructions and feedback on the player's guesses.

## Technologies Used
- Python (with `random` module for generating random numbers)

## Future Enhancements
- Add more rounds or allow the player to choose the number of rounds.
- Display a final result at the end, with feedback based on the player’s score.
- Provide additional options or difficulty levels.

## License
This project is licensed under the MIT License.

