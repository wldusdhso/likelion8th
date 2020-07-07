from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('<int:blog_id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create, name = "create"),
    path('edit/<int:blog_id>', views.edit, name="edit"),
    path('update/<int:blog_id>', views.update, name="update"),
    path('delete/<int:blog_id>', views.delete, name="delete"),
    path('commenting/<int:blog_id>', views.commenting, name="commenting"),
    path('like/<int:blog_id>', views.like, name="like"),
    path('comment_delete/<int:blog_id>/<int:comment_id>', views.comment_delete, name="comment_delete"),
]
