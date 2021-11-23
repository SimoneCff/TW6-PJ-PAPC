let cacheName = 'papc';
let filesToCache = [
    'manifest.json',
    'index.html',
    'css/style.css',
    'js/main.js',
    'images/cpu.png',
    'images/mobo.png',
    'images/psu.png',
    'images/ram.png',
    'images/icon.png'
];
/* Start the service worker and cache all of the app's content */
console.log('Service worker online');

self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open(cacheName).then(function(cache) {
            return cache.addAll(filesToCache);
        })
    );
});
/* Serve cached content when offline */
self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});
