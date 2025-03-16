from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class LogEntry(Base):
    __tablename__ = "api_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    algorithm_name = Column(String, nullable=False)
    input_data = Column(Text, nullable=False)
    output_data = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

