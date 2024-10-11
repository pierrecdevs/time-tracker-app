from django.urls import path


from .views import delete_entry, delete_untracked_entry, edit_entry, edit_task, project, projects, edit_project, task
from .api import api_start_timer, api_stop_timer, api_discard_timer
app_name='project'

 # TODO:
 # change the way the CRUD operations work.)
urlpatterns = [
    path('', projects, name='projects'),
    path('<int:project_id>/', project, name='project'),
    path('<int:project_id>/<int:task_id>/', task, name='task'),
    path('<int:project_id>/<int:task_id>/edit/', edit_task, name='edit_task'),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/edit/', edit_entry, name='edit_entry'),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/delete/', delete_entry, name='delete_entry'),
    path('<int:project_id>/edit/', edit_project, name='edit_project'),
    path('delete_untracked_entry/<int:entry_id>/', delete_untracked_entry, name='delete_untracked_entry'),

    path('api/start_timer/', api_start_timer, name='api_start_timer'),
    path('api/stop_timer/', api_stop_timer, name='api_stop_timer'),
    path('api/discard_timer/', api_discard_timer, name='api_discard_timer'),
]
