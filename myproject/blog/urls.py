from django.urls import path
from . import views
urlpatterns = [
    path('view/<slug:slug_text>',views.view, name='view'),
    path('programming/',views.programming, name='programming'),
    path('tech/',views.tech, name='tech'),
    path('life/',views.life, name='life'),
    path('',views.index, name='index')
]