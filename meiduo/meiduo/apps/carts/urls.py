from django.apps import AppConfig
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cart/$', views.CartsView.as_view()),
    url(r'^cart/selection/$', views.CartsSelectionView.as_view()),
]