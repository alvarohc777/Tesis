let sidebarState = 0;


function openNav() {
    if (sidebarState === 0) {
        document.getElementById("mySidebar").style.width = "250px";
        document.getElementById("mainContent").style.marginLeft = "250px"
        document.getElementById("footer").style.marginLeft = "250px";
        sidebarState = 1;
    } else {

        document.getElementById("mySidebar").style.width = "0";;
        document.getElementById("mainContent").style.marginLeft = "0";
        document.getElementById("footer").style.marginLeft = "0";
        sidebarState = 0;
    }
}

function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("mainContent").style.marginLeft = "0"
    document.getElementById("footer").style.marginLeft = "0"

}