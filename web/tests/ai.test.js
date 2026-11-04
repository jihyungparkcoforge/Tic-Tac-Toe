import { test } from "node:test";
import assert from "node:assert/strict";
import { Board } from "../js/board.js";
import { EasyAI, HardAI, otherMark } from "../js/ai.js";

// Small deterministic PRNG (mulberry32) so EasyAI tests are repeatable.
function seededRng(seed) {
  return () => {
    seed |= 0;
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

test("EasyAI always picks an empty cell and does not modify the board", () => {
  const ai = new EasyAI(seededRng(42));
  const board = new Board();
  board.placeMark(0, 0, "X");
  board.placeMark(1, 1, "O");
  board.placeMark(2, 2, "X");
  const before = board.snapshot();

  for (let i = 0; i < 50; i++) {
    const [r, c] = ai.chooseMove(board, "O");
    assert.equal(before[r][c], " ");
  }
  assert.deepEqual(board.snapshot(), before);
});

test("HardAI takes an immediate win", () => {
  const board = new Board();
  board.placeMark(0, 0, "O");
  board.placeMark(0, 1, "O");
  board.placeMark(1, 0, "X");
  board.placeMark(1, 1, "X");
  board.placeMark(2, 2, "X");
  assert.deepEqual(new HardAI().chooseMove(board, "O"), [0, 2]);
});

test("HardAI blocks the opponent's win", () => {
  const board = new Board();
  board.placeMark(0, 0, "X");
  board.placeMark(0, 1, "X");
  board.placeMark(1, 1, "O");
  assert.deepEqual(new HardAI().chooseMove(board, "O"), [0, 2]);
});

// Plays every possible human move against HardAI and fails if the human ever wins.
function assertNeverLoses(aiMark) {
  const ai = new HardAI();
  const human = otherMark(aiMark);
  let games = 0;

  function play(board, turn) {
    if (board.hasWon(aiMark) || board.isFull()) {
      games++;
      return;
    }
    if (turn === aiMark) {
      const [r, c] = ai.chooseMove(board, aiMark);
      board.placeMark(r, c, aiMark);
      play(board, human);
      board.removeMark(r, c);
    } else {
      for (const [r, c] of board.emptyCells()) {
        board.placeMark(r, c, human);
        assert.equal(board.hasWon(human), false, `human won:\n${JSON.stringify(board.snapshot())}`);
        play(board, aiMark);
        board.removeMark(r, c);
      }
    }
  }

  play(new Board(), "X"); // X always starts
  assert.ok(games > 0);
}

test("HardAI never loses playing O", () => assertNeverLoses("O"));
test("HardAI never loses playing X", () => assertNeverLoses("X"));
