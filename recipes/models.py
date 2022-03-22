from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Recipe(models.Model):
    """ Django Modle of recipe database """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    updated_on = models.DateTimeField(auto_now=True)
    preparation_time = models.CharField(max_length=30 , default=0)
    cooking_time = models.CharField(max_length=30, default=0)
    ingredients = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta:
        """ Orders posts by date created using descending order """
        ordering = ['-created_on']
    
    def __str__(self):
       return f"{self.title} | {self.author}" 
    
    def number_of_likes(self):
        """Helper Method. Returns total count of likes on a recipe """
        return self.likes.count()
    
class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=120)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        """
        Show order of comments.
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


