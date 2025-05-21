from django.apps import AppConfig


class AppdictConfig(AppConfig):
    default_auto_field = 'django_mongodb_backend.fields.ObjectIdAutoField'
    name = 'appdict'
