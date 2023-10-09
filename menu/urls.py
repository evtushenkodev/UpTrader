from django.urls import path
from menu.views import IndexPageView

app_name = 'menu'

urlpatterns = [
    path('foodmenu/', IndexPageView.as_view(), name='index-page')
]
