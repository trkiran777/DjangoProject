/*
function getMessage(){
    name = document.getElementById("ip1").value;
    phone = document.getElementById("ip2").value;
    email = document.getElementById("ip3").value;
    pin = document.getElementById("ip7").value;
    if (name == "" || phone == ""){
        document.getElementById("message").innerHTML = 'Name and Phone number are required!';
    }
    else if (/\b[7-9]([0-9]){9}\b/.test(phone) == false){
        document.getElementById("message").innerHTML = 'Invalid phone number!';
    }
    else if (email != "" && /\b[a-zA-Z0-9]+[@][a-zA-Z0-9]+[.][a-zA-Z]+\b/.test(email) == false){
        document.getElementById("message").innerHTML = 'Invalid email format!';
    }
    else if (pin != "" && /\b[0-9]{6}\b/.test(pin) == false){
        document.getElementById("message").innerHTML = 'Invalid pin-code!';
    }
    else {
        document.getElementById("myForm").submit();
    }
}
*/
$(document).ready(function(){
    $("#btn1").click(function(){
        var name = $("#ip1").val();
        var phone = $("#ip2").val();
        var email = $("#ip3").val();
        var street = $("#ip4").val();
        var city = $("#ip5").val();
        var state = $("#ip6").val();
        var pin = $("#ip7").val();
        if (name == "" || phone == ""){
            $("#message").text('Name and Phone number are required!').css("color", "red");
        }
        else if (/\b[7-9]([0-9]){9}\b/.test(phone) == false){
            $("#message").text('Invalid phone number!').css("color", "red");
        }
        else if (email != "" && /\b[a-zA-Z0-9]+[@][a-zA-Z0-9]+[.][a-zA-Z]+\b/.test(email) == false){
            $("#message").text('Invalid email format!').css("color", "red");
        }
        else if (pin != "" && /\b[0-9]{6}\b/.test(pin) == false){
            $("#message").text('Invalid pin-code!').css("color", "red");
        }
        else{
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            var csrftoken = getCookie('csrftoken');
            $.ajaxSetup({
                beforeSend: function(xhr) {
                    if (!this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
            $.post("modify_contact",
             { name : name, phone_no : phone, email : email, street : street, city : city,
             state : state, pin_code : pin},
             function(data){
                 $("#message").text(data).css("color", "green");
             }
            );
        }
    });
});
/*
$(document).foundation({
    abide : {
        validate_on_blur : true,
        timeout : 500
    }
});
*/
