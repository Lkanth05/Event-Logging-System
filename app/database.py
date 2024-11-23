from pymongo import MongoClient

# Replace the below string with your MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://<Event_logging_system>:<event_log_5>@ai.yafsy1w.mongodb.net/?retryWrites=true&w=majority&appName=AI"

# Create a MongoDB client
client = MongoClient(MONGO_URI)

# Connect to the database
db = client["Event_logging_system"]  # Replace with your database name

# Example: Accessing a collection
event_logs_collection = db["event_logs"]

print("Connected to MongoDB Atlas successfully!")
