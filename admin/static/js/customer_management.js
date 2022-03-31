$(document).ready(function () {
    $('#modal_submit').click(function () {
        var customer_name = $('#name').val();
        var address = $('#address').val();
        var contact_num = $('#contact_number').val();
        var marker = $('#markers').val();
        if (customer_name !=''){
            $.ajax({
                url: '/admin/api/customers/add',
                method:'POST',
                data:{
                    customer: customer_name,
                    address:address,
                    contact_num:contact_num,
                    marker:marker
                },
                success:function(data) {
                    if(data.error){
                        $('#errorAlert').text(data.error).show();
                    }
                    else{
                        $('#addcustomers').modal('hide');
                        location.reload();
                    }
                }
            })
        }
    })
    // new func
})