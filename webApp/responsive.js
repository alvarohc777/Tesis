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
// Borrar
document.getElementById("mainContent").style.marginLeft = "250px"