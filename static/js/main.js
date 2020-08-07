$(document).ready(function() {
    var amountScrolled = 300;
    highlightDay();

    $(window).scroll(function() {
        if ($(window).scrollTop() > amountScrolled) {
            $('a.back-to-top').fadeIn('slow');
        } else {
            $('a.back-to-top').fadeOut('slow');
        }
    });
    $('a.back-to-top').click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 700);
        return false;
    });

    initMap();

    $('.navbar-nav>li>a').on('click', function(){
            $('.navbar-collapse').collapse('hide');
    });

    //$(window).on('hashchange', function() {
    //    scrollToAnchor(window.location.hash.substring(1));
    //});
});

function initMap() {
    var pizzaria = {lat: -29.666314, lng: -51.167436};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: pizzaria
    });
    var marker = new google.maps.Marker({
        position: pizzaria,
        map: map
    });
}

function highlightDay() {
    var date = new Date();
    var tr = $('#'+date.getDay());
    tr.css('color', 'red');

}

function scrollToAnchor(id){
    var dataAnchor = $("div[data-anchor='"+ id +"']");
    $('html,body').animate({scrollTop: dataAnchor.offset().top - 150},'slow');
}
