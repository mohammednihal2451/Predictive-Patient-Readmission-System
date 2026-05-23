from django.db import models


class Patient(models.Model):

    patient_id = models.CharField(max_length=100)

    name = models.CharField(max_length=200)

    age = models.IntegerField()

    gender = models.CharField(max_length=20)

    diagnosis = models.CharField(max_length=200)

    insurance_type = models.IntegerField(default=0)

    socioeconomic_risk_score = models.FloatField(default=0)

    previous_admissions_6m = models.IntegerField()

    previous_readmissions_1y = models.IntegerField()

    time_since_last_discharge = models.IntegerField(default=0)

    length_of_stay = models.IntegerField()

    admission_type = models.IntegerField(default=0)

    primary_diagnosis_group = models.IntegerField(default=0)

    comorbidity_index = models.FloatField(default=0)

    chronic_disease_count = models.IntegerField(default=0)

    icu_stay_flag = models.IntegerField(default=0)

    severity_score = models.FloatField()

    hba1c_level = models.FloatField()

    creatinine_level = models.FloatField()

    hemoglobin_level = models.FloatField()

    average_systolic_bp = models.FloatField()

    number_of_medications = models.IntegerField(default=0)

    medication_change_count = models.IntegerField(default=0)

    high_risk_medication_flag = models.IntegerField(default=0)

    followup_appointment_scheduled = models.IntegerField(default=0)

    discharge_disposition = models.IntegerField(default=0)

    medication_adherence_score = models.FloatField()

    probability_score = models.FloatField(default=0)

    risk_level = models.CharField(
        max_length=50,
        default='Low'
    )

    prediction = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name