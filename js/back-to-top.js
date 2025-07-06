// Back to Top Button
(function() {
    'use strict';

    // Create back to top button
    var backToTop = document.createElement('a');
    backToTop.setAttribute('id', 'back-to-top');
    backToTop.setAttribute('href', '#');
    backToTop.setAttribute('class', 'back-to-top');
    backToTop.innerHTML = '<i class="fa fa-arrow-up"></i>';
    document.body.appendChild(backToTop);

    // Show/hide button on scroll
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            document.getElementById('back-to-top').classList.add('show');
        } else {
            document.getElementById('back-to-top').classList.remove('show');
        }
    });

    // Smooth scroll to top
    document.getElementById('back-to-top').addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
})();
