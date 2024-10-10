from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home_page, contacts_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home_page'),
    path('contacts/', contacts_page, name='contacts_page')
]