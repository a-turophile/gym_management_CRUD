from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url


app_name = 'gym'

urlpatterns = [

    path('', views.register, name = 'member_insert'), #get request to retrieve and display all records
    path('<int:id>/', views.register, name='member_update'), #get and post request for update
    path('list/', views.member_list, name = 'member_show'), #get and post request for insert
    path( 'delete/<int:id>/', views.member_delete, name = 'member_delete'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]