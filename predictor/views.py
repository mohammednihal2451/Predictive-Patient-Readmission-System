import numpy as np

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Patient
from .serializers import PatientSerializer
from .ml_model import model


@api_view(['GET'])
def home(request):

    return Response({

        "message": "Predictive Patient Readmission API Running"
    })


@api_view(['POST'])
def predict_readmission(request):

    try:

        data = request.data

        features = np.array([[

            float(data.get('age', 0)),

            1 if data.get('gender', '').lower() == 'male' else 0,

            float(data.get('insurance_type', 0)),

            float(data.get('socioeconomic_risk_score', 0)),

            float(data.get('previous_admissions_6m', 0)),

            float(data.get('previous_readmissions_1y', 0)),

            float(data.get('time_since_last_discharge', 0)),

            float(data.get('length_of_stay', 0)),

            float(data.get('admission_type', 0)),

            float(data.get('primary_diagnosis_group', 0)),

            float(data.get('comorbidity_index', 0)),

            float(data.get('chronic_disease_count', 0)),

            float(data.get('icu_stay_flag', 0)),

            float(data.get('severity_score', 0)),

            float(data.get('hba1c_level', 0)),

            float(data.get('creatinine_level', 0)),

            float(data.get('hemoglobin_level', 0)),

            float(data.get('average_systolic_bp', 0)),

            float(data.get('number_of_medications', 0)),

            float(data.get('medication_change_count', 0)),

            float(data.get('high_risk_medication_flag', 0)),

            float(data.get('followup_appointment_scheduled', 0)),

            float(data.get('discharge_disposition', 0)),

            float(data.get('medication_adherence_score', 0))

        ]])

        prediction = model.predict(features)[0]

        probability = model.predict_proba(features)[0][1]

        risk_level = "Low"

        if probability > 0.7:

            risk_level = "High"

        elif probability > 0.4:

            risk_level = "Medium"

        patient = Patient.objects.create(

            patient_id=data.get('patient_id'),

            name=data.get('name'),

            age=data.get('age'),

            gender=data.get('gender'),

            diagnosis=data.get('diagnosis'),

            insurance_type=data.get('insurance_type', 0),

            socioeconomic_risk_score=data.get('socioeconomic_risk_score', 0),

            previous_admissions_6m=data.get('previous_admissions_6m'),

            previous_readmissions_1y=data.get('previous_readmissions_1y'),

            time_since_last_discharge=data.get('time_since_last_discharge', 0),

            length_of_stay=data.get('length_of_stay'),

            admission_type=data.get('admission_type', 0),

            primary_diagnosis_group=data.get('primary_diagnosis_group', 0),

            comorbidity_index=data.get('comorbidity_index', 0),

            chronic_disease_count=data.get('chronic_disease_count', 0),

            icu_stay_flag=data.get('icu_stay_flag', 0),

            severity_score=data.get('severity_score'),

            hba1c_level=data.get('hba1c_level'),

            creatinine_level=data.get('creatinine_level'),

            hemoglobin_level=data.get('hemoglobin_level'),

            average_systolic_bp=data.get('average_systolic_bp'),

            number_of_medications=data.get('number_of_medications', 0),

            medication_change_count=data.get('medication_change_count', 0),

            high_risk_medication_flag=data.get('high_risk_medication_flag', 0),

            followup_appointment_scheduled=data.get('followup_appointment_scheduled', 0),

            discharge_disposition=data.get('discharge_disposition', 0),

            medication_adherence_score=data.get('medication_adherence_score'),

            probability_score=round(probability * 100, 2),

            risk_level=risk_level,

            prediction=int(prediction)
        )

        serializer = PatientSerializer(patient)

        return Response(serializer.data)

    except Exception as e:

        return Response({

            "error": str(e)
        })


@api_view(['GET'])
def patient_list(request):

    patients = Patient.objects.all().order_by('-created_at')

    serializer = PatientSerializer(
        patients,
        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])
def dashboard_stats(request):

    total_patients = Patient.objects.count()

    high_risk = Patient.objects.filter(
        risk_level='High'
    ).count()

    medium_risk = Patient.objects.filter(
        risk_level='Medium'
    ).count()

    low_risk = Patient.objects.filter(
        risk_level='Low'
    ).count()

    return Response({

        "total_patients": total_patients,

        "high_risk": high_risk,

        "medium_risk": medium_risk,

        "low_risk": low_risk
    })


@api_view(['GET'])
def chart_data(request):

    high = Patient.objects.filter(
        risk_level='High'
    ).count()

    medium = Patient.objects.filter(
        risk_level='Medium'
    ).count()

    low = Patient.objects.filter(
        risk_level='Low'
    ).count()

    return Response({

        "labels": ["High Risk", "Medium Risk", "Low Risk"],

        "data": [high, medium, low]
    })


@api_view(['GET'])
def recent_patients(request):

    patients = Patient.objects.all().order_by(
        '-created_at'
    )[:5]

    serializer = PatientSerializer(
        patients,
        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])
def alerts(request):

    patients = Patient.objects.filter(
        risk_level='High'
    )

    alert_data = []

    for patient in patients:

        alert_data.append({

            "patient_name": patient.name,

            "risk_level": patient.risk_level,

            "probability": patient.probability_score,

            "message": f"{patient.name} is high risk"
        })

    return Response(alert_data)


@api_view(['PUT'])
def update_patient(request, id):

    try:

        patient = Patient.objects.get(id=id)

        serializer = PatientSerializer(
            patient,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    except Patient.DoesNotExist:

        return Response({

            "error": "Patient not found"
        })


@api_view(['DELETE'])
def delete_patient(request, id):

    try:

        patient = Patient.objects.get(id=id)

        patient.delete()

        return Response({

            "message": "Patient deleted successfully"
        })

    except Patient.DoesNotExist:

        return Response({

            "error": "Patient not found"
        })