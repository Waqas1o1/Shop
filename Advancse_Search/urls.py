from django.urls import path

urlpatterns = [
    path('search_item/<str:ctg>',views.Search,name='serachItems')
]