from .views import PostCreate, PostDelete, PostUpdate
from django.urls import path

urlpatterns = [
    path('', PostCreate.as_view(), name='home'),
    path('post/<int:pk>', PostCreate.as_view(), name='post'),
    path('update/<int:pk>', PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>', PostDelete.as_view(), name='delete')
]
