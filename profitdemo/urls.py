from django.urls import path

from profitdemo.views.start import start

urlpatterns = [
    path('wd', start),
]
