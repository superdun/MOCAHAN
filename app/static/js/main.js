/**
 * Created by lidad on 2018/10/9.
 */
$(document).ready(
    function () {
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
        Materialize.updateTextFields();
    }

);