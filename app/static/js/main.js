/**
 * Created by lidad on 2018/10/9.
 */



function onResize() {
    if($("body").width() < 900){
        $(".brand-logo").css("display", "none");
    }else{
        $(".brand-logo").css("display", "block");
    }
    switch (true) {
        
        case $("body").width() >= 1200:
            
            $(".brand-logo").css("margin-right", ($("body").width() - 1200) + "px");
            break;
        case $("body").width() < 1200:

            $(".brand-logo").css("margin-right", "10px");
            break;
        default:
            break;
    }
}
$(document).ready(
    function () {
        onResize();
        $(".sidenav").sidenav();
        $('.collapsible').collapsible();
        $(".dropdown-trigger").dropdown({
            hover: true
        });
        $('.carousel.carousel-slider').carousel({
            fullWidth: true,
            indicators: true
        });
        $('select').formSelect();
        //Materialize.updateTextFields();
        $('#search_btn').click(function (e) {
            window.location.href = '/cn/search?q=' + $('#search').val();
        })
        $('#clean_search').click(function (e) {
            $('#search').val("");
        })
        // index
        try {
            var carouselHeight = document.querySelector("body > div:nth-child(3) > div.carousel.carousel-slider > div > img").height;
            $(".carousel").css("height", carouselHeight + "px");
        } catch (error) {

        }
        //post
        try {
            $(".post-content").children().addClass("browser-default");
        } catch (error) {

        }

        window.onresize = function () {
            onResize();
        }

    }

);