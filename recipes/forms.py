from .models import Comment 
from django import forms 


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'category',
            'servings',
            'preparation_time',
            'cooking_time',
            'total_time',
            'recipe_image',
            'public'
        )

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author')
        super(RecipeForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Recipe.objects.filter(author=self.author, title=title).exists():
            raise forms.ValidationError("You have already written a recipe with same title.")
        return title
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
