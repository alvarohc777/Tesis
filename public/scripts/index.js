const sidebar = document.getElementById("sidebar")
let sidebarState = sidebar.dataset.state
console.log(sidebarState)
function toogleNav() {
    if (sidebarState === "closed") {
        sidebar.style.width = "250px";
        document.getElementById("openbtn").innerHTML = "x";
        sidebarState = "open"
    } else {
        sidebar.style.width = "0";
        document.getElementById("openbtn").innerHTML = "&#9002;&#9002;&#9002;";
        sidebarState = "closed"
    }
}

sidebar.style.width = "250px";