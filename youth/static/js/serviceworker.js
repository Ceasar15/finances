
var staticCacheName = 'youth_cache';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        'youth/index',
        'youth/sermons',
        'youth/events',
        'youth/contact',
        'youth/about',
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('youth/index',
        'youth/sermons',
        'youth/events',
        'youth/contact',
        'youth/about',));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});
