const CACHE_NAME = 'codecards-v1';
const ASSETS = [
    '/',
    '/index.html',
    '/style.css',
    '/manifest.json',
    '/imgs/32.png',
    '/imgs/96.png',
    '/imgs/180.png'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(ASSETS))
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => response || fetch(event.request))
    );
});
