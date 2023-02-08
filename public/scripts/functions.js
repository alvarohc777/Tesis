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
}

// plot configs and functions

let plotLayout = {
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

function imageCreator(data, element_id) {
    let fig = document.getElementById(element_id);
    fig.parentNode.style.display = "block";
    Plotly.newPlot(element_id, [{
        x: data[0],
        y: data[1],
        line: { shape: data[2] },
    }],
        plotLayout,
        {
            // displayModeBar: true,
            scrollZoom: true,
            responsive: true
        }
    )
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
                // imageCreator(data, element_id)
                console.log('img')
            } else if (data[3] === 'anim') {
                animationCreator(element_id)
            }

        })
        .catch(err => console.log(err))
};

function animationCreator(element_id) {

    let fig = document.getElementById(element_id);
    fig.parentNode.style.display = "block";
    var n = 100;
    var x = [], y = [], z = [];
    var dt = 0.015;

    for (i = 0; i < n; i++) {
        x[i] = Math.random() * 2 - 1;
        y[i] = Math.random() * 2 - 1;
        z[i] = 30 + Math.random() * 10;
    }

    Plotly.newPlot(element_id, [{
        x: x,
        y: y,
        mode: 'markers'
    }], {
        xaxis: { range: [-40, 40] },
        yaxis: { range: [0, 60] }
    }, { showSendToCloud: true })

    // function compute() {
    //     var s = 10, b = 8 / 3, r = 28;
    //     var dx, dy, dz;
    //     var xh, yh, zh;
    //     for (var i = 0; i < n; i++) {
    //         dx = s * (y[i] - x[i]);
    //         dy = x[i] * (r - z[i]) - y[i];
    //         dz = x[i] * y[i] - b * z[i];

    //         xh = x[i] + dx * dt * 0.5;
    //         yh = y[i] + dy * dt * 0.5;
    //         zh = z[i] + dz * dt * 0.5;

    //         dx = s * (yh - xh);
    //         dy = xh * (r - zh) - yh;
    //         dz = xh * yh - b * zh;

    //         x[i] += dx * dt;
    //         y[i] += dy * dt;
    //         z[i] += dz * dt;
    //     }
    // }

    // function update() {
    //     compute();

    //     Plotly.animate(element_id, {
    //         data: [{ x: x, y: z }]
    //     }, {
    //         transition: {
    //             duration: 0,
    //         },
    //         frame: {
    //             duration: 0,
    //             redraw: false,
    //         }
    //     });

    //     requestAnimationFrame(update);
    // }

    // requestAnimationFrame(update);
};