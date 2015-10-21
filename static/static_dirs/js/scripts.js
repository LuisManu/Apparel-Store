
$(document).ready(function(){




// ---------------------------------------
// scripts for mobile menu
// ---------------------------------------




    // ------------------------------------
    // slides in slider for mobile menu
    // ------------------------------------
    $('.glyphicon-menu-hamburger').click(function(){
        var hidden = $('.slide-in');
        if (hidden.hasClass('visible'))
        {
            hidden.animate({"left":"-1500px"}, "slow").removeClass('visible');
        }
        else
        {
            hidden.animate({"left":"0px"}, "slow").addClass('visible');
        }
        $(this).toggleClass('glyphicon-menu-hamburger glyphicon-remove');
        $(this).toggleClass('active-m');
        $('.hamburger').toggleClass('active-m');
    });




    // -----------------------------------------------------------------
    // slider category dropdown 
    // -----------------------------------------------------------------

    $('#womens-btn').click(function() {
        $(this).toggleClass('active-m');
        $('#womens-cats').toggleClass('hidden');
        $('.womens-arrow').toggleClass('glyphicon-chevron-down glyphicon-chevron-up');
    });


    $('#mens-btn').click(function() {
        $(this).toggleClass('active-m');
        $('#mens-cats').toggleClass('hidden');
        $('.mens-arrow').toggleClass('glyphicon-chevron-down glyphicon-chevron-up');
    });

    $('#kids-btn').click(function() {
        $(this).toggleClass('active-m');
        $('#kids-cats').toggleClass('hidden');
        $('.kids-arrow').toggleClass('glyphicon-chevron-down glyphicon-chevron-up');
    });





    // -------------------------------------------------------------
    // Toggle search bar on larger screens
    // --------------------------------------------------------------
    $('#search').click(function () {
        $('.search-bar-desktop').toggleClass('hidden');
        $(this).toggleClass('#search hidden');
    });



// ---------------------------------------------------------------
// testing navbar dropdown on scroll up
// ---------------------------------------------------------------


// Hide Header on on scroll down
var didScroll;
var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('header').outerHeight();

$(window).scroll(function(event){
    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

function hasScrolled() {
    var st = $(this).scrollTop();
    
    // Make sure they scroll more than delta
    if(Math.abs(lastScrollTop - st) <= delta)
        return;
    
    // If they scrolled down and are past the navbar, add class .nav-up.
    // This is necessary so you never see what is "behind" the navbar.
    if (st > lastScrollTop && st > navbarHeight){
        // Scroll Down
        $('header').removeClass('nav-down').addClass('nav-up');
    } else {
        // Scroll Up
        if(st + $(window).height() < $(document).height()) {
            $('header').removeClass('nav-up').addClass('nav-down');
        }
    }
    
    lastScrollTop = st;
}




});








// ------------------------------------------------------
//  SCRIPT FOR LIKE BUTTON
// ------------------------------------------------------

$('.like').click(function(){
    var productid;
    productid = $(this).attr("data-productid");


    var counter = $('#like_count').attr('data-counter');

    console.log(counter);
    // var root = 'http://localhost:8000/apparel/5.json';

    // var foo = $('#like_count').val();
    // console.log(foo);

    $.getJSON('/like_product/', {product_id: productid},  function(data)
        {
            var user_likes = data['user_likes'];
            var likes_counter = data['likes_counter'];
            // for (x in user_likes) {
            //     console.log(x);
            // };
            console.log(likes_counter);
            $('#user_likes').html(user_likes);
            $('#like_count').html(likes_counter);


            // var id = data['id'];
            // var title = data['title'];
            // var brand = data['brand'];
            // var category = data['category'];
            // var department = data['department'];
            // var image = data['image'];

            // $("#demo").append(
            //     "<p><h3>" + id + "</h3></p>" +
            //     "<p><h1>" + title + "</h1></p>" +
            //     "<p>" + brand + "</p>" +
            //     "<p>" + category.name + "</p>" +
            //     "<p>" + department.name + "</p>" +
            //     "<p>" + "<img src=" + image + "></p>"
            // );  
        }
    );









    // $.get('/like_product/', {product_id: productid}, function(data){
    //     $('#like_count').html(data);
    //     // $('#add').html('data sent sent');
    //     console.log(data);
    // });



});