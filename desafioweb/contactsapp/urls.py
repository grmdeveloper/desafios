from django.urls import path
from .views import home, list, delete

urlpatterns = [
    path('', home),
    path('list/', list),
    path('list/delete/<int:id>', delete)
]