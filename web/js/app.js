// UI layer: screen flow, rendering, and input handling.
// All game rules live in board.js / ai.js; this file only wires them to the page.

import { Board } from "./board.js";
import { EasyAI, HardAI, otherMark } from "./ai.js";

const AI_DELAY_MS = 550;

// Slightly wobbly paths so the marks look hand-drawn. Each <path> is animated by CSS.
const MARK_SVG = {
  X: `<svg viewBox="0 0 100 100" aria-hidden="true">
        <path pathLength="1" d="M24 22 C 40 40, 58 60, 77 79" />
        <path pathLength="1" class="second" d="M77 23 C 60 38, 42 58, 23 78" />
      </svg>`,
  O: `<svg viewBox="0 0 100 100" aria-hidden="true">
        <path pathLength="1" d="M50 20 C 70 19, 81 34, 80 51 C 79 69, 66 81, 49 80 C 31 79, 20 66, 21 49 C 22 32, 34 21, 52 22" />
      </svg>`,
};

const $ = (id) => document.getElementById(id);
const els = {
  menuScreen: $("menu-screen"),
  menuForm: $("menu-form"),
  aiOptions: $("ai-options"),
  gameScreen: $("game-screen"),
  status: $("status"),
  board: $("board"),
  scoreX: $("score-x"),
  scoreO: $("score-o"),
  scoreDraw: $("score-draw"),
  scoreXLabel: $("score-x-label"),
  scoreOLabel: $("score-o-label"),
  restartBtn: $("restart-btn"),
  menuBtn: $("menu-btn"),
};

const state = {
  settings: null, // { mode: "ai" | "pvp", difficulty, humanMark }
  ai: null,
  board: null,
  turn: "X",
  over: false,
  aiThinking: false,
  round: 0, // bumped on every new round so stale AI timeouts are ignored
  scores: { X: 0, O: 0, draw: 0 },
};

const isAiTurn = () => state.settings.mode === "ai" && state.turn !== state.settings.humanMark;

function nameOf(mark) {
  if (state.settings.mode === "pvp") return `Player ${mark}`;
  return mark === state.settings.humanMark ? "You" : "AI";
}

// ---------- Rendering ----------

function buildBoard() {
  els.board.innerHTML = "";
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 3; c++) {
      const cell = document.createElement("button");
      cell.type = "button";
      cell.className = "cell";
      cell.dataset.row = r;
      cell.dataset.col = c;
      cell.setAttribute("aria-label", `Row ${r + 1}, column ${c + 1}, empty`);
      els.board.append(cell);
    }
  }
}

function cellAt(r, c) {
  return els.board.children[r * 3 + c];
}

function drawMark(r, c, mark) {
  const cell = cellAt(r, c);
  cell.innerHTML = MARK_SVG[mark];
  cell.classList.add("filled", `mark-${mark.toLowerCase()}`);
  cell.setAttribute("aria-label", `Row ${r + 1}, column ${c + 1}, ${mark}`);
}

function updateInteractivity() {
  const locked = state.over || state.aiThinking;
  els.board.classList.toggle("locked", locked);
  els.board.dataset.turn = state.turn.toLowerCase();
  for (const cell of els.board.children) {
    cell.disabled = locked || cell.classList.contains("filled");
  }
}

function setStatus(text, tone = "") {
  els.status.textContent = text;
  els.status.className = `status ${tone}`;
}

function renderTurnStatus() {
  const mark = state.turn;
  if (state.aiThinking) {
    setStatus("AI is thinking…", `turn-${mark.toLowerCase()} thinking`);
  } else if (state.settings.mode === "ai") {
    setStatus(`Your turn (${mark})`, `turn-${mark.toLowerCase()}`);
  } else {
    setStatus(`${nameOf(mark)}'s turn`, `turn-${mark.toLowerCase()}`);
  }
}

function renderScores() {
  els.scoreX.textContent = state.scores.X;
  els.scoreO.textContent = state.scores.O;
  els.scoreDraw.textContent = state.scores.draw;
  const label = (mark) => (state.settings.mode === "pvp" ? nameOf(mark) : `${nameOf(mark)} (${mark})`);
  els.scoreXLabel.textContent = label("X");
  els.scoreOLabel.textContent = label("O");
}

function bump(el) {
  el.classList.remove("bump");
  void el.offsetWidth; // restart the CSS animation
  el.classList.add("bump");
}

// ---------- Game flow ----------

function startRound() {
  state.round++;
  state.board = new Board();
  state.turn = "X"; // X always starts
  state.over = false;
  state.aiThinking = false;
  buildBoard();
  els.board.classList.remove("has-winner");
  renderScores();
  nextTurn();
}

function nextTurn() {
  if (isAiTurn()) {
    state.aiThinking = true;
    renderTurnStatus();
    updateInteractivity();
    const round = state.round;
    setTimeout(() => {
      if (round !== state.round) return; // round was restarted or left
      state.aiThinking = false;
      const move = state.ai.chooseMove(state.board, state.turn);
      if (move) play(move[0], move[1]);
    }, AI_DELAY_MS);
  } else {
    renderTurnStatus();
    updateInteractivity();
  }
}

function play(r, c) {
  const mark = state.turn;
  if (!state.board.placeMark(r, c, mark)) return;
  drawMark(r, c, mark);

  const line = state.board.winningLine(mark);
  if (line) return finish(mark, line);
  if (state.board.isFull()) return finish(null);

  state.turn = otherMark(mark);
  nextTurn();
}

function finish(winner, line = []) {
  state.over = true;
  updateInteractivity();

  if (winner) {
    state.scores[winner]++;
    els.board.classList.add("has-winner");
    line.forEach(([r, c]) => cellAt(r, c).classList.add("win"));
    const text =
      state.settings.mode === "pvp"
        ? `Player ${winner} wins! 🎉`
        : winner === state.settings.humanMark
          ? "You win! 🎉"
          : "AI wins! Try again?";
    setStatus(text, `result win-${winner.toLowerCase()}`);
    bump(winner === "X" ? els.scoreX : els.scoreO);
  } else {
    state.scores.draw++;
    setStatus("It's a draw! 🤝", "result draw");
    bump(els.scoreDraw);
  }
  renderScores();
}

function showScreen(name) {
  els.menuScreen.hidden = name !== "menu";
  els.gameScreen.hidden = name !== "game";
}

// ---------- Event handlers ----------

els.board.addEventListener("click", (e) => {
  const cell = e.target.closest(".cell");
  if (!cell || cell.disabled || state.over || state.aiThinking) return;
  play(Number(cell.dataset.row), Number(cell.dataset.col));
});

els.menuForm.addEventListener("change", () => {
  els.aiOptions.hidden = els.menuForm.elements.mode.value !== "ai";
});

els.menuForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const form = els.menuForm.elements;
  const mode = form.mode.value;
  state.settings = { mode, difficulty: form.difficulty.value, humanMark: mode === "ai" ? form.mark.value : null };
  state.ai = mode === "ai" ? (form.difficulty.value === "hard" ? new HardAI() : new EasyAI()) : null;
  state.scores = { X: 0, O: 0, draw: 0 };
  showScreen("game");
  startRound();
});

els.restartBtn.addEventListener("click", startRound);

els.menuBtn.addEventListener("click", () => {
  state.round++; // cancel any pending AI move
  showScreen("menu");
});
