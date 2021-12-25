from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from accounts.api.views import UserViewSet, AccountViewSet
from tweets.api.views import TweetViewSet
from friendships.api.views import FriendshipViewSet

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/accounts', AccountViewSet, basename='accounts')
router.register(r'api/tweets', TweetViewSet, basename='tweets')
router.register(r'api/friendships', FriendshipViewSet, basename='friendships')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__', include(debug_toolbar.urls))
    )