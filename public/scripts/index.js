// API endpoints
const csvEndpoint = "http://127.0.0.1:8080/uploadCSV";
const signalNameEndpoint = "http://127.0.0.1:8080/signalName";
const plotsEndpoint = "http://127.0.0.1:8080/plotsList";

// Variables


// Constants
const reader = new FileReader();
const csvForm = document.getElementById("csvForm");
const csvInput = document.getElementById("csvInput");

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
})
