Medical Encounter Management System (MEMS)

A production-ready backend application for managing patients, doctors, and medical appointments.

Tech Stack
FastAPI
SQLAlchemy
MySQL
Pytest
GitHub Actions (CI)

Key Features
Patient creation and retrieval
Doctor management with activate and deactivate support
Appointment scheduling with conflict prevention
Timezone-aware datetime handling
Clean service-based architecture

Run Locally

pip install -r requirements.txt
uvicorn src.main:app --reload

Once running, open:
API Docs: http://127.0.0.1:8000/docs
Health Check: http://127.0.0.1:8000/health
