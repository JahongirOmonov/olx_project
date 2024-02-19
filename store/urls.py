from django.urls import path

from store.views import CategoryListAPIView, PostDetailApiView,StatusPostListApiView


urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('post-detail/<int:pk>', PostDetailApiView.as_view()),
    path('vip-posts/', StatusPostListApiView.as_view())

]