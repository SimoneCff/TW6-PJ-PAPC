window.onload = () => {
    'use strict';

    if ('serviceWorker' in navigator) {
        navigator.serviceWorker
            .register('/service-worker.js', {scope: '/'}).then(function (registration) {

            // Service worker registered correctly.
            console.log('ServiceWorker registration successful with scope: ', registration.scope);
        },
            function (err) {

                // Troubles in registering the service worker. :(
                console.log('ServiceWorker registration failed: ', err);
            });
    }
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function () {
            navigator.serviceWorker.register('/service-worker.js');
        });
    }
}

$('button').click(function() {
    $('#iframe').attr('src', $(this).data('src'))
})

