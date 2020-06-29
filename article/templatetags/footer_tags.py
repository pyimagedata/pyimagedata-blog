from django import template
from article.models import Article



register = template.Library()

@register.simple_tag(name="latest")
def all_latests():
    return Article.objects.all().order_by('-id')[:3]

@register.simple_tag(name="popular")
def all_popular():
    return Article.objects.order_by('-hit')[:3]

