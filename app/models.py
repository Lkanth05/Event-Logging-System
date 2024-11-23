from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime

class EventLog(BaseModel):
    event_type: str = Field(..., example="Error")
    timestamp: datetime = Field(..., example="2024-11-23T12:00:00Z")
    source_app_id: str = Field(..., example="App123")
    data_payload: Dict = Field(..., example={"key": "value"})
    hash: str = Field(..., example="current_log_hash")
    previous_hash: str = Field(..., example="previous_log_hash")
