from django.urls import path

from .views import *

urlpatterns = [

    path('', home),

    path('predict/', predict_readmission),

    path('patients/', patient_list),

    path('dashboard/', dashboard_stats),

    path('chart-data/', chart_data),

    path('recent-patients/', recent_patients),

    path('alerts/', alerts),

    path('update-patient/<int:id>/', update_patient),

    path('delete-patient/<int:id>/', delete_patient),
]