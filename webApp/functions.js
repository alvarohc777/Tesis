
// Cargue de datos

function selectCSV() {
    csvInput.click();
}

function submitSignal() {
    signalMenu.getElementsByTagName('button')[0].click();
}

// Append radio buttons
function signalListAppend(list) {
    signalMenu.textContent = '';
    let btn1 = document.createElement("button");
    btn1.type = 'submit';
    btn1.textContent = "prueba"
    btn1.style.display = "none";
    signalMenu.appendChild(btn1);
    let signalDiv = document.getElementById("signalList");


    let arrayLength = list.length;
    for (let i = 0; i < arrayLength; i++) {

        let radiobox = document.createElement('input');
        radiobox.type = 'radio';
        // radiobox.id = list[i];
        radiobox.required = true;
        radiobox.value = list[i]
        radiobox.name = 'signalName';
        // if (i === 0) {
        //     radiobox.checked = true;
        // }
        let label = document.createElement('label');
        label.htmlFor = list[i];
        label.textContent = list[i];

        // Append elements to signalMenu
        signalMenu.appendChild(radiobox);
        signalMenu.appendChild(label);
        signalMenu.appendChild(document.createElement('BR'));
    }
}



// Create image
let plotLayout = {
    autosize: false,
    width: 400,
    height: 300,
    margin: {
        l: 50,
        r: 50,
        b: 50,
        t: 50,
    },
}

function imageCreator(data, element_id) {
    let fig = document.getElementById(element_id);
    fig.parentNode.style.display = "block";
    Plotly.newPlot('signal1', [{
        x: data[0],
        y: data[1]
    }],
        plotLayout
    )
}

function submitPlots() {
    plotsMenu.getElementsByTagName('button')[0].click();
}

csvInput.addEventListener('input', function () {
    console.log("Se cargó el archivo:" + this.files[0].name);
    let file = this.files[0]
    reader.onload = (e) => console.log(e.target.result);
    reader.onerror = (error) => console.log(error);
    reader.readAsText(file);

});