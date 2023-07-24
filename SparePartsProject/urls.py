from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='AddSparePart'),
    path('add/addSparePart/', views.addSparePart, name='SparePart'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('update/<int:id>', views.update, name='update'),
    # path('update/updateSparePart/<int:id>',views.updateSparePart, name='updateSparePart'),
]