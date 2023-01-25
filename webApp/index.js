let sidebarState = 0;
var signalList
const csvInput = document.getElementById("csvInput");
const csvForm = document.getElementById("csvForm");
const plotsMenu = document.getElementById("plotsMenu")
const signalMenu = document.getElementById("signalMenu");
const signalListBtn = document.getElementById("signalListBtn");
const reader = new FileReader();
const csvEndpoint = "http://127.0.0.1:8080/uploadCSV";
const signalNameEndpoint = "http://127.0.0.1:8080/signalName";


//                                  Funcionalidad

// Cargue de datos

function selectCSV() {
    csvInput.click();
}

function submitSignal() {
    signalMenu.getElementsByTagName('button')[0].click();
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
        if (i === 0) {
            radiobox.checked = true;
        }


        let label = document.createElement('label');
        label.htmlFor = list[i];
        label.textContent = list[i];

        // Append elements to signalMenu
        signalMenu.appendChild(radiobox);
        signalMenu.appendChild(label);
        signalMenu.appendChild(document.createElement('BR'));
    }
}

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

// Enviar plots

plotsMenu.addEventListener('submit', function (e) {
    e.preventDefault();
    console.log("hola")

})




// Estética
function openNav() {
    if (sidebarState === 0) {
        document.getElementById("mySidebar").style.width = "250px";
        document.getElementById("mainContent").style.marginLeft = "250px"
        document.getElementById("footer").style.marginLeft = "250px";
        document.getElementsByClassName("openbtn")[0].innerHTML = "x";
        sidebarState = 1;
    } else {

        document.getElementById("mySidebar").style.width = "0";;
        document.getElementById("mainContent").style.marginLeft = "0";
        document.getElementById("footer").style.marginLeft = "0";
        document.getElementsByClassName("openbtn")[0].innerHTML = "&#9002;&#9002;&#9002;";
        sidebarState = 0;
    }
}