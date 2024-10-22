// Configuración inicial del canvas
const canvas = document.getElementById("pongCanvas");
const ctx = canvas.getContext("2d");

// Variables de la paleta
const paddleWidth = 10;
const paddleHeight = 75;
const paddleSpeed = 7;
let playerY = (canvas.height - paddleHeight) / 2;
let aiY = (canvas.height - paddleHeight) / 2;

// Variables de la pelota
let ballX = canvas.width / 2;
let ballY = canvas.height / 2;
const ballRadius = 8;
let ballSpeedX = 4;
let ballSpeedY = 4;

// Variables de puntuación
let playerScore = 0;
let aiScore = 0;

// Manejo de teclas
let upPressed = false;
let downPressed = false;

// Dibujar la paleta
function drawPaddle(x, y) {
  ctx.fillStyle = "white";
  ctx.fillRect(x, y, paddleWidth, paddleHeight);
}

// Dibujar la pelota
function drawBall() {
  ctx.beginPath();
  ctx.arc(ballX, ballY, ballRadius, 0, Math.PI * 2);
  ctx.fillStyle = "white";
  ctx.fill();
  ctx.closePath();
}

// Dibujar el marcador
function drawScore() {
  ctx.font = "32px Arial";
  ctx.fillStyle = "white";
  ctx.fillText(playerScore, canvas.width / 4, 50); // Puntuación del jugador
  ctx.fillText(aiScore, (canvas.width / 4) * 3, 50); // Puntuación de la IA
}

// Mover la pelota
function moveBall() {
  ballX += ballSpeedX;
  ballY += ballSpeedY;

  // Rebote contra las paredes superior e inferior
  if (ballY + ballRadius > canvas.height || ballY - ballRadius < 0) {
    ballSpeedY = -ballSpeedY;
  }

  // Rebote contra las paletas o gol
  if (ballX - ballRadius < paddleWidth) {
    if (ballY > playerY && ballY < playerY + paddleHeight) {
      ballSpeedX = -ballSpeedX;
    } else {
      aiScore++;  // Si la IA anota
      resetBall();
    }
  }
  
  if (ballX + ballRadius > canvas.width - paddleWidth) {
    if (ballY > aiY && ballY < aiY + paddleHeight) {
      ballSpeedX = -ballSpeedX;
    } else {
      playerScore++;  // Si el jugador anota
      resetBall();
    }
  }
}

// Restablecer la posición de la pelota
function resetBall() {
  ballX = canvas.width / 2;
  ballY = canvas.height / 2;
  ballSpeedX = -ballSpeedX;
}

// Movimiento de las paletas
function movePaddles() {
  if (upPressed && playerY > 0) {
    playerY -= paddleSpeed;
  }
  if (downPressed && playerY < canvas.height - paddleHeight) {
    playerY += paddleSpeed;
  }

  // Movimiento básico del AI
  if (aiY + paddleHeight / 2 < ballY) {
    aiY += paddleSpeed - 2;
  } else {
    aiY -= paddleSpeed - 2;
  }
}

// Dibujar la escena
function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpiar el canvas

  drawPaddle(0, playerY); // Paleta del jugador (izquierda)
  drawPaddle(canvas.width - paddleWidth, aiY); // Paleta AI (derecha)
  drawBall(); // Pelota
  drawScore(); // Dibujar puntuación

  moveBall();
  movePaddles();
}

// Control de teclas presionadas
document.addEventListener("keydown", keyDownHandler);
document.addEventListener("keyup", keyUpHandler);

function keyDownHandler(e) {
  if (e.key == "Up" || e.key == "ArrowUp") {
    upPressed = true;
  } else if (e.key == "Down" || e.key == "ArrowDown") {
    downPressed = true;
  }
}

function keyUpHandler(e) {
  if (e.key == "Up" || e.key == "ArrowUp") {
    upPressed = false;
  } else if (e.key == "Down" || e.key == "ArrowDown") {
    downPressed = false;
  }
}

// Llamar continuamente la función draw
setInterval(draw, 1000 / 60); // 60 FPS
