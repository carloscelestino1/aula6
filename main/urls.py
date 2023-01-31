from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),
    path('aluno/<int:id>', views.alunoIdView, name='aluno-view'),
    path('newaluno/', views.newAluno, name='new-aluno'),
    path('edit/<int:id>', views.editAluno, name="edit-aluno"),
    path('delete/<int:id>', views.deleteAluno, name="delete-aluno"),
]

