## Goal. Two sentences on what the game is and who plays it.
Tic-Tac-Toe game that runs in the terminal. It supports two players or one player against a computer opponent. This is an individual assignment. Write the plan, code, and tests yourself. Do not use AI tools for any part of it, including chat assistants and AI code completion

## Requirements

|ID|Requirements|How to verify it|
|---|-----|-----|
|1|Board is 3X3 and "X" starts first|pytest: initialize new board and check board size and turn|
|2|User can select two number between 1-3| pytest: check range input for `place_mark` function. Manual test of instruction|
|3|Print current board everytime| Manual testing|
|4|Can't place mark in taken cell| pytest: call `place_mark` with same parameter twice|
|5|horizontal, vertical, diagonal, anti-diagonal win condition | pytest: `has_won` with custom board setting|
|6|Human takes "X" and AI takes "O"| Manual testing |
|7|HardAI never lose if AI is "O" | pytest: check all possible cases recursively to see if it actually fails|

## Components. 
### board.py
board object that have functions for placing, removing, check won, display current board, return current empty cells, and check full.

### game.py
main game loop running each turn based on single/multi, easy/hard mode based on user choice from main.py

### main.py
starting file for get user preference about mode/difficulty choice.

### ai.py
After creating a base AI class, I Inheritance it to create EasyAI and HardAI. Although they both have a function named `choose_move`, each derived class performs a different role. EasyAI uses `random.choice()` to randomly select one of the remaining empty cells, while HardAI uses a custom `_minimax()` function to choose the optimal move.

## Decisions
I decided to create a `display` function directly in `board.py` to show the current board state. Since the `board` matrix itself is private, I judged that accessing it directly from outside would be inappropriate. Although I had previously pointed out that using `print` from outside `main.py` in the `public` directory was problematic, I received permission from Adam (the instructor) to create the function.

I decided to create a large loop to implement a feature that allows the game to be replayed.

## What changed
I moved the main loop to `game.py`. It was originally in `main.py`, but since `game.py` was listed in the “required files” and is responsible for turn management and overall game control, I left only the function calls and the mode and difficulty settings in `main.py`.
