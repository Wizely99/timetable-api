// service-worker.js

importScripts('https://cdnjs.cloudflare.com/ajax/libs/workbox-sw/7.0.0/workbox-sw.js');
// importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.1.1/workbox-sw.js');

const staticCacheName = 'timetableStaticCacheName-v4';
const dynamicCacheName = 'timetableDynamicCacheName-v5';
const documentCacheName = 'timetableHtmlCacheName-v5';

workbox.routing.registerRoute(
    ({
        request
    }) => request.destination === 'document',
    new workbox.strategies.NetworkFirst({
        cacheName: documentCacheName,
    })
);

workbox.routing.registerRoute(
    ({
        request
    }) => request.destination === 'script' || request.destination === 'style',
    new workbox.strategies.StaleWhileRevalidate({
        cacheName: staticCacheName,
    })
);

workbox.routing.registerRoute(
    ({
        request
    }) => request.destination === 'image',
    new workbox.strategies.CacheFirst({
        cacheName: staticCacheName,
    })
);

workbox.routing.registerRoute(
    ({
        request
    }) => request.destination === 'font',
    new workbox.strategies.CacheFirst({
        cacheName: staticCacheName,
    })
);



workbox.routing.registerRoute(
    ({
        request
    }) => true, // Catch-all for other requests
    new workbox.strategies.StaleWhileRevalidate({
        cacheName: dynamicCacheName,
    })
);