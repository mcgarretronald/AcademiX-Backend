from django.urls import path
from .views import SchoolCreate, SchoolUpdate, SchoolDelete

urlpatterns = [
    # School urls
    path('schools/', SchoolCreate.as_view(), name='school_create'),  # Create School
    path('schools/<int:pk>/update/', SchoolUpdate.as_view(), name='school_update'),  # Update School
    path('schools/<int:pk>/delete/', SchoolDelete.as_view(), name='school_delete'),  # Delete School
]
