from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('form/', views.form, name="form"),
    path('empty/', views.empty, name="empty"),
    path('table/', views.table, name="table"),
    path('download-csv', views.download_csv, name='download_csv'),
    path('api/upload-csv', views.upload_csv, name='upload_csv'),
    path('upload_csv/', views.upload_csv, name="upload_csv"),

]