$(document).ready(function(){
    $('#editsubmit').click(function(){
        var id = $('#clienttransid').val();
        var customername =  $('#optioncustomer').val();
        var  customeraddress = $('#address').val();
        var customercontact = $('#contact_number').val();
        var productcatalog = $('#categories option:selected').text();
        var productname = $('#productname option:selected').text();
        var productprice = $('#formprice').val();
        var deliverystatus = $('#status option:selected').val();
        var producttotal = $('#total_price').text()
        var producttotal = producttotal.replace('₱', '')
        var userbal = $('#balance').text()
        var userbal = userbal.replace('₱', '')
        var qty = $('#qty').val()

        if(producttotal == null){
            $('#errorAlert').text('Please input all the details!').show()
        }
        if(customername == ""){
         $('#errorAlert').text('Please input customer name').show()
        }
        else{
            swal({
                title: "Are you sure?",
                text: "Once submitted this cannot be undone",
                icon: "warning",
                buttons: true,
                allowOutsideClick: false,
                dangerMode: true,
              })
              .then((willsave)=>{
                if(willsave){
                    $.ajax({
                        url : '/admin/api/transaction/editsubmit',
                        method : 'POST',
                        data : {
                           id : id,
                           customername : customername,
                           customercontact : customercontact,
                           customeraddress :  customeraddress,
                           deliverystatus : deliverystatus,
                           productcatalog : productcatalog,
                           productname : productname,
                           productprice : productprice,
                           producttotal : producttotal,
                           userbal : userbal,
                           qty : qty
                        },
                        success:function(data){
                            if(data.error){
                              swal({
                                  title: "Something went wrong.",
                                  text: data.error,
                                  icon: "danger",
                                  button: "Okay",
                                }).then(function(){
                                    $('#exampleModal').modal('hide');
                                    return_default();
                                    location.reload();
                                })
                            }
                          swal({
                              title: "Yay!",
                              text: 'Transaction has been edited',
                              icon: "success",
                              button: "Okay",
                            }).then(function(){
                                $('#exampleModal').modal('hide');
                                return_default();
                                location.reload();
                            })
                        }
  
                        //end
                    })
                }
              })
        }

    });
    // this will reset any modificatiosn from the edit func
    $('.reset').click(function(){
        return_default()
    })
    //
    function return_default(){
        $('#optioncustomer').val('');
        $('#qty').val('');
        $('#formprice').val();
        $('#contact_number').val('');
        $('#address').val('');
        // back to default
        $('#submitdata').show();
        $('#editsubmit').hide();
        $('#zoomwarn').hide()

        $('#regcustom').show();
        $('#customertypediv').show()

        $('#guestcustom').hide()
        $('#customertype').prop('disabled', false)
        $('#guestcustom').prop('class', 'form-group col-md-4')
        $('#usercontactnum').prop('class', 'form-group col-md-4')
        $('#exampleModalLabel').text('Add Transaction')
    }
})