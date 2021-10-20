from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('techniques/all/', views.all_techniques, name='bjj-all'),
    path('techniques/any/', views.random_technique, name='bjj-random'),
    path('techniques/<int:pk>/', views.technique_by_id, name='bjj-id'),
    path('techniques/type/<str:tech_type>/', views.techniques_by_type, name='bjj-type'),
    path('techniques/difficulty/<str:tech_difficulty>/', views.techniques_by_difficulty, name='bjj-diff'),
    path('techniques/name/<str:tech_name>/', views.technique_by_name, name='bjj-name'),
    path('techniques/t-d/<str:tech_type>/<str:tech_difficulty>/', views.techs_by_type_diff, name='bjj-type-diff'),
    path('techniques/create/', views.create_technique, name='bjj-create'),
    path('techniques/update/<int:pk>/', views.update_technique, name='bjj-update'),
    path('techniques/delete/<int:pk>/', views.delete_technique, name='bjj-delete'),
]