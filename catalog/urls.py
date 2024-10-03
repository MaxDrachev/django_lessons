from django.urls import path, include
from catalog.apps import CatalogConfig
<<<<<<< HEAD
from catalog.views import home_page, contacts_page
=======
>>>>>>> origin/main

app_name = CatalogConfig.name

urlpatterns = [
<<<<<<< HEAD
    path('', home_page, name='home_page'),
    path('contacts/', contacts_page, name='contacts_page')
=======
    path('',)
>>>>>>> origin/main
]
