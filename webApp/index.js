let sidebarState = 0;
var signalList
const csvInput = document.getElementById("csvInput");
const csvForm = document.getElementById("csvForm");
const signalMenu = document.getElementById("signalMenu");
const reader = new FileReader();
const csvEndpoint = "http://127.0.0.1:8080/uploadCSV";


//                                  Funcionalidad

// Cargue de datos

function selectCSV() {
    document.getElementById("csvInput").click();
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
    formData.append('file_type', 'CSV')

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
    let arrayLength = list.length;
    for (let i = 0; i < arrayLength; i++) {
        console.log(signalList[i])
        let radiobox = document.createElement('input');


        radiobox.type = 'radio';
        radiobox.id = list[i];
        radiobox.name = 'email';

        let label = document.createElement('label');
        label.htmlFor = list[i];
        label.textContent = list[i];
        signalMenu.appendChild(radiobox);
        signalMenu.appendChild(label);
        signalMenu.appendChild(document.createElement('BR'));
    }
    let btn = document.createElement("button");
    btn.type = 'submit';
    btn.textContent = "Load Plots";
    signalMenu.appendChild(btn);
}


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