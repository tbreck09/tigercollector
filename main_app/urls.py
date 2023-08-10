from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tigers/', views.tigers_index, name='index'),
    path('tigers/<int:tiger_id>/', views.tigers_detail, name='detail'),
    path('tigers/create/', views.TigerCreate.as_view(), name='tigers_create'),
    path('tigers/<int:pk>/update/', views.TigerUpdate.as_view(), name='tigers_update'),
    path('tigers/<int:pk>/delete/', views.TigerDelete.as_view(), name='tigers_delete'),
    path('tigers/<int:tiger_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('tigers/<int:tiger_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('tigers/<int:tiger_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
