from django.urls import path
from webcore.views import IndexView

app_name = 'webcore'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
