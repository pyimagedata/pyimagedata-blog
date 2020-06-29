from django.urls import path
from .views import *

urlpatterns = [
    path('',Index_View.as_view(),name='index'),
    path('detail/<int:pk>/<slug:slug>/',Detail_View.as_view(),name='detail'),
    path('category/<slug:slug>/<int:pk>/',Category_View.as_view(),name='category'),
    path('tag/<slug:slug>/<int:pk>/',Tag_View.as_view(),name='tag'),
    path('search/',Search_View.as_view(),name='searchh'),
    # ai
    path('artificial-intelligence/deep-learning',DeepLearning_View.as_view(),name='deep_learning'),
    path('artificial-intelligence/machine-learning',MachineLearning_View.as_view(),name='machine_learning'),
    path('artificial-intelligence/reinforcement-learning',RF_View.as_view(),name='rf_learning'),
    path('artificial-intelligence/datascience',Datascience_View.as_view(),name='datascience'),
    # computer vision

    path('computer-vision/image-processing',Image_Processing_View.as_view(),name='image_processing'),
    path('computer-vision/opencv',Opencv_View.as_view(),name='opencv'),
    path('computer-vision/r-cnn',RCNN_View.as_view(),name='r_cnn'),
    path('computer-vision/yolo',Yolo_View.as_view(),name='yolo'),

    # robotics

    path('robotics/ros',Ros_View.as_view(),name='ros'),
    path('robotics/raspberry-pi',RaspberryPi_View.as_view(),name='raspberry_pi'),
    path('robotics/arduino',Arduino_View.as_view(),name='arduino'),
    path('robotics/robot-arm',RobotArm_View.as_view(),name='robot_arm'),

    # programming

    path('programming/python',Python_View.as_view(),name='python'),
    path('programming/c++',Cpluplus_View.as_view(),name='cplusplus'),
    path('programming/javascript',Javascript_View.as_view(),name='javascript'),
    path('programming/golang',Golang_View.as_view(),name='golang'),



]
