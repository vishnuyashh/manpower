from django.urls import path
from.import views
app_name='jobseeker'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about')
]