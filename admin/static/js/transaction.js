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
        var price = $('#product_val option:selected').val();
        var total = (qty * price)
        $('#total_price').text('₱' + total);
    })
})