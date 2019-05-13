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
        //Materialize.updateTextFields();
        $('#search_btn').click(function(e){
            window.location.href='/cn/search?q='+$('#search').val();
        })
        $('#clean_search').click(function(e){
            $('#search').val("");
        })
    }

);