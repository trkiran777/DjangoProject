/*
function getMessage(){
    phone = document.getElementById("phone").value;
    if (phone == ""){
        document.getElementById("message").innerHTML = 'Required!';
    }
    else if (/\b[7-9]([0-9]){9}\b/.test(phone)){
        document.getElementById("myForm").submit();
    }
    else {
        document.getElementById("message").innerHTML = 'Invalid!';
    }
}
*/
$(document).ready(function(){
    $("#btn1").click(function(){
        var phone = $("#phone").val();
        if (phone == ""){
            $("#message").text('Required!').css("color", "red");
        }
        else if (/\b[7-9]([0-9]){9}\b/.test(phone)){
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
            $.post("delete_contact",
             { phone_no : phone},
             function(data){
                 if (data == "login first!") {
                     $("#AccountModel").foundation("reveal", "open");
                 }
                 else {
                     $("#message").text(data).css("color", "green");
                 }
             }
            );
        }
        else {
            $("#message").text('Invalid!').css("color", "red");
        }
    });

    $("#myForm2").on('valid.fndtn.abide', function() {
        var name = $("#signup-name").val();
        var email = $("#signup-email").val();
        var phone = $("#signup-phoneNumber").val();
        var password = $("#signup-password").val();
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
        $.post("add_user",
            { name : name, email : email, phone_no : phone, password : password},
            function(data){
                $("#message2").text(data).css("color", "red");
            }
        );
    });

    $("#myForm1").on('valid.fndtn.abide', function() {
        var email = $("#login-email").val();
        var password = $("#login-password").val();
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
        $.post("login",
            {email: email, password: password},
            function (data) {
                if(data == "login success"){
                    $("#AccountModel").foundation("reveal", "close");
                    $("#btn1").trigger("click");
                }
                else {
                    $("#message1").text(data).css("color", "red");
                }
            }
        );
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