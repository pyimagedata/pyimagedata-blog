from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from PIL import Image
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(editable=False,default='slug_slug')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def article_count(self):
        return self.article_counts.all().count()


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

    def tag_count(self):
        return self.tag_count.all().count()

class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="article_counts")
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    slug = models.SlugField(max_length=100,editable=False,default="slug")
    tag = models.ManyToManyField(Tag, related_name="tag_count", blank=True)
    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        img = img.resize((1000, 620))
        img.save(self.image.path)
        