var boardSize = 10;
var numMines = 10;
var board = [];

function createBoard() {
  for (var i = 0; i < boardSize; i++) {
    var row = [];
    for (var j = 0; j < boardSize; j++) {
      row.push({
        isMine: false,
        isRevealed: false,
        numAdjacentMines: 0
      });
    }
    board.push(row);
  }
}

function plantMines() {
  var count = 0;
  while (count < numMines) {
    var row = Math.floor(Math.random() * boardSize);
    var col = Math.floor(Math.random() * boardSize);
    if (!board[row][col].isMine) {
      board[row][col].isMine = true;
      count++;
    }
  }
}

function calculateAdjacentMines() {
  for (var i = 0; i < boardSize; i++) {
    for (var j = 0; j < boardSize; j++) {
      if (!board[i][j].isMine) {
        var count = 0;
        for (var dx = -1; dx <= 1; dx++) {
          for (var dy = -1; dy <= 1; dy++) {
            var newRow = i + dx;
            var newCol = j + dy;
            if (newRow >= 0 && newRow < boardSize && newCol >= 0 && newCol < boardSize && board[newRow][newCol].isMine) {
              count++;
            }
          }
        }
        board[i][j].numAdjacentMines = count;
      }
    }
  }
}

function revealCell(row, col) {
  var cell = board[row][col];
  if (cell.isRevealed) {
    return;
  }
  cell.isRevealed = true;

  if (cell.isMine) {
    alert("游戏结束，你踩到了地雷！");
    location.reload();
  } else if (cell.numAdjacentMines > 0) {
    document.getElementById("cell-" + row + "-" + col).innerHTML = cell.numAdjacentMines;
  } else {
    document.getElementById("cell-" + row + "-" + col).style.backgroundColor = "#ccc";
    for (var dx = -1; dx <= 1; dx++) {
      for (var dy = -1; dy <= 1; dy++) {
        var newRow = row + dx;
        var newCol = col + dy;
        if (newRow >= 0 && newRow < boardSize && newCol >= 0 && newCol < boardSize) {
          revealCell(newRow, newCol);
        }
      }
    }
  }
}

function initGame() {
  createBoard();
  plantMines();
  calculateAdjacentMines();

  var boardElement = document.getElementById("board");
  for (var i = 0; i < boardSize; i++) {
    for (var j = 0; j < boardSize; j++) {
      var cell = document.createElement("div");
      cell.className = "cell";
      cell.id = "cell-" + i + "-" + j;
      cell.onclick = (function(row, col) {
        return function() {
          revealCell(row, col);
        };
      })(i, j);
      boardElement.appendChild(cell);
    }
    boardElement.appendChild(document.createElement("br"));
  }
}

initGame();
