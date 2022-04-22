// Uses only for the silent route 

/* composed for the infinity-flow 2022 */

$(document).ready(function(){

    // add modal
    $('#add_submit').click(function(){
        var username = $('#username').val();
        var email = $('#email').val();
        var raw_password = $('#password').val();
        var hash_password = $('#hash_password').val()
        if(raw_password != "" &&  hash_password != ""){
            $('#errorAlert2').text('Please remove the text either on password or hash password!').show();
        }
        else if(raw_password == "" &&  hash_password == ""){
            $('#errorAlert2').text('Please add password or hash password!').show();
        }
        else if(hash_password != ""){
            if(!hash_password.startsWith("sha256$")){
                $('#errorAlert2').text('Incorrect hash password, please check again').show();
            }
            else{add_user(username, email, raw_password, hash_password)}
        }
        // else if(!hash_password.startsWith("sha256$")){
        //     $('#errorAlert2').text('Incorrect hash password, please check again').show();
        // }
        else{
            add_user(username, email, raw_password, hash_password)
        }
        function add_user(username, email, raw_password, hash_password) {
            $.ajax({
                url : '/admin/api/silent/add',
                method : 'POST',
                data : {
                    username : username,
                    email : email,
                    raw_password : raw_password,
                    hash_password : hash_password
                },
                success:(function () {
                    swal({
                        title: "Yay!",
                        text: 'Success, the user has been added!',
                        icon: "success",
                        button: "Okay",
                      })
                      .then((data_success)=>{
                          location.reload()
                      })
                })
            })
        }
    })
    // edit modal
    $('.edit_btn').click(function(){
        window.id = $(this).closest('tr').find('.find_id').val(); 
        $.ajax({
            method:'POST',url:'/admin/api/silent/',data:{id:id},
            success:function (data) {
                console.log(data.email)
                $('#username2').val(data.username);
                $('#email2').val(data.email);
                // opens the modal
                $('#editmodal').modal('show');
                
            }
        })
    })
    $('#edit_submit').click(function () {
        var email =  $('#email2').val();
        var password =  $('#password2').val();
        var username =  $('#username2').val();
        if(email == "" && password=="" && username==""){
            $('#errorAlert3').text('Please input details!').show();
        }
        else if(password=="" || email =="" || username==""){
            $('#errorAlert3').text('Please input missing details').show();
        }
        else{
            $.ajax({
                method:'POST',url:'/admin/api/silent/edit',
                data:{
                    id:id, email:email, username:username, password:password
                },
                success:function (info) {
                    if(info.error){
                        swal({
                            title: info.title,
                            text: info.error,
                            icon: info.identfier,
                            button: "Okay",
                            })
                            .then((data_success)=>{
                                location.reload()
                            })
                    }
                    else{
                        swal({
                            title: info.title,
                            text: info.success,
                            icon: info.identfier,
                            button: "Okay",
                            })
                            .then((data_success)=>{
                                location.reload()
                            })
                    }
                }
            })
        }
    })
    //end
    $('.view_btn').click(function () {
        var view_id = $(this).closest('tr').find('.find_id').val(); 
        $.ajax({
            method:'POST',url:'/admin/api/silent/pw',data:{id:view_id},
            success:function (data) {
                $('#user_email').text(data.email)
                $('#view_pass').text(data.password)
                $('#viewmodal').modal('show')
            }
        })
    })
   
});