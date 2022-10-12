from django.urls import path
from .views import addParentCategoryView, getParentCategoryView

urlpatterns = [
    path('addParentCategory', addParentCategoryView.as_view(), name= 'addParentCategory'),
    path('getParentCategory', getParentCategoryView.as_view(), name= 'getParentCategory'),
]
