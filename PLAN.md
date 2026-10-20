## Goal. Two sentences on what the game is and who plays it.
Tic-Tac-Toe game that runs in the terminal. It supports two players or one player against a computer opponent. This is an individual assignment. Write the plan, code, and tests yourself. Do not use AI tools for any part of it, including chat assistants and AI code completion

## Requirements
1. Game play both single play versus Easy/Hard AI or multiplayer mode.
2. Test file and connect with github Action for CI and passes all possible function inputs.
3. Hard AI never losses when it plays second
4. Re-ask user choice for both difficulty choice and multi/single player
5. Ask valid input when user ask outbounded input not within 1-3
6. Check won when it reach full board in same time without saying Draw and Won in same time.

## Components. 
### board.py
board object that have functions for placing, removing, check won, display current board, return current empty cells, and check full.

### game.py
main game loop running each turn based on single/multi, easy/hard mode based on user choice from main.py

### main.py
starting file for get user preference about mode/difficulty choice.
