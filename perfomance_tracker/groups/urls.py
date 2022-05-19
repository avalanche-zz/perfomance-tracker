from django.urls import path
from .views import GroupsList, GroupDetail, AddGroup, EditGroup, DeleteGroup

app_name = 'groups'
urlpatterns = [
    path('', GroupsList.as_view(), name='groups'),
    path('<int:pk>/', GroupDetail.as_view(), name='group'),
    path('add/', AddGroup.as_view(), name='add'),
    path('<int:pk>/edit/', EditGroup.as_view(), name='edit'),
    path('<int:pk>/delete/', DeleteGroup.as_view(), name='delete')
]
