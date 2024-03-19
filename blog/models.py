from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
RATE = ((1, "1",), (2, "2",), (3, "3",), (4, "4",), (5, "5",))

class Style(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"This is {self.name} decor style "

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    image= models.CharField(max_length=200)
    decor_style= models.ForeignKey(Style, on_delete=models.CASCADE, related_name="post_style")
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"  


class Purchase(models.Model):
    post_interest = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='purchases')
    store_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_link = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"You can find {self.product_name} in {self.store_name} "

class Review (models.Model):
    post_review = models.ForeignKey(Post,
        on_delete=models.CASCADE, related_name="reviews")
    author_review = models.ForeignKey(User,
        on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField(max_length=1000)
    date_review = models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(choices=RATE, blank=True)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Review {self.body} by {self.author_review}"



