$(document).ready(function(){
    var previousScroll = 0;
    $(window).scroll(function () {
        var currentScroll = $(this).scrollTop();
        if (currentScroll < 60) { //if less than 60px show navbar
            $('nav').removeClass('black');
        } else if (currentScroll > 0 && currentScroll < $(document).height() - $(window).height()) {  
            if (currentScroll > previousScroll) { // if scrolled down
                $('nav').fadeOut(1000).removeClass('black');
            } else { 
                $('nav').fadeIn(750).addClass('black');
            }7
            previousScroll = currentScroll;
        }
    });
    // Make nav bg black when button is click
    $(".navbar-toggler").click(function() {
        $("nav").toggleClass("toggle-background");
    });
});  