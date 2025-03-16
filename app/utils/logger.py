from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.database.models import LogEntry

import json
import logging

# Configure logging for file-based error logs
logging.basicConfig(filename="app_logs.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def log_api_call(algorithm_name: str, input_data: dict, output_data: dict):
    """
    Logs API calls to the database.
    """
    db: Session = None
    try:
        db = SessionLocal()
        log_entry = LogEntry(
            algorithm_name=algorithm_name,
            input_data=json.dumps(input_data, indent=2),
            output_data=json.dumps(output_data, indent=2)
        )
        db.add(log_entry)
        db.commit()
    except Exception as e:
        logging.error(f"Database Logging Failed: {str(e)}")
    finally:
        if db:
            db.close()

def log_error(error_message: str):
    """
    Logs errors to both the file and the database.
    """
    logging.error(error_message)

    # Also log the error to the database
    db: Session = None
    try:
        db = SessionLocal()
        log_entry = LogEntry(
            algorithm_name="Error",
            input_data=json.dumps({"error": "N/A"}),  
            output_data=json.dumps({"error_message": error_message})
        )
        db.add(log_entry)
        db.commit()
    except Exception as e:
        logging.error(f"Database Error Logging Failed: {str(e)}")
    finally:
        if db:
            db.close()
