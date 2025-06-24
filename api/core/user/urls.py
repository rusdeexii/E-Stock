from django.urls import path
from .views import UserListView, UserCreateView, UserDetailView, MeView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('create', UserCreateView.as_view(), name='user-create'),
    path('<uuid:pk>', UserDetailView.as_view(), name='user-detail'),
    path('me', MeView.as_view(), name='user-me'),
]
