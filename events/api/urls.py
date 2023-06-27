
from django.urls import path, include
from . import views

urlpatterns = [path('events/', views.EventApiViews.as_view()),
                path("users/", views.ListUsersAPIViews.as_view()),
               path("event/<int:pk>/", views.ParticipateAPIEvent.as_view())
]