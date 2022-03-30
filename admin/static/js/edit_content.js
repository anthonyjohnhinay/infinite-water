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
    // catalog edit
    $('#submit_button_catalog').click(function(){
        var id = $('#catalog_code').val();
        var catalog_name = $('#catalog').val();
        if(catalog_name != ''){
            swal({
                title: "Are you sure?",
                text: "Do you want to proceed to edit? " + catalog_name,
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Yes",
                closeOnConfirm: false
            }).then(function(){
                $.ajax({
                    url: '/admin/api/products/catalog/edit/'+id,
                    method: 'POST',
                    data:{catalog : catalog_name },
                    success:(function(data) {
                        window.location.href = '/admin/products'
                    })
                })
            })
        }
        else{
            $('#errorAlert2').text('Please input text!').show();
        }
        
    })
    //end function
})