from django.urls import path

from . import views
# from core.urls import urlpatterns
from .views import *

app_name = 'products'

urlpatterns = [
    path('', view=views.home, name='index'),

]