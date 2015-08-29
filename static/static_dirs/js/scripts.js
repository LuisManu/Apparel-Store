
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

