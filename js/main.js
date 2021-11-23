window.addEventListener('load', e => {
    new PWAConfApp();
    registerSW(); (1)
});

async function registerSW() { (1)
    if ('serviceWorker' in navigator) { (2)
        try {
            await navigator.serviceWorker.register('./sw.js'); (3)
        } catch (e) {
            alert('ServiceWorker registration failed. Sorry about that.'); (4)
        }
    } else {
        document.querySelector('.alert').removeAttribute('hidden'); (5)
    }
}