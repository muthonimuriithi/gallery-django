from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    path('',views.landing,name='landing'),
    path('search/',views.search_results, name='search_results'),
    path('category/(\w+)', views.page_category,name='page_category'),
    path('location/(\w+)', views.page_location,name='page_location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)