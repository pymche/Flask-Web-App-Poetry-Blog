$(document).ready(function(){

    $(".hamburger").on("click", function(event){

        $("nav ul").toggleClass("open");
        event.preventDefault();

    });

});

// whenever click on hamburger, give the "nav ul" a class of 'open',
// Or take it away if it already has that class