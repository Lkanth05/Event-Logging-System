from fastapi import APIRouter, Query
from .controllers import create_log, query_logs

router = APIRouter()

# Route to fetch logs with query parameters
@router.get("/log")
async def get_logs(
    event_type: str = Query(None, description="Filter logs by event type"),
    timestamp_range: str = Query(None, description="Filter logs by a timestamp range (start,end)"),
    source_app_id: str = Query(None, description="Filter logs by source app ID"),
):
    # Build the filters dictionary
    filters = {}
    if event_type:
        filters["event_type"] = event_type
    if timestamp_range:
        # Parse the timestamp range into a list of [start, end]
        try:
            start, end = timestamp_range.split(",")
            filters["timestamp_range"] = [start, end]
        except ValueError:
            return {"error": "Invalid timestamp_range format. Use 'start,end'."}
    if source_app_id:
        filters["source_app_id"] = source_app_id

    # Call the query_logs function with the filters
    logs = query_logs(filters)
    return logs

# Route to create a log
@router.post("/log")
async def add_log(event_data: dict):
    log = create_log(event_data)
    return log
