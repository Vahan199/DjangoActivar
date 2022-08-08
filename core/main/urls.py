from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='home'),
    path('about-us/', views.AboutListView.as_view(), name='about'),
    path('schedule/', views.ScheduleListView.as_view(), name='sched'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog-single/', views.BlogDetailListView.as_view(), name='blogs'),
    path('contact/', views.ContactDetailView.as_view(), name='contact'),




]