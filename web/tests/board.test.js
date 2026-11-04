import { test } from "node:test";
import assert from "node:assert/strict";
import { Board } from "../js/board.js";

function boardFrom(rows) {
  const board = new Board();
  rows.forEach((row, r) =>
    [...row].forEach((cell, c) => {
      if (cell !== ".") board.placeMark(r, c, cell);
    }),
  );
  return board;
}

test("new board is 3x3 and empty", () => {
  const board = new Board();
  assert.equal(board.emptyCells().length, 9);
  assert.equal(board.isFull(), false);
});

test("placeMark rejects taken cells", () => {
  const board = new Board();
  assert.equal(board.placeMark(1, 1, "X"), true);
  assert.equal(board.placeMark(1, 1, "O"), false);
  assert.equal(board.snapshot()[1][1], "X");
});

test("placeMark rejects out-of-range coordinates and invalid marks", () => {
  const board = new Board();
  assert.equal(board.placeMark(-1, 0, "X"), false);
  assert.equal(board.placeMark(0, 3, "X"), false);
  assert.equal(board.placeMark(0, 0, "Z"), false);
  assert.equal(board.emptyCells().length, 9);
});

test("removeMark clears a cell", () => {
  const board = new Board();
  board.placeMark(0, 0, "O");
  board.removeMark(0, 0);
  assert.equal(board.emptyCells().length, 9);
});

test("detects row, column, diagonal and anti-diagonal wins", () => {
  assert.deepEqual(boardFrom(["...", "XXX", "..."]).winningLine("X"), [[1, 0], [1, 1], [1, 2]]);
  assert.deepEqual(boardFrom(["..O", "..O", "..O"]).winningLine("O"), [[0, 2], [1, 2], [2, 2]]);
  assert.deepEqual(boardFrom(["X..", ".X.", "..X"]).winningLine("X"), [[0, 0], [1, 1], [2, 2]]);
  assert.deepEqual(boardFrom(["..O", ".O.", "O.."]).winningLine("O"), [[0, 2], [1, 1], [2, 0]]);
});

test("no win on a full drawn board", () => {
  const board = boardFrom(["XOX", "XOO", "OXX"]);
  assert.equal(board.isFull(), true);
  assert.equal(board.hasWon("X"), false);
  assert.equal(board.hasWon("O"), false);
});

test("snapshot is a copy", () => {
  const board = new Board();
  board.snapshot()[0][0] = "X";
  assert.equal(board.emptyCells().length, 9);
});
