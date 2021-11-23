let cacheName = 'papc';
let staticAssets = [
    './',
    'index.html',
    'css/style.css',
    'js/main.js',
    'images/case.png',
    'images/cooling.png',
    'images/cpu.png',
    'images/icon.png',
    'images/icon1.png',
    'images/memory.png',
    'images/mobo.png',
    'images/psu.png',
    'images/ram.png'
    ];

self.addEventListener('install', async event => {
    console.log('install event');
    const cache = await caches.open(cacheName);
    await cache.addAll(staticAssets);
});

self.addEventListener('fetch', async event => {
    console.log('fetch event');
    const req = event.request;
    if (/.*(json)$/.test(req.url)) {
        event.respondWith(networkFirst(req));
    } else {
        event.respondWith(cacheFirst(req));
    }
});

async function cacheFirst(req) {
    const cache = await caches.open(cacheName);
    const cachedResponse = await cache.match(req);
    return cachedResponse || networkFirst(req);
}

async function networkFirst(req) {
    const cache = await caches.open(cacheName);
    try { (1)
        const fresh = await fetch(req);
        cache.put(req, fresh.clone());
        return fresh;
    } catch (e) { (2)
        const cachedResponse = await cache.match(req);
        return cachedResponse;
    }
}