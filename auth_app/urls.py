from django.conf.urls import url
from auth_app import views

#TEMPLATE URLS!
app_name = 'auth_app'

urlpatterns = [
    url(r'^register/', views.register, name='register'),
   # url(r'^login/', views.login, name='login'),
]
