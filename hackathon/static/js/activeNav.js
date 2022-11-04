const currentPage = location.href;
const navItem = document.querySelectorAll(".navbar ul a");
const navLength = navItem.length;

for(var i = 0; i < navLength; i++){
    if(navItem[i].href === currentPage){
        navItem[i].className = "active";
    }
}