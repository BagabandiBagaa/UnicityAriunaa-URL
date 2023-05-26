from . import views
from  django.urls import path

app_name = 'products'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:item_id>/',views.details,name='details'),
    path('Category/<str:item_type>/',views.sortt,name='sortt'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('order/',views.order,name='order'),
    path('success/',views.success,name='success'),


]