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

function openhtml(x){
    var tab = document.createElement("IFRAME");
    switch(x) {
        case'cpu':
            tab.setAttribute("src","www.google.com");
            document.body.appendChild(x);
            break;
        case'mobo':
            console.log('cliccato mobo');
            break;
        case'psu':
            console.log('cliccato psu');
            break;
        case'ram':
            console.log('cliccato ram');
            break;
        case'memory':
            console.log('cliccato memory');
            break;
        case'cooling':
            console.log('cliccato cooling');
            break;
        case'case':
            console.log('cliccato case');
            break;
    }
}

