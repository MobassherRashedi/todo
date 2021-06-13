from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import TodoListView, TodoDetailView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name = 'mytodolist'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)