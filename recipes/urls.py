from . import views
from django.urls import path


urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'post/',
        views.RecipeList.as_view(),
        name='post'
    ),
    path(
        'category/',
        views.CategoryList.as_view(),
        name='category'
    ),
    path(
        'categoryrecipe/<slug:slug>',
        views.CategoryRecipe.as_view(),
        name='category_recipe'
    ),
    path(
        '<slug:slug>/',
        views.RecipeDetail.as_view(),
        name='recipe_detail'
    ),
    path(
        'like/<slug:slug>',
        views.RecipeLike.as_view(),
        name='recipe_like'
    ),
    path(
        'create-recipe',
        views.CreateRecipe,
        name='create_recipe'
    ),
    path(
        'user-recipe',
        views.UserRecipes.as_view(),
        name='user_recipes'
    ),
    path(
        'update-recipe/<slug:slug>',
        views.UpdateRecipe.as_view(),
        name='update_recipe'
    ),
    path(
        'delete-recipe/<slug:slug>',
        views.DeleteRecipe.as_view(),
        name='delete_recipe'
    ),
]
