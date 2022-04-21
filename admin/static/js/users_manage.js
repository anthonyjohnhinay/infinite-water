$(document).ready(function(){
    $('.reset_pw').click(function(){
      var id = $(this).closest('tr').find('.reset_id').val(); // finds what users click in table
      swal({
        title: "Holdup!",
        text: "Once password reset this will affect the user",
        icon: "warning",
        buttons: true,
        allowOutsideClick: false,
        dangerMode: true,
      })
      .then((willreset) =>{
        if(willreset){
          $('#loader').modal('show')
          $.ajax({
            url: '/admin/api/users/users/sudo',
            method: 'POST',
            data: {id : id},
            success: (function(data){
              $('#loader').modal('hide')
              if(data.identifier == 'success'){
                $('#useremail').text(data.email);
                $('#newpw').text(data.pw);
                $('#exampleModal').modal('show');
              }
              else{
                swal({
                  title: "Oops!",
                  text: data.error,
                  icon: "error",
                  button: "Okay",
                });
                }
            })
            // ajax success request
          })
        }
      }) 

    })
  })