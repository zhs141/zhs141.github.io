document.addEventListener('DOMContentLoaded', function() {
    var gameContainer = document.getElementById('game-container');
    var player = document.getElementById('player');
    var scoreElement = document.getElementById('score');
    var moveLeftButton = document.getElementById('move-left');
    var moveRightButton = document.getElementById('move-right');
    var score = 0;
    var obstacles = [];

    function createObstacle() {
        var obstacle = document.createElement('div');
        obstacle.className = 'obstacle';
        obstacle.style.left = Math.random() * (gameContainer.offsetWidth - obstacle.offsetWidth) + 'px';
        gameContainer.appendChild(obstacle);
        obstacles.push(obstacle);
    }

    function moveObstacles() {
        for (var i = 0; i < obstacles.length; i++) {
            var obstacle = obstacles[i];
            obstacle.style.top = obstacle.offsetTop + 10 + 'px';

            if (obstacle.offsetTop + obstacle.offsetHeight > gameContainer.offsetHeight) {
                gameOver();
                return;
            }

            if (obstacle.offsetTop + obstacle.offsetHeight >= player.offsetTop &&
                obstacle.offsetTop <= player.offsetTop + player.offsetHeight &&
                obstacle.offsetLeft + obstacle.offsetWidth >= player.offsetLeft &&
                obstacle.offsetLeft <= player.offsetLeft + player.offsetWidth) {
                gameOver();
                return;
            }

            for (var j = 0; j < player.bullets.length; j++) {
                var bullet = player.bullets[j];
                if (bullet.offsetTop + bullet.offsetHeight >= obstacle.offsetTop &&
                    bullet.offsetTop <= obstacle.offsetTop + obstacle.offsetHeight &&
                    bullet.offsetLeft + bullet.offsetWidth >= obstacle.offsetLeft &&
                    bullet.offsetLeft <= obstacle.offsetLeft + obstacle.offsetWidth) {
                    gameContainer.removeChild(bullet);
                    player.bullets.splice(j, 1);
                    gameContainer.removeChild(obstacle);
                    obstacles.splice(i, 1);
                    score++;
                    scoreElement.textContent = 'Score: ' + score;
                    break;
                }
            }
        }
    }

    function gameOver() {
        clearInterval(gameInterval);
        clearInterval(shootInterval);
        alert('游戏结束，得分：' + score);
    }

    function movePlayer(direction) {
        var step = 20;
        var left = player.offsetLeft;
        if (direction === 'left') {
            left -= step;
        } else if (direction === 'right') {
            left += step;
        }
        if (left < 0) {
            left = 0;
        } else if (left + player.offsetWidth > gameContainer.offsetWidth) {
            left = gameContainer.offsetWidth - player.offsetWidth;
        }
        player.style.left = left + 'px';
    }

    function shoot() {
        var bullet = document.createElement('div');
        bullet.className = 'bullet';
        bullet.style.left = player.offsetLeft + player.offsetWidth / 2 + 'px';
        bullet.style.top = player.offsetTop - bullet.offsetHeight + 'px';
        gameContainer.appendChild(bullet);
        player.bullets.push(bullet);
    }

    var gameInterval = setInterval(function() {
        createObstacle();
        moveObstacles();
    }, 1000);

    player.bullets = [];
    var shootInterval = setInterval(function() {
        shoot();
    }, 500);

    var moveLeftInterval;
    moveLeftButton.addEventListener('mousedown', function() {
        moveLeftInterval = setInterval(function() {
            movePlayer('left');
        }, 100);
    });

    moveLeftButton.addEventListener('mouseup', function() {
        clearInterval(moveLeftInterval);
    });

    var moveRightInterval;
    moveRightButton.addEventListener('mousedown', function() {
        moveRightInterval = setInterval(function() {
            movePlayer('right');
        }, 100);
    });

    moveRightButton.addEventListener('mouseup', function() {
        clearInterval(moveRightInterval);
    });
});
