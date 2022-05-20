from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Recipe, Category
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    """View to show all recipes posted"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipe.html'
    paginate_by = 10


class RecipeDetail(View):
    """View to show recipe details for selected recipe"""
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


def index(request):
    """View to see index page"""
    return render(request, "index.html")


class CategoryList(generic.ListView):
    """View to see categories"""
    model = Category
    queryset = Category.objects.all()
    template_name = 'category.html'


class CategoryRecipe(View):
    """View to see recipes in specific category"""
    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        queryset = Recipe.objects.filter(
            category__slug=slug).order_by('-created_on')
        context = {
            'recipe_list': queryset,
            'category': category
        }

        return render(
            request,
            'category_recipe.html',
            context
        )


class RecipeLike(View):
    """View to toggle like button"""
    def post(self, request, slug):
        post = get_object_or_404(Recipe, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def CreateRecipe(request):
    """
    renders share a recipe page
    """
    recipe_form = RecipeForm(request.POST or None, request.FILES or None)
    context = {
        'recipe_form': recipe_form,
    }

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            print('valid')
            recipe_form.instance.author = request.user
            recipe_form.instance.status = 1
            recipe = recipe_form.save(commit=False)

            recipe.save()
            return redirect('index')
        else:
            print('invalid')
    else:
        recipe_form = RecipeForm()
    return render(request, "create_recipe.html", context)


class UserRecipes(generic.ListView):
    """View to show recipes posted by the user logged in."""
    def get(self, request):
        recipes = Recipe.objects.filter(
            author=request.user, status=1
        ).order_by('-created_on')
        print(recipes)
        return render(request, 'my_recipes.html', {'recipes': recipes})


class UpdateRecipe(UpdateView):
    """View to update a recipe"""
    model = Recipe
    template_name = 'update_recipe.html'
    form_class = RecipeForm


class DeleteRecipe(DeleteView):
    """View to delete recipe"""
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('user_recipes')
