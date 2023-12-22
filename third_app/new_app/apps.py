from django import apps


class NewAppConfig(apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'new_app'
    verbose_name = 'New App'


# user_model = apps.get_model('new_app1.Product')
# user_model = apps.get_model('new_app1.SKU')