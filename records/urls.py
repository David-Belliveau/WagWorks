from django.urls import path
from . import views
# from .views import MultiStepFormView


urlpatterns = [
    path("", views.index, name="index"),
    path("register.html/", views.register, name="register"),
    path("about.html/", views.about, name="about"),
    path("success.html/", views.success, name="success"),
    path("mission.html/", views.mission, name="mission"),
    path("register2.html/", views.register2, name="register2"),
    # path('register2/', RegistrationWizard.as_view(forms), name='register2')
]


