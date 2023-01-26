let sidebarState = 0;
var signalList
const csvInput = document.getElementById("csvInput");
const csvForm = document.getElementById("csvForm");
const plotsMenu = document.getElementById("plotsMenu")
const signalMenu = document.getElementById("signalMenu");
const signalListBtn = document.getElementById("signalListBtn");
const reader = new FileReader();
// API endpoints
const csvEndpoint = "http://127.0.0.1:8080/uploadCSV";
const signalNameEndpoint = "http://127.0.0.1:8080/signalName";
const plotsEndpoint = "http://127.0.0.1:8080/plotsList";



// Event Listeners




// Enviar CSV al servidor
csvForm.addEventListener("submit", (e) => {
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
        // .then(console.log(signalList))
        .catch(err => console.log(err))
});

// Enviar nombre de señal seleccionada
signalMenu.addEventListener("submit", function (e) {
    e.preventDefault();
    let signalName = document.querySelector('input[name="signalName"]:checked').value;
    // console.log(JSON.stringify({ "signal_name": signalName }));
    fetch(signalNameEndpoint, {
        method: 'post',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "signal_name": signalName }),
    })
        .then(res => res.json())
        .then((data) => {
            console.log(data.signal_name);
            console.log(data.filename);
        })
        .catch(err => console.log(err))
})

signalMenu.addEventListener('change', function () {
    let signalName = document.querySelector('input[name="signalName"]:checked').value;
    console.log(signalName)
    fetch(signalNameEndpoint, {
        method: 'post',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "signal_name": signalName }),
    })
        .then(res => res.json())
        .then((data) => {
            console.log(data)
        })
        .catch(err => console.log(err))
})









// Enviar plots

plotsMenu.addEventListener('submit', function (e) {
    e.preventDefault();
    const plotsDict = {}
    for (let value of plotsMenu.getElementsByTagName('input')) {
        plotsDict[value.id] = value.checked
    }
    fetch(plotsEndpoint, {
        method: 'post',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(plotsDict)
    })
        .then(res => res.json())
        .then((data) => {
            console.log(data);
            imageCreator(data, "signal1")

        })
        .catch(err => console.log(err))
})








