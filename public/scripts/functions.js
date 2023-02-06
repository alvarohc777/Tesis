

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
    signalDiv.style.backgroundColor = 'black';
    signalDiv.id = value.value;
    h3.innerHTML = value.dataset.name;


    let resizeObserver = new ResizeObserver(onResize);
    resizeObserver.observe(signalDiv);

    plotDiv.appendChild(h3);
    plotDiv.appendChild(signalDiv);
    plotsSection.insertAdjacentElement('beforeend', plotDiv);
}

let plotLayout = {
    // autosize: true,
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
            displayModeBar: true,
            scrollZoom: true
        }
    )
    let plotContainer = fig.getElementsByClassName('plot-container')[0]
    let resizeObserver = new ResizeObserver(onResize);
    resizeObserver.observe(plotContainer);

};

function onResize(e) {
    let plotContainerResize = e[0].target
    plotContainerResize.parentElement.style.width = plotContainerResize.style.width;
    plotContainerResize.parentElement.style.height = plotContainerResize.style.height;

    Plotly.Plots.resize(plotContainerResize);
};

function fetchSignalData(element_id) {
    console.log(`${plotsEndpoint}${element_id}`)
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
            console.log(data);
            imageCreator(data, element_id)
        })
        .catch(err => console.log(err))
};