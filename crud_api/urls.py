from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/events/', views.get_events, name='get_events'),
    path('api/events/update/<int:event_id>', views.update_event, name='update_event'),
    path('api/events/delete/<int:event_id>', views.delete_event, name='delete_event'),
    path('api/events/create/', views.create_event, name='create_event'),
]