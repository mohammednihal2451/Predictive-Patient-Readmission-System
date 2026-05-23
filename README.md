# Predictive Patient Readmission System

A Machine Learning based Healthcare Analytics System that predicts whether a patient is likely to be readmitted to the hospital.

---

# Features

- Patient Readmission Prediction
- Risk Level Detection
- REST API using Django REST Framework
- Dashboard Analytics
- Patient Management
- Chart Data API
- Alerts System
- CRUD Operations
- Machine Learning Integration

---

# Technologies Used

## Backend
- Django
- Django REST Framework
- SQLite

## Machine Learning
- Scikit-learn
- Pandas
- NumPy

## Tools
- Postman
- GitHub
- VS Code

---

# Project Structure

```bash
Predictive-Patient-Readmission-System/
│
├── backend/
│   ├── predictor/
│   ├── backend/
│   ├── manage.py
│
├── model/
├── dataset/
├── README.md
└── requirements.txt
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Predictive-Patient-Readmission-System.git
```

---

## Navigate to Backend

```bash
cd backend
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Server

```bash
python manage.py runserver
```

Server URL:

```text
http://127.0.0.1:8000/
```

---

# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/ | Home API |
| POST | /api/predict/ | Predict Readmission |
| GET | /api/patients/ | Patient List |
| GET | /api/dashboard/ | Dashboard Statistics |
| GET | /api/chart-data/ | Chart Analytics |
| GET | /api/recent-patients/ | Recent Patients |
| GET | /api/alerts/ | High Risk Alerts |
| PUT | /api/update-patient/<id>/ | Update Patient |
| DELETE | /api/delete-patient/<id>/ | Delete Patient |

---

# Machine Learning Features

- Age
- Gender
- Insurance Type
- Severity Score
- HbA1c Level
- Creatinine Level
- Medication Adherence
- Previous Admissions
- ICU Stay Flag
- Comorbidity Index
- Chronic Disease Count

---

# Sample Prediction Output

```json
{
    "patient_id": "P1001",
    "name": "John Doe",
    "risk_level": "High",
    "probability_score": 77.44,
    "prediction": 1
}
```

---

# Future Enhancements

- JWT Authentication
- PDF Report Export
- Email Notifications
- React Frontend
- Cloud Deployment
- AI Visualization Dashboard

---

# Author

Mohammad Nihal

---

# License

This project is for educational and academic purposes.