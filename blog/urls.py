from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name=''),
    path('featured/', views.BlogPostFeaturedView.as_view(), name='blog-featured'),
    # path('category', views.BlogPostCategoryView.as_view(), name='blog-category'),
    path('<slug>', views.BlogPostDetailView.as_view(), name='blog-detail'),
    path('category/<str:pk>/', views.BlogPostCategoryView.as_view(), name='blog-category'),
]
