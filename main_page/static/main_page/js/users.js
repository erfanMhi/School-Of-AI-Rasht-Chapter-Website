
var good_register_el = document.createElement("p");
var good_register_node = document.createTextNode("You're registered, you can login now.");
good_register_el.appendChild(good_register_node);

var bad_register_el = document.createElement("p");
var bad_register_node = document.createTextNode("Some of input values are not valid.");
bad_register_el.appendChild(bad_register_node);

function signup_send() {
    var xhr = new XMLHttpRequest();
    var url = "/users/signup";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText)
            addLogin()

            var element = document.getElementById("login-form");
            if (element.firstChild != good_register_el) 
                element.insertBefore(good_register_el, element.firstChild);

        } else if (xhr.status === 403) {

            var element = document.getElementById("register-form");
            if (element.firstChild != bad_register_el) 
                element.insertBefore(bad_register_el, element.firstChild);

        }
    };

    var data = JSON.stringify({"username": document.getElementById('username_register').value,
                               "password": document.getElementById('password_register').value,
                               "email": document.getElementById('emailaddress_register').value,
                               "fullname": document.getElementById('fullname_register').value
                                });
    xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))
    xhr.send(data);
    return false;
}


var good_update = document.createElement("p");
var good_update_node = document.createTextNode("Information Updated Successfully.");
good_update.appendChild(good_update_node);

var bad_update = document.createElement("p");
var bad_update_node = document.createTextNode("Information Updated UnSuccessfully -_-");
bad_update.appendChild(bad_update_node);


function profile_update() {
    var xhr = new XMLHttpRequest();
    var url = "/users/profile";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText)

            var element = document.getElementById("profile_update_form");
            if (element.firstChild != good_update) 
                element.insertBefore(good_update, element.firstChild);

        } else if (xhr.status === 403) {

            var element = document.getElementById("profile_update_form");
            if (element.firstChild != bad_update) 
                element.insertBefore(bad_update, element.firstChild);

        }
    };

    var data = JSON.stringify({"province": document.getElementById('province').value,
                               "city": document.getElementById('city').value,
                               "mobile": document.getElementById('mobile').value,
                               "email": document.getElementById('email').value,
                               "fullname": document.getElementById('full_name').value,
                               "birthdate": document.getElementById('birthdate').value
                                });
    xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))
    xhr.send(data);
    return false;
}


function upload_profile_pic(){
    var formData = new FormData(),
    file = document.getElementById('pro_pic').files[0],
    xhr = new XMLHttpRequest();
    
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText)
            console.log(xhr.responseText)
            JSON.parse(xhr.responseText)
            json = JSON.parse(xhr.responseText)
            document.getElementById("main_pro_pic").src= json['photo_url'];
            document.getElementById("nav_pro_pic").src= json['photo_url'];
            console.log("fuck Love you")

        } else if (xhr.status === 403) {

            console.log("fuck you")

        }
    };
    formData.append('file', file);
    xhr.open('POST', '/users/profile_photo');
    xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))
    xhr.send(formData);
}

