// 更新细胞的数量
numCells = Math.floor(canvas.width / cellSize);

// 重新创建细胞状态的二维数组
cells = [];
for (var i = 0; i < numCells; i++) {
    cells[i] = [];

// 获取canvas元素和绘图上下文
var canvas = document.getElementById("gameCanvas");
var ctx = canvas.getContext("2d");

// 定义细胞的大小和数量
var cellSize = 10;
var numCells = Math.floor(canvas.width / cellSize);

// 创建细胞状态的二维数组
var cells = [];
for (var i = 0; i < numCells; i++) {
    cells[i] = [];
    for (var j = 0; j < numCells; j++) {
        cells[i][j] = Math.random() > 0.5 ? 1 : 0; // 随机初始化细胞状态
    }
}

// 绘制细胞
function drawCells() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (var i = 0; i < numCells; i++) {
        for (var j = 0; j < numCells; j++) {
            if (cells[i][j] === 1) {
                ctx.fillRect(i * cellSize, j * cellSize, cellSize, cellSize);
            }
        }
    }
}

// 更新细胞状态
function updateCells() {
    var newCells = [];

    for (var i = 0; i < numCells; i++) {
        newCells[i] = [];
        for (var j = 0; j < numCells; j++) {
            var neighbors = countNeighbors(i, j);

            if (cells[i][j] === 1) {
                if (neighbors < 2 || neighbors > 3) {
                    newCells[i][j] = 0; // 细胞死亡
                } else {
                    newCells[i][j] = 1; // 细胞存活
                }
            } else {
                if (neighbors === 3) {
                    newCells[i][j] = 1; // 细胞复活
                } else {
                    newCells[i][j] = 0; // 细胞仍死亡
                }
            }
        }
    }

    cells = newCells;
}

// 计算细胞周围的存活邻居数量
function countNeighbors(x, y) {
    var count = 0;

    for (var i = -1; i <= 1; i++) {
        for (var j = -1; j <= 1; j++) {
            var neighborX = (x + i + numCells) % numCells;
            var neighborY = (y + j + numCells) % numCells;

            if (cells[neighborX][neighborY] === 1) {
                count++;
            }
        }
    }

    if (cells[x][y] === 1) {
        count--; // 排除自身
    }

    return count;
}

// 游戏循环
function gameLoop() {
    drawCells();
    updateCells();

    requestAnimationFrame(gameLoop);
}

// 启动游戏循环
gameLoop();
