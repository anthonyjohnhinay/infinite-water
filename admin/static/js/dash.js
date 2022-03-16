$(document).ready(function(){


    $('#modal_submit').click(function(){
        var username = $('#username').val();
        var email = $('#active_email').val();
        var role = $('#role').val();
        if(username != '' && email != ''){
            $.ajax({
                url: '/admin/users',
                method: 'POST',
                data:{
                    username:username,
                    email:email,
                    role:role
                },
                success:function(data) {
                    $('#modal').modal('hide');
                }
            });
        }
      
      
    });
    
});