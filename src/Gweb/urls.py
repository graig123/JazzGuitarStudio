from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import scales.urls
from . import views
from scales.views import ScalesPage, AjaxScales
from chords.views import ChordsPage, ArpegiosPage, AjaxChord


urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^scales/$', ScalesPage.as_view(), name='scales'),
    url(r'^chords/$', ChordsPage.as_view(), name='chords'),
    url(r'^arpegios/$', ArpegiosPage.as_view(), name='arpegios'),
    url(r'^AjaxChord/$', AjaxChord.as_view(), name='AjaxChord'),
    url(r'^AjaxScales/$', AjaxScales.as_view(), name='AjaxScales'),
    #url(r'^scales/', include(scales.urls, namespace='scales')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
