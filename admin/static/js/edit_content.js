$(document).ready(function () {
    $('#submit_button').click(function() {
    var id = $('#product_code').val();
    var category = $('#categories option:selected').text(); // this is to get the value name in the text
    var productname = $('#name').val();
    var price = $('#price').val();
    var qty = $('#quantity').val();
    if (category != "" && price != ""){
        swal({
            title: "Are you sure?",
            text: "Do you want to proceed to edit?",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes",
            closeOnConfirm: false
        }).then(function(){
            $.ajax({
            url : '/admin/api/products/product/edit/'+id,
            method : 'POST',
            data : {
                category:category,
                productname:productname,
                price:price,
                qty:qty
            },
            success:function(data){
                window.location.href = '/admin/products'
            }

        })
        })
    
    }
    })
})