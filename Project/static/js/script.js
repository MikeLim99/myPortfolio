//scroll to top behavior
const toTop = document.querySelector(".to-top");

window.addEventListener('scroll', checkHeight)
function checkHeight(){
    if (window.scrollY > 100) {
        toTop.style.opacity = "1"
    } else {
        toTop.style.opacity = "0"

    }
}
