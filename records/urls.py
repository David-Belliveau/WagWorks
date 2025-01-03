from django.urls import path
from . import views
# from .views import MultiStepFormView


urlpatterns = [
    path("", views.index, name="index"),
    # path("register/", views.register, name="register"),
    path("about", views.about, name="about"),
    path("success/", views.success, name="success"),
    path("mission/", views.mission, name="mission"),
    # path("register2", views.register2, name="register2"),
    # path('register2/', RegistrationWizard.as_view(forms), name='register2')
    path('pet-info/', views.pet_info_view, name='pet_info'),
    # path('diagnosis/<int:pet_id>/', views.diagnosis_view, name='diagnosis'),
    # path('treatment/<int:pet_id>/', views.treatment_view, name='treatment'),
    # path('long-term/<int:pet_id>/', views.long_term_view, name='long_term'),
    # path('upload-docs/<int:pet_id>/', views.upload_docs_view, name='upload_docs'),
    # path('thank-you/', views.thank_you_view, name='thank_you'),
]

