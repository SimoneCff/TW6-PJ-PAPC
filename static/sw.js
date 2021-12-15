let cacheName = 'papc';
let filesToCache = [
    '/',
    '/css/style.css',
    '/js/main.js',
    '/images/case.png',
    '/images/cooling.png',
    '/images/cpu.png',
    '/images/memory.png',
    '/images/mobo.png',
    '/images/psu.png',
    '/images/ram.png',
    '/images/icon.jpg',
    '/images/icon1.jpg',
    '/images/logo.png',
    '/images/icon.ico']

self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(cacheName).then(function(cache) {
            return cache.addAll(filesToCache);
        })
    );
});

self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});
