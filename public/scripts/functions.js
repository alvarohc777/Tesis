const slider = document.getElementById('slider')
let sliderMin = slider.min;
let sliderMax = slider.max;
let animationsExist = false;

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

    // console.log('value')
    // console.log(value)
    // // console.log(plotDiv.style.order)
    // console.log(value.dataset.index)
    // plotDiv.style.order = value.dataset.index
    const plotDiv = document.createElement('div');
    const h3 = document.createElement('h3');
    const signalDiv = document.createElement('div');
    plotDiv.backgroundColor = "black";
    plotDiv.classList.add('plotDiv');

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
            } else if (data[3] === 'trip') {
                console.log(data[0].length)
                tripCreator(data, element_id)
            } else if (data[3] === 'anim') {
                console.log(data[0].length)
                slider.max = data[0].length - 1
                animationsExist = true;
                animationCreator(data, element_id)
                slider.dispatchEvent(new Event('input', {}), slider.value = slider.value);
            } else if (data[3] == 'STFT') {
                slider.max = data[0].length - 1
                animationsExist = true;
                stftCreator(data, element_id)
                slider.dispatchEvent(new Event('input', {}), slider.value = slider.value);
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
    let maxWindowValueY = Math.max(...data[1]);
    let minWindowValueY = Math.min(...data[1]);
    slider.addEventListener('input', () => {

        if (animationsExist === true) {

            // let maxWindowValue = data[1].indexOf(Math.max(...data[1]));

            let minWindowValueX = data[0][slider.value * 4];
            let maxWindowValueX = data[0][(slider.value * 4) + 63];

            let update = {
                shapes: [
                    // Begining of Window
                    {
                        type: 'line',
                        x0: minWindowValueX,
                        y0: minWindowValueY,
                        x1: minWindowValueX,
                        y1: maxWindowValueY,
                        line: {
                            color: 'rgb(55, 128, 191)',
                            width: 1.5
                        }
                    },
                    // End of window
                    {
                        type: 'line',
                        x0: maxWindowValueX,
                        y0: minWindowValueY,
                        x1: maxWindowValueX,
                        y1: maxWindowValueY,
                        line: {
                            color: 'rgb(55, 128, 191)',
                            width: 1.5
                        }
                    },
                    // top of window
                    {
                        type: 'line',
                        x0: minWindowValueX,
                        y0: maxWindowValueY,
                        x1: maxWindowValueX,
                        y1: maxWindowValueY,
                        line: {
                            color: 'rgb(55, 128, 191)',
                            width: 1.5
                        }
                    },
                    // bottom of window
                    {
                        type: 'line',
                        x0: minWindowValueX,
                        y0: minWindowValueY,
                        x1: maxWindowValueX,
                        y1: minWindowValueY,
                        line: {
                            color: 'rgb(55, 128, 191)',
                            width: 1.5
                        }
                    }]
            }
            Plotly.relayout(element_id, update);
        }
    })
};


// Image plot
function tripCreator(data, element_id) {
    let fig = document.getElementById(element_id);
    fig.parentNode.style.display = "block";

    let maxWindowValueY = Math.max(...data[1]);
    let minWindowValueY = Math.min(...data[1]);
    const staticLayout = {
        xaxis: {
            range: [data[0][0], (data[0][parseInt(data[0].length) - 1])]
        },
        yaxis: {
            range: [minWindowValueY - 0.03, maxWindowValueY + 0.03]
        },
        showlegend: false
    }
    let layout = JSON.parse(JSON.stringify(plotLayout));
    layout = Object.assign(layout, staticLayout);

    Plotly.newPlot(element_id, [{
        x: data[0],
        y: data[1],
        line: { shape: data[2] },
    }],
        layout,
        plotOptions
    );
    let maxWindowValueX = data[0][parseInt(slider.value) + 1];
    let valueY = data[1][parseInt(slider.value) + 1];
    console.log(parseInt(slider.value) + 1);
    let tripSignal = {
        x: [maxWindowValueX],
        y: [valueY],
        mode: 'markers'
    }

    Plotly.addTraces(element_id, tripSignal, 1);

    slider.addEventListener('input', () => {

        if (animationsExist === true) {

            // let maxWindowValue = data[1].indexOf(Math.max(...data[1]));
            Plotly.deleteTraces(element_id, 1);
            let maxWindowValueX = data[0][parseInt(slider.value) + 1];
            let valueY = data[1][parseInt(slider.value) + 1];
            console.log(parseInt(slider.value) + 1);
            let tripSignal = {
                x: [maxWindowValueX],
                y: [valueY],
                mode: 'markers',
                marker: {
                    color: 'rgb(139,0,0)',
                    size: 8
                }
            }

            Plotly.addTraces(element_id, tripSignal, 1);
            // Plotly.update(element_id, tripSignal, ll, 1);
        }
    })
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
