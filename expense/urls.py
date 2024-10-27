from django.urls import path
from .views import *

urlpatterns = [
    path('', expense_list, name='expense_list'),
    path('create/', create_expense, name='create_expense'),
    path('update/<int:id>/', update_expense, name='update_expense'),
    path('delete/<int:id>/', delete_expense, name='delete_expense'),
]
