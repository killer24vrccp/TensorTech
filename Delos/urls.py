from django.conf.urls.i18n import i18n_patterns
from django.template.context_processors import static
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from Delos import settings
from authentication import admin

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(
    # Needed for translations in Javascript
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
)