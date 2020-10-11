from django.contrib import admin
from django.urls import path
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main_page)
]

for module in main_views.load_modules():
    urlpatterns.append(
        path(
            module['id'],
            main_views.module_page
        )
    )
