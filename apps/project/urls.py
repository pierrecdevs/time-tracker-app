from django.urls import path

from .views import delete_entry, edit_entry, edit_task, project, projects, edit_project, task

app_name = 'project'

 # TODO:
 # change the way the CRUD operations work. (i.e use proper GET, POST, PATCH/PUT, DELETE)
urlpatterns = [
    path('', projects, name='projects'),
    path('<int:project_id>/', project, name='project'),
    path('<int:project_id>/<int:task_id>/', task, name='task'),
    path('<int:project_id>/<int:task_id>/edit/', edit_task, name='edit_task'),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/edit/', edit_entry, name='edit_entry'),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/delete/', delete_entry, name='delete_entry'),
    path('<int:project_id>/edit/', edit_project, name='edit_project')
]
