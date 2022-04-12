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
                        location.reload()
                    })
            }
        })
    })
})