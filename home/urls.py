from django.conf.urls import url
from .views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	url(r'^$', HomeView.as_view(), name = 'home'),
	
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

