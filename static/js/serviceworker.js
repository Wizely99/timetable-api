// service-worker.js

importScripts('https://cdnjs.cloudflare.com/ajax/libs/workbox-sw/7.0.0/workbox-sw.js');
// importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.1.1/workbox-sw.js');

const timetableStaticCacheName = 'timetableStaticCacheName-v2';
const timetableDynamicCacheName = 'timetableDynamicCacheName-v2';
const timetableDocumentCacheName = 'timetableHtmlCacheName-v2';
const timetableScriptsCacheName = 'timetableScriptsCacheName-v2';

workbox.routing.registerRoute(
    ({
        request,
        url
    }) => request.destination === 'document' &&
    !url.pathname.startsWith('/accounts/login/'),
    new workbox.strategies.NetworkFirst({
        cacheName: timetableDocumentCacheName,
    })
);

workbox.routing.registerRoute(
    ({
        request
    }) => request.destination === 'script' || request.destination === 'style',
    new workbox.strategies.StaleWhileRevalidate({
        cacheName: timetableScriptsCacheName,
    })
);

workbox.routing.registerRoute(
    ({
        request
    }) => request.destination === 'image',
    new workbox.strategies.CacheFirst({
        cacheName: timetableStaticCacheName,
    })
);

workbox.routing.registerRoute(
    ({
        request
    }) => request.destination === 'font',
    new workbox.strategies.CacheFirst({
        cacheName: timetableStaticCacheName,
    })
);