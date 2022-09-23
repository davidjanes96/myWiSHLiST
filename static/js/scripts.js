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
    var pageURL6 = "http://127.0.0.1:8000/reset_password/";
    var pageURL7 = "http://127.0.0.1:8000/reset_password_sent/";
    var pageURL8 = "http://127.0.0.1:8000/reset/MQ/set-password/";
    var pageURL9 = "http://127.0.0.1:8000/reset_password_complete/";
    var pageURL10 = "http://127.0.0.1:8000/change_password/";
    var pageURL11 = "http://127.0.0.1:8000/change_password_done/";
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
                window.location.href == pageURL5 ||
                window.location.href == pageURL6 ||
                window.location.href == pageURL7 ||
                window.location.href == pageURL8 ||
                window.location.href == pageURL9 ||
                window.location.href == pageURL10 ||
                window.location.href == pageURL11
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



//Edit & preview account switch
function editDIV() {
    document.getElementById("displayDIV").style.display="none";
    document.getElementById("editDIV").style.display="block";
}
//if errors exist keep edit div display
let error = document.getElementById("error");

if (error){
    editDIV();
}


//Search + Pagination fix
//get search forms and page links
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

//ensure search form exists
if(searchForm){
    for(let i=0; pageLinks.length > i; i++){
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault()
            //get thr data attribute
            let page = this.dataset.page
            //add hidden search input to form
            searchForm.innerHTML += `<input value=${page} name="page" hidden />`
            //submit
            searchForm.submit()
        })
    }
}

//sort dropdown submit