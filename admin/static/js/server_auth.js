$(document).ready(function() {
    $('.modalactivator').click(function () {
        window.id = $(this).closest('tr').find('.find_id').val(); 
        $('#deletemodal').modal('show');
    })

    // auth the user
    $('#deletebtn').click(function () {
        var email = $('#emailinput').val();
        var password = $('#passwordinput').val()
        if (email=="" && password==""){

        }
        $.ajax({
            method:'POST',url:'/admin/api/verify',
            data:{ id:id, email:email, password:password},
            success:function(data){
                $('#deletemodal').modal('hide');
                swal({
                    title: data.title,
                    text: data.info,
                    icon: data.identifier,
                    button: {cancel : 'Ok'},
                    })
                    .then((data_success)=>{
                        //location.reload()
                        if(data.identifier == 'success'){delete_transaction(id)}
                    })
            }
        })
    })
    // edit button
    $('.editactivator').click(function () {
        window.client_id = $(this).closest('tr').find('.find_id').val(); 
        var stats = send_id(client_id)
        $('#editmodal').modal('show')
        if(stats.status == 'Delivered'){
            $("label[for*='trans_status']").html(' Delivery Status: <span class="badge badge-pill badge-success"><i class="fas fa-check-circle"></i> Delivered at '+stats.time +'</span>');
            $('#trans_status').prop('disabled', true )
        }
        else{
            $("label[for*='status']").html('Delivery Status: ');
            $('#trans_status').prop('disabled', false )
            
        }
       
        
    })
    $('#submitedit').click(function () {
        new_status = $('#trans_status option:selected').val();
        if(new_status == 'Delivered'){
            swal({
                title: 'Are you Sure?',
                text: 'Once set to "Delivered" it cannot be edit easily',
                icon: 'warning',
                button: {cancel : 'Ok'},
            })
            .then((data_success)=>{
                send_newstatus(client_id, new_status)
            })
        }
        send_newstatus(client_id, new_status)

    })
    // edit all func
    $('#editall').click(function () {
        $('#editmodal').modal('hide');
        console.log(client_id)
        var edit_auth = auth(client_id)
        if(edit_auth == true){
            console.log('hdh')
        }
        console.log(edit_auth)
        
    })
   
    //delete function
    function delete_transaction(id){
        $.ajax({
            method: 'POST', url:'/admin/api/transaction/delete',
            data:{id:id},
            success:function () {
                location.reload()
            }
        })
    }
    function send_id(id){
        $.ajax({
            async :false,
            method:'POST',url:'/admin/api/transaction/edit',
            data:{id:id},
            success:function (data) {
                client_data = data
            
            }

        })
        return client_data
        
    }
    function send_newstatus(id, newstatus){
        $.ajax({
            method:'POST',url:'/admin/api/transaction/edit',
            data:{id:id, newstatus:newstatus},
            success:function () {
                swal({
                    title: 'Updated the Status',
                    text: 'Succefully updated the status',
                    icon: 'success',
                    button: {cancel : 'Ok'},
                })
                .then((data_success)=>{
                    location.reload()
                })
            
            }

        })
      
        
    }
    // use for authenticating request before submission
    function auth(id) {
        $('#authmodal').modal('show');
        
        $('#authbtn').click(function () {
            var email = $('#authemail').val();
            var password = $('#authpw').val();
            $.ajax({
                method:'POST',url:'/admin/api/verify',
                data:{ id:id, email:email, password:password},
                success:function(data){
                    window.auth_stat = 'success';
                    swal({
                        title: data.title,
                        text: data.info,
                        icon: data.identifier,
                        button: {cancel : 'Ok'},
                        })
                        .then((data_success)=>{
                            //location.reload()
                            if(data.identifier == 'success'){
                                
                                $('#authmodal').modal('hide');
                                
                            }
                        })
                }
            })
            return(auth_stat)
        })
    }
    
})