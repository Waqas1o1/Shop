from django.urls import path
from . import views
urlpatterns = [
    path('serach/<str:ctg>',views.Search,name='serachItems')
]