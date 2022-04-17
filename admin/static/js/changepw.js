$(document).ready(function () {
    $('#changepw').click(function(){
        $('#changemypw').modal('show')
        
    })
    // change pw for new password
    $('#changepass').click(function(){

        if($("#newpw").is('input[type="password"]')){
            $('#newpw').prop('type', 'text')
            // change the eyes
            $('#eyechange').css("display", "none")
            $('#slashchange').css("display", "block")
        }
        else if($("#newpw").is('input[type="text"]')){
            $('#newpw').prop('type', 'password')
             // change the eyes
             $('#eyechange').css("display", "block")
             $('#slashchange').css("display", "none")
        }   
    })
    $('#confirmpass').click(function(){

        if($("#confirmpw").is('input[type="password"]')){
            $('#confirmpw').prop('type', 'text')
              // change the eyes
              $('#eyeconfirm').css("display", "none")
              $('#slashconfirm').css("display", "block")
        }
        else if($("#confirmpw").is('input[type="text"]')){
            $('#confirmpw').prop('type', 'password')
            // change the eyes
            $('#eyeconfirm').css("display", "block")
            $('#slashconfirm').css("display", "none")
        }
    })
    $('#savemypw').click(function () {
        console.log(1)
        var id = $('#current-id').val();
        var confirm = $('#confirmpw').val();
        var newpw = $('#newpw').val();
        if(confirm != newpw){
            $('#newpassAlert').text("your password doesn't match please check again").show();
        }
        else if(confirm =="" && newpw == ""){
            $('#newpassAlert').text("Please enter your new password").show();
        }
        else if(confirm==""|| newpw==""){
            $('#newpassAlert').text("Please input missing fields").show();
        }
        else{
            $.ajax({
                method:'POST',url:'/admin/api/silent/changepassword',
                data:{id:id, password:confirm},
                success:function (data) {
                    swal({
                        title: data.title,
                        text: data.msg,
                        icon: data.identfier,
                        button: "Ok",
                    })
                    .then(function(){
                        $('#changemypw').modal('hide');
                    })
                }
            })
        }
    })
})