from django.contrib import admin
from .models import Post, Style, Purchase, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status','updated_on')
    search_fields = ['title','author']
    list_filter = ('status','author','date_posted',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'excerpt')

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('post_review', 'author_review', 'rating', 'date_review')
    search_fields = ['post_review', 'author_review', 'rating']
    list_filter = ('post_review', 'author_review', 'rating')
    prepopulated_fields = {}
    summernote_fields = ('body',)

@admin.register(Style)
class StyleAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('name','description',)
    search_fields = ['name']
    list_filter = ('name',)
    prepopulated_fields = {}
    summernote_fields = ('description',)

@admin.register(Purchase)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('post_interest', 'product_name','created_on')
    search_fields = ['post_interest', 'product_name',]
    list_filter = ('post_interest', 'product_name','price','store_name')
    prepopulated_fields = {}
    summernote_fields = ()


# Register your models here.
