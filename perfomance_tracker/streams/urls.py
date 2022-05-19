from django.urls import path
from .views import StreamsList, StreamDetail, AddStream, EditStream, DeleteStream, AddGroup

app_name = 'streams'
urlpatterns = [
    path('', StreamsList.as_view(), name='streams'),
    path('<int:pk>/', StreamDetail.as_view(), name='stream'),
    path('add/', AddStream.as_view(), name='add'),
    path('<int:pk>/edit/', EditStream.as_view(), name='edit'),
    path('<int:pk>/delete/', DeleteStream.as_view(), name='delete'),
]
