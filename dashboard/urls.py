from django.urls import path
from .views import DashboardView, AdminPanelView, ProfileUpdateView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
    path("admin-panel/", AdminPanelView.as_view(), name="admin_panel"),
]
