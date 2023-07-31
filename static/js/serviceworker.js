var staticCacheName = 'djangopwa-v3';
var dynamicCacheName = 'dynamicCacheName-v2';

self.addEventListener('install', function (event) {
    console.log("ServiceWorker installed");
    event.waitUntil(
        caches.open(staticCacheName).then(function (cache) {
            return cache.addAll([
                '/',
            ]);
        })
    );
});

self.addEventListener('fetch', function (event) {
    //var requestUrl = new URL(event.request.url);
    // if (requestUrl.origin === location.origin) {
    //     if ((requestUrl.pathname === '/landing')) {
    //         event.respondWith(caches.match('/'));
    //         return;
    //     }
    // }


    self.addEventListener('fetch', function (event) {
        event.respondWith(
            // Try fetching the request from the server first.
            fetch(event.request)
            .then(function (fetchRes) {
                // If fetch is successful, clone the response and cache it before returning it to the page.
                const clonedResponse = fetchRes.clone();
                caches.open(dynamicCacheName)
                    .then(function (cache) {
                        cache.put(event.request, clonedResponse);
                    });

                return fetchRes;
            })
            .catch(function () {
                // If fetch fails (e.g., when the user is offline), try to retrieve the response from the cache.
                return caches.match(event.request);
            })
        );
    });

});