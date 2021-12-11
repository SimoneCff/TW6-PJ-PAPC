let cacheName = 'papc';
let filesToCache = [
    '/',
    '/static/css/style.css',
    '/static/js/main.js',
    '/static/images/case.png',
    '/static/images/cooling.png',
    '/static/images/cpu.png',
    '/static/images/memory.png',
    '/static/images/mobo.png',
    '/static/images/psu.png',
    '/static/images/ram.png',
    '/static/images/icon.jpeg',
    '/static/images/icon1.jpeg',
    '/static/images/logo.png',
    '/static/images/icon.icon'
    ];
self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(cacheName).then(function(cache) {
            console.log('Opened cache');
            return cache.addAll(filesToCache);
        })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
            .then(function(response) {
                // Cache hit - return response
                if (response) {
                    return response;
                }

                return fetch(event.request).then(
                    function(response) {
                        // Check if we received a valid response
                        if(!response || response.status !== 200 || response.type !== 'basic') {
                            return response;
                        }

                        var responseToCache = response.clone();

                        caches.open('papc')
                            .then(function(cache) {
                                cache.put(event.request, responseToCache);
                            });

                        return response;
                    }
                );
            })
    );
});

self.addEventListener('activate', function(event) {

    var cacheAllowlist = ['pages-cache-v1', 'blog-posts-cache-v1'];

    event.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(cacheName) {
                    if (cacheAllowlist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});