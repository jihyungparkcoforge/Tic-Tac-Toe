// Port of ai.py. Both AIs return an empty [row, col] and leave the board unchanged.
// `rng` is a function returning a float in [0, 1), injectable for deterministic tests
// (the JS counterpart of passing random.Random() in Python).

export const otherMark = (mark) => (mark === "X" ? "O" : "X");

class AI {
  constructor(rng = Math.random) {
    this.rng = rng;
  }

  chooseMove(_board, _mark) {
    throw new Error("chooseMove must be implemented by a subclass");
  }
}

export class EasyAI extends AI {
  chooseMove(board, _mark) {
    const cells = board.emptyCells();
    if (cells.length === 0) return null;
    return cells[Math.floor(this.rng() * cells.length)];
  }
}

export class HardAI extends AI {
  chooseMove(board, mark) {
    const [, move] = this.#minimax(board, mark, mark, 0);
    return move;
  }

  // Scores are from the AI's (`me`) point of view, so it works whether the AI plays X or O.
  // Subtracting depth makes the AI prefer quicker wins and slower losses.
  #minimax(board, me, player, depth) {
    if (board.hasWon(me)) return [10 - depth, null];
    if (board.hasWon(otherMark(me))) return [depth - 10, null];

    const moves = board.emptyCells();
    if (moves.length === 0) return [0, null];

    const maximizing = player === me;
    let bestScore = maximizing ? -Infinity : Infinity;
    let bestMove = null;

    for (const [row, col] of moves) {
      board.placeMark(row, col, player);
      let score;
      try {
        [score] = this.#minimax(board, me, otherMark(player), depth + 1);
      } finally {
        board.removeMark(row, col);
      }

      if (maximizing ? score > bestScore : score < bestScore) {
        bestScore = score;
        bestMove = [row, col];
      }
    }

    return [bestScore, bestMove];
  }
}
