window.onload = () => {
    'use strict';

// service-worker:
    if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('./sw.js').then(function (registration) {
                console.log('Service Worker registration was successful with scope: ', registration.scope);
            }).catch(function (err) {
                console.log('ServiceWorker registration failed: ', err);
            });
    } else {
        console.log("sw not working");
    };
}

$('button').click(function() {
    $('#iframe').attr('src', $(this).data('src'))
})

$('carrello').click(function() {
    $('#check').attr('src', $(this).data('src'))
})

