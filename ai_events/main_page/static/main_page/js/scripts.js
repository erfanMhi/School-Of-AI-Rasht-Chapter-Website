
// Toggling between login and sign up
document.getElementById("login-bt").addEventListener("click", addRegister);
document.getElementById("register-bt").addEventListener("click", addLogin);
function addRegister() {
    removeClass(document.getElementById("register-form"), 'not-show')
    addClass(document.getElementById("login-form"), 'not-show')
}

function addLogin() {
    addClass(document.getElementById("register-form"), 'not-show')
    removeClass(document.getElementById("login-form"), 'not-show')
}



// document.getElementById("login-button").addEventListener("click", addLoginPage);
// document.getElementById("register-button").addEventListener("click", addRegisterPage);
// document.getElementById("register-bt-2").addEventListener("click", addRegisterPage);


document.getElementById('login-register-close-bt').addEventListener("click", removeFormContainer);

function addLoginPage() {
    addFormContainer()
    addLogin()
}
function addRegisterPage() {
    addRegister()
    addFormContainer()
}

function addFormContainer() {
    removeClass(document.getElementById("login-signup-container"), 'not-show')
    addClass(document.getElementById("login-signup-container"), 'flex-container')
}

function removeFormContainer() {
    addClass(document.getElementById("login-signup-container"), 'not-show')
    removeClass(document.getElementById("login-signup-container"), 'flex-container')
}


function hover(element, others=false) {
    if (others) 
        element.setAttribute('src', '../resources/imgs/soa_logo_2.svg');
    else
        element.setAttribute('src', './resources/imgs/soa_logo_2.svg');
}

function unhover(element, others=false) {
    if (others)
        element.setAttribute('src', '../resources/imgs/soa_logo_3.svg');
    else
        element.setAttribute('src', './resources/imgs/soa_logo.svg');

}