from . import views 
from django.urls import path

#base_url/recipes
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('recipe/', views.RecipeList.as_view(), name='recipe'),
#     path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
#     path('category/', views.CategoryList.as_view(), name='category'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.RecipeList.as_view(), name='post'),
    path('category/', views.CategoryList.as_view(), name='category'),
    path('categoryrecipe/<slug:slug>', views.CategoryRecipe.as_view(), name='category_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('create-recipe', views.CreateRecipe, name='create_recipe'),
    path('user-recipe', views.UserRecipes.as_view(), name='user_recipes')
]