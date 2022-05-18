from django.urls import path
from . import views

app_name = 'streams'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.add, name='add'),
    path('<int:stream_id>/edit/', views.edit, name='edit'),
    path('<int:stream_id>/delete/', views.delete, name='delete')
]
