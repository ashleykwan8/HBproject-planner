const startingMinutes = 10;
let time = startingMinutes * 60;

const countdownEl =  document.getElementById('meditate');
// const startButton = document.getElementById('start'); 
// const startButton = $('#start');
// const stopButton = document.getElementById('stop')

function updateTimer() {
    const minutes = Math.floor(time / 60);
    let seconds = time % 60;

    seconds = seconds < 10 ? '0' + seconds : seconds;

    countdownEl.innerHTML = `${minutes}:${seconds}`;
    time --;
} 

$('#start').on("click", (evt) => {
    timer = setInterval(updateTimer, 1000);
});

// startButton.addEventListener("click", (evt) => {
//     timer = setInterval(updateTimer, 1000);
// }); 

$('#stop').on("click", (evt) => {
    clearInterval(timer);
});


