window.onload = () => {
    'use strict';


// service-worker:
    if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/sw.js').then(function (registration) {
                console.log('Service Worker registration was successful with scope: ', registration.scope);
            }).catch(function (err) {
                console.log('ServiceWorker registration failed: ', err);
            });
    };
}

$('button').click(function() {
    $('#iframe').attr('src', $(this).data('src'))
})

