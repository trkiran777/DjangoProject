/*
function getMessage(){
    provider = document.getElementById("provider").value;
    if (provider == 'select provider'){
        document.getElementById("message").innerHTML = 'Select a Provider!';
    }
    else {
        document.getElementById("myForm").submit();
    }
}
*/
$(document).ready(function(){
    $("#btn1").click(function(){
        var provider = $("#provider").val();
        if (provider == "select provider"){
            $("#message").text('Select a Provider!');
        }
        else{
            $("#myForm").submit();
        }
    });
});