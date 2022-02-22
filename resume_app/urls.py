from django.urls import path
from . import views, views2


urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download_file, name='download'),
    path('downloadpdf/', views2.download_pdf_file, name='download_pdf_file'),
    path('downloadpdf//', views2.download_pdf_file, name='download_pdf_file'),
]