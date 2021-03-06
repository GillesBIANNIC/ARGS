#!/usr/bin/env python
# -*- coding: utf-8 -*

import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, maximum-scale=1">

<title>Homepage</title>
<link rel="icon" href="favicon.png" type="image/png">
<link rel="shortcut icon" href="favicon.ico" type="img/x-icon">

<link href='https://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,800italic,700italic,600italic,400italic,300italic,800,700,600' rel='stylesheet' type='text/css'>

<link href="css/bootstrap.css" rel="stylesheet" type="text/css">
<link href="css/style.css" rel="stylesheet" type="text/css">
<link href="css/font-awesome.css" rel="stylesheet" type="text/css">
<link href="css/responsive.css" rel="stylesheet" type="text/css">
<link href="css/animate.css" rel="stylesheet" type="text/css">

<!--[if IE]><style type="text/css">.pie {behavior:url(PIE.htc);}</style><![endif]-->

<script type="text/javascript" src="js/jquery.1.8.3.min.js"></script>
<script type="text/javascript" src="js/bootstrap.js"></script>
<script type="text/javascript" src="js/jquery-scrolltofixed.js"></script>
<script type="text/javascript" src="js/jquery.easing.1.3.js"></script>
<script type="text/javascript" src="js/jquery.isotope.js"></script>
<script type="text/javascript" src="js/wow.js"></script>
<script type="text/javascript" src="js/classie.js"></script>
<script src="contactform/contactform.js"></script>

<!-- =======================================================
    Theme Name: Knight
    Theme URL: https://bootstrapmade.com/knight-free-bootstrap-theme/
    Author: BootstrapMade
    Author URL: https://bootstrapmade.com
======================================================= -->

</head>
<body>
<header class="header" id="header"><!--header-start-->
	<div class="container">
    	<figure class="logo animated fadeInDown delay-07s">
        	<a href="#"><img src="img/logo.png" alt=""></a>
        </figure>
        <h1 class="animated fadeInDown delay-07s">Welcome to the TurtleBot Tic Tac Toe</h1>
        <ul class="we-create animated fadeInUp delay-1s">
        	<li>Made by students at ISEN.</li>
        </ul>
            <a class="link animated fadeInUp delay-1s servicelink" href="#service">PLAY</a>
    </div>
</header><!--header-end-->

<nav class="main-nav-outer" id="test"><!--main-nav-start-->
	<div class="container">
        <ul class="main-nav">
        	<li><a href="#header">Home</a></li>
            <li><a href="#service">Game</a></li>
            <li><a href="#team">Team</a></li>
        </ul>
        <a class="res-nav_click" href="#"><i class="fa-bars"></i></a>
    </div>
</nav><!--main-nav-end-->



<section class="main-section" id="service"><!--main-section-start-->
	<div class="container">
    	<h2>Game</h2>
    	<h6>Let's the game begin<a href="img/saw.jpg">.</a></h6>
        <div class="row">
        	<div class="col-xs-offset-3 wow fadeInLeft delay-05s">
							<iframe width="620" height="480"
										src="http://192.168.2.126:8182/stream?topic=/augmented_reality_output/image_raw&type=ros_compressed">
										<!--
                                        http://192.168.2.126:8182/stream?topic=/augmented_reality_output/image_raw&type=ros_compressed
										http://192.168.2.126:8182/stream?topic=/usb_cam/image_raw&type=ros_compressed
										_image_transport:=compressed-->
								</iframe>
            </div>
            </div>
						<div class="col-xs-offset-3 wow fadeInLeft delay-05s">
							<form action="/index.py" method="post">
						        <input type="text" name="name" value="A1" />
						        <input type="submit" name="send" value="Envoyer mouvement">
						  </form>
						</div>
        </div>
	</div>
</section><!--main-section-end-->

<section class="main-section team" id="team"><!--main-section team-start-->
	<div class="container">
        <h2>team</h2>
        <h6>Take a closer look into our amazing team. We won’t bite.</h6>
        <div class="team-leader-block clearfix">
            <div class="team-leader-box">
                <div class="team-leader wow fadeInDown delay-03s">
                    <div class="team-leader-shadow"><a href="#"></a></div>
                    <img src="img/gilles.jpg" alt="">
                    <ul>
                        <li><a href="https://fr.linkedin.com/in/gilles-biannic-46834b11a" class="fa-linkedin"></a></li>
                    </ul>
                </div>
                <h3 class="wow fadeInDown delay-03s">Gilles</h3>
                <span class="wow fadeInDown delay-03s">Seigneur sith</span>
                <p class="wow fadeInDown delay-03s">"Wololo !" Citation d'un prêtre</p>
            </div>
            <div class="team-leader-box">
                <div class="team-leader  wow fadeInDown delay-06s">
                    <div class="team-leader-shadow"><a href="#"></a></div>
                    <img src="img/david2.jpg" alt="">
                    <ul>
                        <li><a href="https://fr.linkedin.com/in/david-floc-h-510797115" class="fa-linkedin"></a></li>
                    </ul>
                </div>
                <h3 class="wow fadeInDown delay-06s">David</h3>
                <span class="wow fadeInDown delay-06s">Sergent chef</span>
                <p class="wow fadeInDown delay-06s">"Un deux un deux, ennemis repérés !" Citation Droïde de combat B241 </p>
            </div>
						<div class="team-leader-box">
								<div class="team-leader wow fadeInDown delay-09s">
										<div class="team-leader-shadow"><a href="#"></a></div>
										<img src="img/pym.jpg" alt="">
										<ul>
												<li><a href="https://fr.linkedin.com/in/pierre-yves-mingam-72196a10a" class="fa-linkedin"></a></li>
										</ul>
								</div>
								<h3 class="wow fadeInDown delay-09s">Pierre-yves</h3>
								<span class="wow fadeInDown delay-09s">Contrebandier de bâtons de la mort</span>
								<p class="wow fadeInDown delay-06s">"Tu aime l'odeur du bruit de l'eau ?"</p>
						</div>
            <div class="team-leader-box">
                <div class="team-leader wow fadeInDown delay-09s">
                    <div class="team-leader-shadow"><a href="#"></a></div>
                    <img src="img/matthieu2.jpg" alt="">
                    <ul>
                        <li><a href="https://fr.linkedin.com/in/matthieu-philippe-30269082" class="fa-linkedin"></a></li>
                    </ul>
                </div>
                <h3 class="wow fadeInDown delay-09s">Matthieu</h3>
                <span class="wow fadeInDown delay-09s">kounchita</span>
                <p class="wow fadeInDown delay-06s">"Un intellectuel assis va moins loin qu'un con qui marche." Citation de Michel Audiard</p>
            </div>
        </div>
    </div>
</section><!--main-section team-end-->

<footer class="footer">
    <div class="container">
        <div class="footer-logo"><a href="#"><img src="img/footer-logo.png" alt=""></a></div>
        <span class="copyright">&copy; Knight Theme. All Rights Reserved</span>
        <div class="credits">
            <!--
                All the links in the footer should remain intact.
                You can delete the links only if you purchased the pro version.
                Licensing information: https://bootstrapmade.com/license/
                Purchase the pro version with working PHP/AJAX contact form: https://bootstrapmade.com/buy/?theme=Knight
            -->
            <a href="https://bootstrapmade.com/free-business-bootstrap-themes-website-templates/">Business Bootstrap Themes</a> by <a href="https://bootstrapmade.com/">BootstrapMade</a>
        </div>
    </div>
</footer>


<script type="text/javascript">
    $(document).ready(function(e) {
        $('#test').scrollToFixed();
        $('.res-nav_click').click(function(){
            $('.main-nav').slideToggle();
            return false

        });

    });
</script>

  <script>
    wow = new WOW(
      {
        animateClass: 'animated',
        offset:       100
      }
    );
    wow.init();
  </script>


<script type="text/javascript">
	$(window).load(function(){

		$('.main-nav li a, .servicelink').bind('click',function(event){
			var $anchor = $(this);

			$('html, body').stop().animate({
				scrollTop: $($anchor.attr('href')).offset().top - 102
			}, 1500,'easeInOutExpo');
			/*
			if you don't want to use the easing effects:
			$('html, body').stop().animate({
				scrollTop: $($anchor.attr('href')).offset().top
			}, 1000);
			*/
      if ($(window).width() < 768 ) {
        $('.main-nav').hide();
      }
			event.preventDefault();
		});
	})
</script>

<script type="text/javascript">

$(window).load(function(){


  var $container = $('.portfolioContainer'),
      $body = $('body'),
      colW = 375,
      columns = null;


  $container.isotope({
    // disable window resizing
    resizable: true,
    masonry: {
      columnWidth: colW
    }
  });

  $(window).smartresize(function(){
    // check if columns has changed
    var currentColumns = Math.floor( ( $body.width() -30 ) / colW );
    if ( currentColumns !== columns ) {
      // set new column count
      columns = currentColumns;
      // apply width to container manually, then trigger relayout
      $container.width( columns * colW )
        .isotope('reLayout');
    }

  }).smartresize(); // trigger resize to set container width
  $('.portfolioFilter a').click(function(){
        $('.portfolioFilter .current').removeClass('current');
        $(this).addClass('current');

        var selector = $(this).attr('data-filter');
        $container.isotope({

            filter: selector,
         });
         return false;
    });

});

</script>

</body>
</html>
"""
print(html)
