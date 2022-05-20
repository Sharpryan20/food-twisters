from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'category',
            'preparation_time',
            'cooking_time',
            'total_time',
            'serving_size',
            'ingredients',
            'instructions',
            'featured_image',
        ]

        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
