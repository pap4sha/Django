from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/', views.BlogDetalView.as_view(), name = 'post-detail'),
    path('post/new', views.BlogCreateView.as_view(), name = 'post_new'),
    path('post/edit/', views.BlogUpdateView.as_view(), name = 'post_edit'),
    path('post/delete/', views.BlogDeleteView.as_view(), name = 'post_delete')
]