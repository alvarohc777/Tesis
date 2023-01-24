let sidebarState = 0;
const csvInput = document.getElementById("csvInput")
const reader = new FileReader()


// Funcionalidad

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