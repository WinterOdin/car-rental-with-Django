
    $('.clickFaq').click(function() {
    $('.displayFaq').toggle('1000');
    $("i", this).toggleClass("fa-arrow-circle-up fa-arrow-circle-down ");
});


$(".open").hide();
$('.questionUs').click(function(){
    $(this).next().slideToggle();
});


$(document).ready(function($) {
    $(".scroll").click(function(event){     
        event.preventDefault();
        $('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);
    });
});
