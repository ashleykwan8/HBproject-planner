const startingMinutes = 10;
let time = startingMinutes * 60;

const countdownEl =  document.getElementById('meditate');
const startButton = document.getElementById('start'); 

function updateTimer() {
    const minutes = Math.floor(time / 60);
    let seconds = time % 60;

    seconds = seconds < 10 ? '0' + seconds : seconds;

    countdownEl.innerHTML = `${minutes}:${seconds}`;
    time --;
    
}  

startButton.addEventListener("click", () => {
    setInterval(updateTimer, 1000);
}); 
