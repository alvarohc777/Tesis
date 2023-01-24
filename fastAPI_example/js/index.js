var CSVFile
var api_prueba
var signalList
const reader = new FileReader()

const myForm = document.getElementById("csvForm");
const csvInput = document.getElementById("csvInput");

myForm.addEventListener("submit", e => {
    e.preventDefault();
    const endpoint = "http://127.0.0.1:443/uploadCSV";
    // const endpoint = "http://httpbin.org/post";
    const formData = new FormData();


    // console.log(csvInput.files);
    // console.log(csvInput.files[0]);
    formData.append('csv_files', csvInput.files[0])
    formData.append('nombre', 'Alvaro')

    fetch(endpoint, {
        method: 'post',
        body: formData
    })
        .then(res => res.json())
        .then((data) => {
            signalList = data;
            console.log(signalList.signal_list);
            signalListAppend(signalList.signal_list)
        })
        .then(console.log(signalList))
        .catch(err => console.log(err))
});

function signalListAppend(signalList) {
    let signalsList = document.getElementById('signalsList');
    // sequential loop
    let arrayLength = signalList.length;
    for (var i = 0; i < arrayLength; i++) {
        let li = document.createElement('li');
        li.appendChild(document.createTextNode(signalList[i]));
        li.setAttribute('id', signalList[i])
        signalsList.appendChild(li);

    };
    // let li = document.createElement('li');

    // li.appendChild(document.createTextNode(signalList[22]));
    // li.setAttribute('id', 'prueba_lista');
    // signalsList.appendChild(li);
    // console.log("Terminó signalListAppend")
}

$.ajax({
    url: "http://127.0.0.1:443/info/2",
    type: 'GET',
    dataType: 'json',
    success: function (data) {
        console.log(data);
    }
})

$("#csvInput").on("input", function (e) {
    console.log("se cargó el archivo: " + $(this).val());
    let file = this.files[0]
    // console.log(e.type) --> devuelve input
    reader.onload = event => console.log(event.target.result);
    reader.onerror = error => console.log(error);
    reader.readAsText(file)
    CSVFile = file
    // console.log($('#CSVInput')[0].files[0])
});
// $("#CSVUpload").on("click", function () {
//     // var fd = new FormData();
//     // fd.append('file', CSVFile)
//     $.ajax({
//         url: "http://127.0.0.1:443/uploadCSV",
//         type: 'POST',
//         data: JSON.stringify({ 'id': 'alvaro' }),
//         dataType: 'json',
//         processData: false,
//         contentType: 'application/json',
//         // contentType: false,
//         success: function (data) {
//             console.log(data);
//         }
//     })
// })

$('#LoadCSV').on("click", function () {
    $.ajax({
        url: "http://127.0.0.1:443/signal_list",
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            console.log(data)
        }
    })
})

$('#CSVInput').on('Change', function () {
    console.log(this.val)
})