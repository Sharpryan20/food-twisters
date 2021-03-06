from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
import string
import random

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    "Django Model of category database"
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    category_image = CloudinaryField("categories", blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """ Django Model of recipe database """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(null=False, max_length=250, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="recipe_posts"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipe_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    preparation_time = models.CharField(max_length=30, default=0)
    cooking_time = models.CharField(max_length=30, default=0)
    total_time = models.CharField(max_length=30, default=0)
    serving_size = models.CharField(max_length=30, default=0)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True
    )

    class Meta:
        """ Orders posts by date created using descending order """
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} | {self.author}"

    def number_of_likes(self):
        """Helper Method. Returns total count of likes on a recipe """
        return self.likes.count()

    def get_absolute_url(self):
        """Tells Django to go to recipe_detail.html"""
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """Comments Model"""
    post = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="comments"
    )
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
