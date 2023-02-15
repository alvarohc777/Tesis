const slider = document.getElementById('slider')
let sliderMin = slider.min;
let sliderMax = slider.max;
let sliderVal = slider.value;





function signalListAppend(list) {
    signalMenu.textContent = '';

    let btn1 = document.createElement("button");
    btn1.type = 'submit';
    btn1.textContent = 'prueba';
    btn1.style.display = 'none';
    signalMenu.appendChild(btn1);

    let signalDiv = document.getElementById("signalList");

    let arrayLength = list.length;
    for (let i = 0; i < arrayLength; i++) {
        let radiobox = document.createElement('input');
        radiobox.type = 'radio';
        radiobox.required = true;
        radiobox.value = list[i];
        radiobox.id = list[i];
        radiobox.name = 'signalName';

        let label = document.createElement('label');
        label.htmlFor = list[i];
        label.textContent = list[i];

        signalMenu.appendChild(radiobox);
        signalMenu.appendChild(label);
        signalMenu.appendChild(document.createElement('BR'));
    }
}

// Signal Divs

function plotSignal(value) {

    let divExists = document.getElementById(value.value);
    if (divExists) {
        divExists.parentElement.style = 'block'
    } else {
        createDiv(value);
        fetchSignalData(value.value);
    }

};

function removeSignal(value) {
    let divExists = document.getElementById(value.value);
    if (divExists) {
        divExists.parentElement.style.display = 'none';
    } else {
        console.log('doesnt exist')
    }
};

function createDiv(value) {
    const plotDiv = document.createElement('div');
    const h3 = document.createElement('h3');
    const signalDiv = document.createElement('div');
    plotDiv.backgroundColor = "black";
    plotDiv.classList.add('plotDiv')


    signalDiv.style['width'] = '400px';
    signalDiv.style['height'] = '300px';
    signalDiv.style.backgroundColor = 'white';
    signalDiv.id = value.value;
    signalDiv.className = 'responsiveDiv';
    h3.innerHTML = value.dataset.name;

    let observer = new ResizeObserver(function (mutations) {
        window.dispatchEvent(new Event('resize'));
    });
    observer.observe(signalDiv, {
        attributes: true
    })

    plotDiv.appendChild(h3);
    plotDiv.appendChild(signalDiv);
    plotsSection.insertAdjacentElement('beforeend', plotDiv);
};

function fetchSignalData(element_id) {
    // console.log(`${plotsEndpoint}${element_id}`)
    fetch(`${plotsEndpoint}${element_id}`, {
        method: 'post',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(plotDict)
    })
        .then(res => res.json())
        .then((data) => {

            if (data[3] === 'img') {
                imageCreator(data, element_id)
            } else if (data[3] === 'anim') {
                slider.max = data[0].length - 1
                animationCreator(data, element_id)
            } else if (data[3] == 'STFT') {
                slider.max = data[0].length - 1
                stftCreator(data, element_id)
            }

        })
        .catch(err => console.log(err))
};

// plot configs and functions

const plotOptions = {
    scrollZoom: true,
    responsive: true,
    // displayModeBar: true,
}

const plotLayout = {
    autosize: true,
    margin: {
        l: 50,
        r: 50,
        b: 50,
        t: 50,
    },
    modebar: {
        orientation: 'v',
    }
};

// Image plot
function imageCreator(data, element_id) {
    let fig = document.getElementById(element_id);
    fig.parentNode.style.display = "block";

    let layout = JSON.parse(JSON.stringify(plotLayout));
    Plotly.newPlot(element_id, [{
        x: data[0],
        y: data[1],
        line: { shape: data[2] },
    }],
        layout,
        plotOptions
    )
};


function animationCreator(data, element_id) {

    let fig = document.getElementById(element_id);

    let window_index = 0
    let maxWindowIndex = data[0].length - 1

    const animLayout = {
        yaxis: {
            range: [data[2][1], data[2][0]]
        },
    };
    let layout = JSON.parse(JSON.stringify(plotLayout));
    layout = Object.assign(layout, animLayout);

    fig.parentNode.style.display = "block";
    Plotly.react(element_id, [{
        x: data[0][slider.value],
        y: data[1][slider.value],
        // line: { shape: data[2] },
    }],
        layout,
        plotOptions
    )


    slider.addEventListener('input', function () {
        Plotly.react(element_id, [{
            x: data[0][slider.value],
            y: data[1][slider.value],
        }],
            layout,
            plotOptions)
    });
};


function stftCreator(data, element_id) {
    let fig = document.getElementById(element_id);
    let window_index = 0
    let maxWindowIndex = data[0].length - 1

    const stftLayout = {
        yaxis: {
            range: [data[2][1], data[2][0]]
        },
        xaxis: {
            tickangle: -45,
            tickvals: data[0][window_index].slice(0, 11),
            // ticktext: ['0', '60', '', '180', '', '300', '', '420', '', '540', ''],
            ticklabelstep: 2,
        },
    };

    let layout = JSON.parse(JSON.stringify(plotLayout));
    layout = Object.assign(layout, stftLayout);

    fig.parentNode.style.display = "block";
    Plotly.newPlot(element_id, [{
        x: data[0][slider.value].slice(0, 11),
        y: data[1][slider.value],
        // line: { shape: data[2] },
        // mode: 'markers',
        type: 'bar',
        width: 10,
    }],
        layout,
        plotOptions
    )

    // Reactive plot
    slider.addEventListener('input', function () {
        Plotly.react(element_id, [{
            x: data[0][slider.value].slice(0, 11),
            y: data[1][slider.value],
            type: 'bar',
            width: 10,
        }],
            layout,
            plotOptions)
    });
};






// Play/Pause logic

const playBtn = document.getElementById('play');
const stopBtn = document.getElementById('stop');
const plusSample = document.getElementById('plusSample');
const minusSample = document.getElementById('minusSample');
let playState = false;
let playIntervalID = 0;
let intervalId = 0;

playBtn.addEventListener('click', function () {
    if (playState === true) {
        console.log('pause')
        playState = false;
        clearInterval(playIntervalID)
        return
    };
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
    intervalId = setInterval(() => { slider.value++ }, 100);
})
plusSample.addEventListener('mouseup', () => { clearInterval(intervalId) })

minusSample.addEventListener('mousedown', function () {
    slider.dispatchEvent(new Event('input', {}), slider.value--);
    intervalId = setInterval(() => { slider.value-- }, 100);
})
minusSample.addEventListener('mouseup', () => { clearInterval(intervalId) })
// function funcionPrueba() {
//     console.log('hola')
// }
// var intervalId;
// minusSample.addEventListener("mousedown", function () {
//     intervalId = setInterval(console.log('hola'), 500);
// }).mouseup(function () {
//     clearInterval(intervalId);
// });

function playPlots() {
    if (playState === true) {
        slider.dispatchEvent(new Event('input', {}), slider.value++);
        if (slider.value === slider.max) {
            playState = false;
            // slider.value = 0
        }
    }
};
