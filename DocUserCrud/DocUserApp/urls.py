from django.urls import path
from . import views  

urlpatterns = [
    path('api/users/create_user/', views.create_user, name='create_user'),
    path('api/users/<int:pk>/', views.user_detail, name='user_detail'),
    path('api/users/', views.list_user, name='list_user'),
    path('api/users/<int:pk>/update/', views.update_user, name='update_user'),

    path('api/docs/create_doc/', views.list_doc, name='create_doc'),
    path('api/docs/<int:pk>/', views.doc_detail, name='doc_detail'),
    path('api/docs/', views.list_doc, name='list_doc'),
    path('api/docs/<int:pk>/update/', views.update_doc, name='update_doc'),

    path('api/companies/create_company/', views.list_company, name='create_company'),
    path('api/companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('api/companies/', views.list_company, name='list_company'),
    path('api/companies/<int:pk>/update/', views.update_company, name='update_company'),
]