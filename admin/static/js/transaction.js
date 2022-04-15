$(document).ready(function(){
    $('selectpicker').selectpicker();

    // function bool
    $('#customertype').on('change', function (e) {
        var type = $('#customertype option:selected').val();
        // Guest customers 
        if(type == 'guest'){ 
            $('#regcustom').hide();
            $('#guestcustom').show();
            $('#contact_number').val('');
            $('#address').val('');
            $('#markers').val('');
        }
        // regular customer
        else{
            $('#regcustom').show();
            $('#guestcustom').hide();
            // the value
            $('#customername').change(function () {
                var selectedItem = $('#customername option:selected').text();
                // send an ajax request for getting other details
                $.ajax({
                    url: '/admin/api/transaction/request',
                    method: 'POST',
                    data : {customer : selectedItem},
                    success:function(data){
                        $('#contact_number').val(data.contact);
                        $('#address').val(data.address);
                        $('#markers').val(data.markers);
                    }
                })
            });
        }
        

    })
   $('#categories').change(function(){
        $.ajax({
            url: '/admin/api/transaction/fetch_product',
            method: 'POST',
            data: {categories : $('#categories option:selected').text()},
            success : function(data){
                $('#product_drop').html(data);
                $('#product_drop').append(data.response)
                $('#qty').prop('disabled', false);
            }
        })
   })
    //end func
    $('#qty').keyup(function(){
        var qty = $('#qty').val();
        var price = $('#productname option:selected').val();
        window.total = (qty * price)
        $('#total_price').text('₱' + total);
    })
    $('#formprice').keyup(function(){
        window.payment = $('#formprice').val();
        window.balance = (payment - window.total);
        if(0>balance){
            $('#balance').css('color', 'red')
        }
        else{
            $('#balance').css('color', 'black')
        }
        $('#balance').text('₱' + balance);

    })
    $('#submitdata').click(function(){
        // list of datas 
        // getting the value for the customer since it has two classes, already know and not.
        if($('#optioncustomer').val()==""){ var customername = $('#regcustom option:selected').text();}
        else{var customername = $('#optioncustomer').val(); }

        const customeraddress = $('#address').val();
        var customercontact = $('#contact_number').val();
        var customermarkers = $('#markers').val();
        var productcatalog = $('#categories option:selected').text();
        var productname = $('#productname option:selected').text();
        var productprice = $('#productname option:selected').val();
        var deliverystatus = $('#status option:selected').val();
        var producttotal = window.total;
        var userbal = window.balance
        var qty = $('#qty').val()
        //end
       if(window.total == null){
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
                      url : '/admin/api/transaction/fetch_transaction',
                      method : 'POST',
                      data : {
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
                        swal({
                            title: "Yay!",
                            text: 'Transaction has been added',
                            icon: "success",
                            button: "Okay",
                          }).then(function(){
                              $('#exampleModal').modal('hide');
                              location.reload();
                          })
                      }

                      //end
                  })
              }
          })
       }
    })
    //
})