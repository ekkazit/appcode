(function ($) {
  // wow
  new WOW().init();

  // affix
  var $nav = $('#nav');
  $nav.affix({
    offset: {top: 150}
  });

  // scrollup
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('.scrollup').fadeIn();
    } else {
      $('.scrollup').fadeOut();
    }
  });

  $('.scrollup').click(function () {
    $('html, body').animate({scrollTop: 0}, 1000);
    return false;
  });

  // animate
  function doAnimations(elems) {
    var animEndEv = 'webkitAnimationEnd animationend';

    elems.each(function () {
      var $this = $(this),
        $animationType = $this.data('animation');
      $this.addClass($animationType).one(animEndEv, function () {
        $this.removeClass($animationType);
      });
    });
  }

  // carousel
  var $myCarousel = $('#carousel-example-generic'),
    $firstAnimatingElems = $myCarousel.find('.item:first').find("[data-animation^='animated']");

  $myCarousel.carousel();

  doAnimations($firstAnimatingElems);

  $myCarousel.on('slide.bs.carousel', function (e) {
    var $animatingElems = $(e.relatedTarget).find("[data-animation^='animated']");
    doAnimations($animatingElems);
  });

  // login
  $('#loginModal').on('shown.bs.modal', function () {
    $('#username').focus();
  });

  $('#loginform').on('submit', function () {
    $('#btnlogin').html('กำลังเข้าสู่ระบบ...');
    $.ajax({
      type: 'POST',
      url: '{% url "app:login" %}',
      data: $(this).serialize(),
      success: function(response) {
        if(response.result === 'success') {
          window.location.href = '{{request.path}}';
        } else {
          alert('อีเมลหรือรหัสผ่านของท่านไม่ถูกต้อง!');
          $('#username').val('');
          $('#password').val('');
          $('#btnlogin').html('Login');
        }
      }
    });
    return false;
  });
})(jQuery);
