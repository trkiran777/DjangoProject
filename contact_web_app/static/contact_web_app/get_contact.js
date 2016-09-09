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
/*
$(document).ready(function(){
    $("btn1").click(function () {
        var phone = $("#phone").val();
        if (phone == ""){
            $("#message").text('Required!').css("color", "red");
        }
        else if (/\b[7-9]([0-9]){9}\b/.test(phone)){
            $("#myForm").submit();
        }
        else {
            $("#message").text('Invalid!').css("color", "red");
        }
    });
});
*/
$(document).foundation({
    abide : {
        validate_on_blur : true,
        timeout : 500
    }
});