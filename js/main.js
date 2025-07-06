(function ($) {
    "use strict";
    
    // Document ready
    $(document).ready(function () {
        // Dropdown on mouse hover
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
        
        // Initialize Hero Carousel
        console.log('Document ready - Initializing hero carousel...');
        
        // Check if the carousel element exists
        var $heroCarousel = $('.hero-carousel');
        if ($heroCarousel.length) {
            console.log('Hero carousel element found, initializing...');
            
            // Initialize the carousel
            $heroCarousel.owlCarousel({
                items: 1,
                loop: true,
                autoplay: true,
                autoplayTimeout: 7000,
                autoplayHoverPause: true,
                smartSpeed: 1000,
                dots: true,
                nav: false,
                animateOut: 'fadeOut',
                animateIn: 'fadeIn',
                onInitialized: function(event) {
                    console.log('Hero carousel initialized successfully');
                },
                onChanged: function(event) {
                    console.log('Slide changed to: ' + event.item.index);
                }
            });
            
            // Custom navigation
            $('.carousel-nav-prev').click(function() {
                $heroCarousel.trigger('prev.owl.carousel');
            });

            $('.carousel-nav-next').click(function() {
                $heroCarousel.trigger('next.owl.carousel');
            });
            
            // Pause autoplay when hovering over carousel
            $heroCarousel.hover(
                function() {
                    $heroCarousel.trigger('stop.owl.autoplay');
                },
                function() {
                    $heroCarousel.trigger('play.owl.autoplay');
                }
            );
            
            // Scroll down button
            $('.scroll-down').click(function() {
                $('html, body').animate({
                    scrollTop: $('.hero-section').next().offset().top
                }, 800);
            });
            
            // Log if images are loaded
            $heroCarousel.find('.hero-slide').each(function() {
                var bg = $(this).css('background-image').replace('url("', '').replace('")', '');
                console.log('Slide background image:', bg);
            });
        } else {
            console.error('Hero carousel element not found!');
        }
        
        // Back to top button
        $(window).scroll(function () {
            if ($(this).scrollTop() > 100) {
                $('.back-to-top').fadeIn('slow');
            } else {
                $('.back-to-top').fadeOut('slow');
            }
        });
        
        $('.back-to-top').click(function () {
            $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
            return false;
        });

        // Portfolio isotope and filter
        var portfolioIsotope = $('.portfolio-container').isotope({
            itemSelector: '.portfolio-item',
            layoutMode: 'fitRows'
        });

        $('#portfolio-flters li').on('click', function () {
            $("#portfolio-flters li").removeClass('active');
            $(this).addClass('active');
            portfolioIsotope.isotope({filter: $(this).data('filter')});
        });

        // Post carousel
        $(".post-carousel").owlCarousel({
            autoplay: true,
            smartSpeed: 1500,
            dots: false,
            loop: true,
            nav: true,
            navText: [
                '<i class="fa fa-angle-left" aria-hidden="true"></i>',
                '<i class="fa fa-angle-right" aria-hidden="true"></i>'
            ],
            responsive: {
                0: { items: 1 },
                576: { items: 1 },
                768: { items: 2 },
                992: { items: 2 }
            }
        });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        center: true,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        smartSpeed: 1000,
        dots: true,
        loop: true,
        nav: true,
        navText: [
            '<i class="fas fa-chevron-left"></i>',
            '<i class="fas fa-chevron-right"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        },
        onInitialized: function() {
            console.log('Testimonial carousel initialized');
        },
        onTranslated: function() {
            console.log('Testimonial carousel slide changed');
        }
    });
    
    }); // Close the document.ready function
    
})(jQuery);

