from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.database import Base


class Appointment(Base):
    __tablename__ = "vaishnavik_appointments"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("vaishnavik_patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("vaishnavik_doctors.id"), nullable=False)

    start_time = Column(DateTime(timezone=True), nullable=False)
    duration_minutes = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
