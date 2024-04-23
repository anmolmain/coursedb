from django.contrib import admin
from django.urls import path
from courseapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('courses/', views.courses,name="courses"),
    path('codeeditor/', views.codeeditor,name="codeeditor"),
    path('pricing/', views.pricing,name="pricing"),
    path('contactus/', views.contactus, name='contactus'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("css/", views.css, name="css"),
    path("html/", views.html, name="html"),
    path("Javascript/", views.Javascript, name="Javascript"),
    path("Bootstrap/", views.Bootstrap, name="Bootstrap"),
    path("ExpressJs/", views.ExpressJs, name="ExpressJs"),
    path("React/", views.React, name="React"),
    path("NodeJs/", views.NodeJs, name="NodeJs"),
    path("MongoDB/", views.MongoDB, name="MongoDB"),

]