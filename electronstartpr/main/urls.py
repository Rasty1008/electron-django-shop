from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
]