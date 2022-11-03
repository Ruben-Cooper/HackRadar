const currentPage = location.href;
const navItem = document.querySelectorAll('.navbar li a');
const navLength = navItem.length;

for(var i = 0; i < navLength; i++){
    if(navItem[i].href === currentPage){
        navItem[i].className = "active";
    }
    else if (navItem[i].href === "dropdown"){
    }
}