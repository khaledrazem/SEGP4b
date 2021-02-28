"""project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('About/',views.about, name="about"),
    path('Topics/',views.topic, name="topic"),
    path('Case1/',views.case1, name="case1"),
    path('Case2/',views.case2, name="case2"),
    path('Results1/',views.results1, name="r1"),
    path('Results2/',views.results2, name="r2"),
    path('Testing/',views.testing, name="test"),
    path('SingleCategoryResult/',views.single_category, name="single_category"),
    path('SingleKeywordResult/',views.single_keyword_result, name="single_keyword"),
    path('KeywordCombination/',views.keyword_combination_result, name="keyword_combination"),
    path('SubcategoryCombination/',views.subcategory_combination_result, name="keyword_combination"),]