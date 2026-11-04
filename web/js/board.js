// Port of board.py. The grid is private (#board) so it can only be changed
// through the methods below, same as the Python version.

export const MARKS = ["X", "O"];
const EMPTY = " ";

// Every line of three that wins the game: 3 rows, 3 columns, 2 diagonals.
const LINES = [
  [[0, 0], [0, 1], [0, 2]],
  [[1, 0], [1, 1], [1, 2]],
  [[2, 0], [2, 1], [2, 2]],
  [[0, 0], [1, 0], [2, 0]],
  [[0, 1], [1, 1], [2, 1]],
  [[0, 2], [1, 2], [2, 2]],
  [[0, 0], [1, 1], [2, 2]],
  [[0, 2], [1, 1], [2, 0]],
];

export class Board {
  #board;

  constructor() {
    this.#board = Array.from({ length: 3 }, () => Array(3).fill(EMPTY));
  }

  /** Places mark at (row, col). Returns false if the cell is invalid, taken, or the mark is invalid. */
  placeMark(row, col, mark) {
    if (![0, 1, 2].includes(row) || ![0, 1, 2].includes(col)) return false;
    if (this.#board[row][col] !== EMPTY) return false;
    if (!MARKS.includes(mark)) return false;
    this.#board[row][col] = mark;
    return true;
  }

  /** Clears (row, col) if it holds a mark. Does nothing for empty or invalid cells. */
  removeMark(row, col) {
    if (MARKS.includes(this.#board[row]?.[col])) {
      this.#board[row][col] = EMPTY;
    }
  }

  /** Returns a list of [row, col] pairs for every empty cell. */
  emptyCells() {
    const avail = [];
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        if (this.#board[i][j] === EMPTY) avail.push([i, j]);
      }
    }
    return avail;
  }

  /** Returns the three winning [row, col] pairs for mark, or null if mark has not won. */
  winningLine(mark) {
    return LINES.find((line) => line.every(([r, c]) => this.#board[r][c] === mark)) ?? null;
  }

  hasWon(mark) {
    return this.winningLine(mark) !== null;
  }

  isFull() {
    return this.emptyCells().length === 0;
  }

  /** Returns a copy of the grid so callers can read it without changing it. */
  snapshot() {
    return this.#board.map((row) => [...row]);
  }
}
