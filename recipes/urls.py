from . import views 
from django.urls import path


urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('recipe/', views.RecipeList.as_view(), name='recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]