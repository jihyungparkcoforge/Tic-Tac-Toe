# Tic-Tac-Toe

Tic-Tac-Toe game that runs in the terminal. It supports two players or one player against a computer opponent. This is an individual assignment. Write the plan, code, and tests yourself. Do not use AI tools for any part of it, including chat assistants and AI code completion


## Quick Start

```sh
git clone https://github.com/jihyungparkcoforge/Tic-Tac-Toe.git
cd Tic-Tac-Toe
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## Run tests

With the virtual environment activated, run:

```sh
python -m pytest
```

## Description

1. The board is 3x3. X always goes first.
2. Players enter a move as a row and a column, numbered from 1, such as 2 3.
3. The board is printed after every move.
4. A move to a taken cell, a cell off the board, or non-numeric input shows a message and lets the player try again. It does not use up the turn.
5. The game detects a win (across, down, or diagonal) and a draw.
6. At the start, the player chooses two players or versus computer. In versus computer mode, the human plays X and the computer plays O, and the player picks Easy or Hard.
7. Easy picks a random empty cell. Hard uses the minimax algorithm and never loses when it plays second.

## Test cases for main output (print)


|#|What I tested | What I did | Expected result | Actual result | Pass? |
|---|---|---|---|---|---|
|1|Invalid player mode choice (invalid number)| Enter 3 | Shows "Invalid input." and ask again | Invalid input. Do you want to play single mode? | Yes |
|2|Invalid player mode choive (invalid character)|Enter "Yes"| Shows "Invalid input." and ask again | Invalid input. Do you want to play single mode? | Yes |
