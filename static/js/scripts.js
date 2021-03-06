/*!
* Start Bootstrap - Creative v7.0.6 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {
    // Navbar shrink function
    var pageURL = "http://127.0.0.1:8000/home/";
    var pageURL2 = "http://127.0.0.1:8000/";
    var pageURL3 = "http://127.0.0.1:8000/account/";
    var pageURL4 = "http://127.0.0.1:8000/register/";
    var pageURL5 = "http://127.0.0.1:8000/login/";
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0 && (
                window.location.href == pageURL || 
                window.location.href == pageURL2 || 
                window.location.href == pageURL3 ||
                window.location.href == pageURL4 ||
                window.location.href == pageURL5
            )) {
            navbarCollapsible.classList.remove('navbar-shrink')
            
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };
    console.log(window)
    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);


    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    new SimpleLightbox({
        elements: '#portfolio a.portfolio-box'
    });

});

// Tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})


// Alerts fade out
setTimeout(function () {
  
    // Closing the alert
    $(".alert").delay(5000).slideUp(800, function() {
        $(this).alert('close');
    });
});