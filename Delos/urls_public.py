from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from Delos import settings

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('translate/', include('rosetta.urls')),

]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('webcore.urls')),
    path('accounts/', include('authentication.urls')),
    # Needed for translations in Javascript
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
)