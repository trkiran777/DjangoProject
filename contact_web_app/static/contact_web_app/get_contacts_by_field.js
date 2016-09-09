/*
function getMessage(){
    field = document.getElementById("field").value;
    if (field == 'select a field'){
        document.getElementById("message").innerHTML = 'Select a Field!';
    }
    else {
        document.getElementById("myForm").submit();
    }
}
*/
$(document).ready(function(){
    $("#btn1").click(function(){
        var field = $("#field").val();
        if (field == "select a field"){
            $("#message").text('Select a Field!');
        }
        else{
            $("#myForm").submit();
        }
    });
});