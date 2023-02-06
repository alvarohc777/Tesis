// API endpoints
const csvEndpoint = "http://127.0.0.1:8080/uploadCSV";
const signalNameEndpoint = "http://127.0.0.1:8080/signalName";
const plotsEndpoint = "http://127.0.0.1:8080/plotsList";

// Variables


// Constants
const reader = new FileReader();
const csvForm = document.getElementById("csvForm");
const csvInput = document.getElementById("csvInput");
const signalMenu = document.getElementById('signalMenu');
const plotsMenu = document.getElementById('plotsMenu');
const plotsSection = document.getElementById('plots')
// eventListeners

// Cargue de datos

function selectCSV() {
    csvInput.click();
}

csvInput.addEventListener('input', function () {
    console.log('Se cargó el archivo' + this.files[0].name);
    let file = this.files[0];
    reader.onload = (e) => console.log(e.target.result);
    reader.onerror = (error) => console.log(error);
    reader.readAsText(file);
});

csvForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData;
    formData.append('csv_files', csvInput.files[0])
    fetch(csvEndpoint, {
        method: 'post',
        body: formData
    })
        .then(res => res.json())
        .then((data) => {
            signalList = data;
            console.log(signalList.signals_list);
            signalListAppend(signalList.signals_list)
        })
        .catch(err => console.log(err))
});


// Submit signal

signalMenu.addEventListener('submit', function (e) {
    e.preventDefault();
});

signalMenu.addEventListener('change', function (e) {
    e.preventDefault();
    let signalName = document.querySelector('input[name="signalName"]:checked').value;
    console.log(JSON.stringify({ "signal_name": signalName }));
    fetch(signalNameEndpoint, {
        method: 'post',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "signal_name": signalName }),
    })
        .then(res => res.json())
        .then((data) => console.log(data))
        .catch(err => console.log(err))
});


// submit plots

plotsMenu.addEventListener('submit', function (e) {
    e.preventDefault();
});
const pltDict = {};
for (let value of plotsMenu.getElementsByTagName('input')) {
    pltDict[value.id] = value;
    value.addEventListener('change', function (e) {
        // const newDiv = document.createElement('div');
        // const divContent = document.createTextNode(value.value);
        // newDiv.appendChild(divContent);
        // plotsSection.appendChild(newDiv);
        let divHTML = `<div class="plotDiv"><h3>${value.value}</h3><div id="signal" style="width: 400px;height:300px;background:black"></div></div>`
        plotsSection.insertAdjacentHTML('beforeend', divHTML)
    })
};
console.log(pltDict)


