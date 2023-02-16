// Play/Pause logic

const playBtn = document.getElementById('play');
const stopBtn = document.getElementById('stop');
const plusSample = document.getElementById('plusSample');
const minusSample = document.getElementById('minusSample');
let playState = false;
let playIntervalID = 0;
let intervalId = 0;

playBtn.addEventListener('click', function () {
    // pause slider
    if (playState === true) {
        console.log('pause slider')
        playState = false;
        clearInterval(playIntervalID)
        return
    };
    // restart slider when at end
    if (slider.value === slider.max) {
        console.log('restart slider')
        slider.value = 0;

    }
    // play slider
    playState = true;
    console.log('play');
    playIntervalID = setInterval(playPlots, 100);
});

stopBtn.addEventListener('click', function () {
    playState = false;
    clearInterval(playIntervalID);
    slider.value = 0;
    console.log('stop');
});

plusSample.addEventListener('mousedown', function () {
    slider.dispatchEvent(new Event('input', {}), slider.value++);
    intervalId = setInterval(() => {
        slider.value++;
        slider.dispatchEvent(new Event('input', {}), slider.value++);
    }, 100);
})
plusSample.addEventListener('mouseup', () => { clearInterval(intervalId) })

minusSample.addEventListener('mousedown', function () {
    slider.dispatchEvent(new Event('input', {}), slider.value--);
    intervalId = setInterval(() => {
        slider.value--;
        slider.dispatchEvent(new Event('input', {}), slider.value--);
    }, 100);
})
minusSample.addEventListener('mouseup', () => { clearInterval(intervalId) })

function playPlots() {
    if (playState === true) {

        slider.dispatchEvent(new Event('input', {}), slider.value++);
        if (slider.value === slider.max) {
            playState = false;
        }
    }
};