document.addEventListener('DOMContentLoaded', () => {
    const gameContainer = document.getElementById('game-container');
    const dinosaur = document.getElementById('dinosaur');
    const scoreDisplay = document.getElementById('score');
    const jumpButton = document.getElementById('jump-button');
    let score = 0;
    let isJumping = false;

    function jump() {
        if (!isJumping) {
            isJumping = true;
            let position = 0;
            let timerId = setInterval(() => {
                if (position === 150) {
                    clearInterval(timerId);
                    let downTimerId = setInterval(() => {
                        if (position === 0) {
                            clearInterval(downTimerId);
                            isJumping = false;
                        }
                        position -= 30;
                        dinosaur.style.bottom = position + 'px';
                    }, 20);
                }
                position += 30;
                dinosaur.style.bottom = position + 'px';
            }, 20);
        }
    }

    jumpButton.addEventListener('click', jump);

    function generateCactus() {
        const cactus = document.createElement('div');
        let cactusPosition = 600;
        let randomTime = Math.random() * 6000;

        cactus.classList.add('cactus');
        gameContainer.appendChild(cactus);
        cactus.style.left = cactusPosition + 'px';

        let timerId = setInterval(() => {
            if (cactusPosition < -20) {
                clearInterval(timerId);
                gameContainer.removeChild(cactus);
                score += 100;
                scoreDisplay.textContent = 'Score: ' + score;
            } else if (cactusPosition > 0 && cactusPosition < 60 && position < 60) {
                clearInterval(timerId);
                gameContainer.removeChild(cactus);
                alert('Game Over. Final Score: ' + score);
                score = 0;
                scoreDisplay.textContent = 'Score: ' + score;
            } else {
                cactusPosition -= 10;
                cactus.style.left = cactusPosition + 'px';
            }
        }, 20);

        if (score < 10000) {
            setTimeout(generateCactus, randomTime);
        } else {
            alert('Congratulations! You reached the finish line.');
        }
    }

    generateCactus();
});
