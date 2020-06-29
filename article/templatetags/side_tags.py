from django import template
from article.models import Category, Article, Tag



register = template.Library()

@register.simple_tag(name="category")
def all_categories():
    return Category.objects.all()

@register.simple_tag(name="tag")
def all_tags():
    return Tag.objects.all()

@register.simple_tag(name="popular")
def all_popular():
    return Article.objects.order_by('-hit')[:5]

