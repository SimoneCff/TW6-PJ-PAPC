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
    var id = this.id
    if (id == 'checkout') {
        console.log("nel checkout")
        $('#check').attr('src', $(this).data('src'))
    } else {
        $('#iframe').attr('src', $(this).data('src'))
    }
})

