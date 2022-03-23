$(document).ready(function(){


    $('#modal_submit').click(function(){
        var username = $('#catalog').val();
        if(username != ''){
            $.ajax({
                url: "/admin/api/products/catalogs",
                method: 'POST',
                data:{
                    catalogs:username,
                },
                success:function(data) {
                    if(data.error){
                        $('#errorAlert').text(data.error).show();
				        $('#successAlert').hide();
                    }
                    else{
                        
				        $('#errorAlert').hide();
                        $('#exampleModal').modal('hide');
                        location.reload();      // this will set reload after the success
                    
                        
                    }
                }
            });
        }
        
      
    });
    // new function for the select
    $('#categories').on('change' , function(event){ // it detects what the on select option then send post request to the backend
        var product = $('#categories').val();
        $.ajax({
            url:"/admin/api/products/add",
            method:"POST",
            data: {product: product},
            success:function(data){
                console.log(product)
            }
        })
    });
    
    // function for the the adding products
    $('#modal_submit2').click(function(){
        var selectprod = $('#categories').val();
        var productname = $('#productname').val();
        var price = $('#price').val();
        var qty = $('#qty').val();
        if(productname != '' && price !=""){
            $.ajax({
                url: "/admin/api/products/add",
                method: 'POST',
                data:{
                    selectprod : selectprod,
                    productname : productname,
                    price : price,
                    qty : qty

                },
                success:function(data) {
                    if(data.error){
                        $('#errorAlert').text(data.error).show();
				        $('#successAlert').hide();
                    }
                    else{
                        
				        $('#errorAlert').hide();
                        $('#exampleModal').modal('hide');
                        location.reload();      // this will set reload after the success
                    
                        
                    }
                }
            });
        }
        
      
    });
    
    
});