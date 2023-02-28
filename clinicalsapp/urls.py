from django.urls import path
from . import views

app_name="clinicals"
urlpatterns=[
    path("home",views.home,name='home'),
    path('index',views.index,name='index'),
    path('listview',views.PatientListView.as_view(),name='list'),
    path('createview',views.PatientCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.PatientUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.PatientDeleteView.as_view(),name='delete'),
    path('register',views.register,name='register'),
    path('adddata/<int:pk>',views.addData,name='adddata'),
    path('email/<int:pk>',views.sendmail,name="email")

]