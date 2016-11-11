"""bookings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
import settings

from hotels import views as hv
from flights import views as fv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', hv.index),
    url(r'^$', hv.HotelList.as_view()),
	url(r'^hotels/(?P<pk>\d+)$', hv.HotelDetail.as_view(), name='hotel-detail'),
	url(r'^hotel/new$', hv.HotelCreate.as_view(), name='hotel-create'),
    url(r'^vols$', fv.index),
    url(r'^contact$', hv.ContactView.as_view(), name='contact'),

    url(r'^accounts/', include('allauth.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]