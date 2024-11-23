import hashlib
from datetime import datetime
from .database import event_logs_collection


# Initialize the previous hash
previous_hash = "0"

def create_log(event_data):
    global previous_hash

    # Generate the hash for the current log
    log_data = {
        "event_type": event_data.event_type,
        "timestamp": event_data.timestamp,
        "source_app_id": event_data.source_app_id,
        "data_payload": event_data.data_payload,
        "previous_hash": previous_hash,
    }
    current_hash = hashlib.sha256(str(log_data).encode()).hexdigest()
    log_data["hash"] = current_hash

    # Save the log in the database
    event_logs_collection.insert_one(log_data)

    # Update the previous hash
    previous_hash = current_hash

    return log_data


def query_logs(filters):
    try:
        # Apply filters to the query
        query = {}
        if "event_type" in filters:
            query["event_type"] = filters["event_type"]
        if "timestamp_range" in filters:
            start, end = filters["timestamp_range"]
            query["timestamp"] = {"$gte": start, "$lte": end}
        if "source_app_id" in filters:
            query["source_app_id"] = filters["source_app_id"]

        # Query the database
        logs = list(event_logs_collection.find(query))
        
        # Convert ObjectId to string for serialization
        for log in logs:
            log["_id"] = str(log["_id"])
        
        return logs
    except Exception as e:
        return {"status": "error", "message": str(e)}

