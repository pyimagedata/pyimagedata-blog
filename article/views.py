from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView, ListView,DetailView
from .models import Article, Category, Tag
from django.db.models import Q
from django.db.models.expressions import F

# Create your views here.


class Index_View(ListView):
    model = Article
    template_name = 'articles/index.html'
    context_object_name = "posts"
    ordering = '-id'
    paginate_by = 6


# Detail Page

class Detail_View(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = "post"

    def get(self, request, *args, **kwargs):
        self.hit = Article.objects.filter(id = self.kwargs['pk']).update(hit=F('hit')+1)
        return super(Detail_View, self).get(request, *args, **kwargs)

    def get_context_data(self,*args, **kwargs):
        context = super(Detail_View, self).get_context_data(**kwargs)
        context['previous'] = Article.objects.filter(id__lt = self.kwargs['pk']).order_by('-pk').first()
        context['next'] = Article.objects.filter(id__gt = self.kwargs['pk']).order_by('pk').first()
        return context


# Category Page

class Category_View(ListView):
    model = Article
    template_name = 'articles/categories.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Article.objects.filter(category=self.category).order_by("-id")

    def get_context_data(self,*args, **kwargs):
        context = super(Category_View, self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        context['category_name'] = self.category
        return context


# Tag Page

class Tag_View(ListView):
    model = Article
    template_name = 'articles/tags.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return Article.objects.filter(tag=self.tag).order_by("-id")

    def get_context_data(self,*args, **kwargs):
        context = super(Tag_View, self).get_context_data(**kwargs)
        self.tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        context['tag_name'] = self.tag
        return context

# search page

class Search_View(ListView):
    model = Article
    template_name = 'articles/search.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self,*args, **kwargs):
        query = self.request.GET.get('q')

        if query:
            querry = Article.objects.filter(Q(title__icontains=query)).order_by('-id')
            return Article.objects.filter(Q(title__icontains=query)).order_by('-id')

        

# ai

class DeepLearning_View(ListView):
    model = Article
    template_name = 'articles/ai/deep_learning.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="deep learning")).order_by("-id")


class MachineLearning_View(ListView):
    model = Article
    template_name = 'articles/ai/machine_learning.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="machine learning")).order_by("-id")

class RF_View(ListView):
    model = Article
    template_name = 'articles/ai/rf_learning.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="reinforcement learning")).order_by("-id")

class Datascience_View(ListView):
    model = Article
    template_name = 'articles/ai/datascience.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="datascience")).order_by("-id")

# computer vision

class Image_Processing_View(ListView):
    model = Article
    template_name = 'articles/computer_vision/image_processing.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="image processing")).order_by("-id")

class Opencv_View(ListView):
    model = Article
    template_name = 'articles/computer_vision/opencv.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="opencv")).order_by("-id")

class RCNN_View(ListView):
    model = Article
    template_name = 'articles/computer_vision/r_cnn.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="r-cnn")).order_by("-id")

class Yolo_View(ListView):
    model = Article
    template_name = 'articles/computer_vision/yolo.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="yolo")).order_by("-id")

# Robotics

class Ros_View(ListView):
    model = Article
    template_name = 'articles/robotics/ros.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="ros")).order_by("-id")

class RaspberryPi_View(ListView):
    model = Article
    template_name = 'articles/robotics/raspberry_pi.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="raspberry pi")).order_by("-id")

class Arduino_View(ListView):
    model = Article
    template_name = 'articles/robotics/arduino.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="arduino")).order_by("-id")

class RobotArm_View(ListView):
    model = Article
    template_name = 'articles/robotics/robot_arm.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="robot arm")).order_by("-id")

# programming

class Python_View(ListView):
    model = Article
    template_name = 'articles/programming/python.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="python")).order_by("-id")

class Cpluplus_View(ListView):
    model = Article
    template_name = 'articles/programming/cplusplus.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="c++")).order_by("-id")

class Javascript_View(ListView):
    model = Article
    template_name = 'articles/programming/javascript.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="javascript")).order_by("-id")

class Golang_View(ListView):
    model = Article
    template_name = 'articles/programming/golang.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(Q(category__title__icontains="golang")).order_by("-id")