function sign_up_event(user, event_id){
  console.log(event_id);
  var xhr = new XMLHttpRequest();
  var url = "/users/event_sign_up";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          console.log(xhr.responseText)

          // var element = document.getElementById("profile_update_form");
          // if (element.firstChild != good_update) 
          //     element.insertBefore(good_update, element.firstChild);

      } else if (xhr.status === 403) {

          // var element = document.getElementById("profile_update_form");
          // if (element.firstChild != bad_update) 
          //     element.insertBefore(bad_update, element.firstChild);

      }
  };
  if (user != 'AnonymousUser') {
      var data = JSON.stringify({"event_id": event_id});
      xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
      xhr.send(data);
  }
  return false;

}

function send_dicision(req_id, decision){
    console.log(decision);
    console.log(req_id);
    var xhr = new XMLHttpRequest();
    var url = "/users/join_requests";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText)
            document.getElementById('request'+req_id).remove()
            // var element = document.getElementById("profile_update_form");
            // if (element.firstChild != good_update) 
            //     element.insertBefore(good_update, element.firstChild);
  
        } else if (xhr.status === 403) {
  
            // var element = document.getElementById("profile_update_form");
            // if (element.firstChild != bad_update) 
            //     element.insertBefore(bad_update, element.firstChild);
  
        }
    };
    
    var data = JSON.stringify({"request_id": req_id, 'reg_status': decision });
    xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
    xhr.send(data);
    
    return false;
  
}


function remove_event(event_id, decision) {
    console.log(decision);
    console.log(event_id);
    var xhr = new XMLHttpRequest();
    var url = "/users/event_management";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText)
            document.getElementById('event'+event_id).remove()
            // var element = document.getElementById("profile_update_form");
            // if (element.firstChild != good_update) 
            //     element.insertBefore(good_update, element.firstChild);
  
        } else if (xhr.status === 403) {
  
            // var element = document.getElementById("profile_update_form");
            // if (element.firstChild != bad_update) 
            //     element.insertBefore(bad_update, element.firstChild);
  
        }
    };
    
    var data = JSON.stringify({"event_id": event_id, 'decision': decision });
    xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
    xhr.send(data);
    
    return false;
}