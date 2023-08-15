from django.urls import path
from . import views
urlpatterns = [
    path('',  views.home),
    path('new_work/', views.store_work, name='storeWork'),
    path('show_work/', views.show_works, name='show_works'),
    path('edit_work/<int:id>', views.edit_work, name='edit_work'),
    path('delete_work/<int:id>', views.delete_work, name='delete_work'),
    path('complete_work/<int:id>', views.complete_task, name='complete_work'),
    path('completed_work/', views.completed_tasks, name='completed_work'),
]