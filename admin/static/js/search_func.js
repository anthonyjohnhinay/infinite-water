/* https://www.w3schools.com/jquery/jquery_filters.asp */

$(document).ready(function () {
    
    // search function for transaction
    $('#transacinput').keyup(function () {
        var value = $(this).val().toLowerCase();
        $('#transactable tr').filter(function(){
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        })
    })
<<<<<<< HEAD
=======

    // search function for user
    $('#user_search').keyup(function () {
        var value = $(this).val().toLowerCase();
        $('#user_table tr').filter(function(){
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        })
    })
>>>>>>> b5644c32c44cb041c77e04bab75d4cac8e81a62e
})