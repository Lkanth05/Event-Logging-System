
# Event Logging System

## **Overview**
The Event Logging System is a scalable and tamper-proof backend solution for logging events in distributed applications. It is built using **FastAPI** for the RESTful API, **MongoDB** for storage, and incorporates features like cryptographic hashing to ensure data integrity.

---

## **Features**
1. **Event Logging API**: 
   - Accepts logs with metadata (type, timestamp, source ID, and payload).
2. **Tamper-Proof Design**:
   - Lightweight blockchain-inspired log chaining using cryptographic hashes.
3. **Search and Query**:
   - Query logs by timestamp range, type, and source ID.
4. **Scalability**:
   - MongoDB indexing and sharding for large datasets.
5. **Error Handling**:
   - Validation and handling of invalid or missing data.

---

## **Technologies Used**
- **FastAPI**: For building the RESTful API.
- **MongoDB**: To store the event logs with indexing and sharding.
- **Pymongo**: Python MongoDB driver for database interactions.
- **Uvicorn**: ASGI server to run the FastAPI application.
- **Pydantic**: For data validation and modeling.

---

## **Getting Started**

### **1. Prerequisites**
Ensure the following are installed on your system:
- Python (version 3.8 or higher)
- MongoDB (local or cloud instance like MongoDB Atlas)
- Git

---

### **2. Installation Steps**

#### Clone the Repository
```bash
git clone <repository-url>
cd event_logging_system
```

#### Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

#### Set Up MongoDB
1. Start your MongoDB server locally or create a cluster using **MongoDB Atlas**.
2. Add the MongoDB connection URI to a `.env` file:
   ```plaintext
   MONGO_URI = "mongodb+srv://<Event_logging_system>:<event_log_5>@ai.yafsy1w.mongodb.net/?retryWrites=true&w=majority&appName=AI"
   Modify Event_logging_system and event_log_5 with your actual username and password of you MongoDB atlas.
---

### **3. Project Structure**
```
event_logging_system/
├── app/
│   ├── __init__.py          # Package initializer
│   ├── main.py              # Application entry point
│   ├── models.py            # Data models using Pydantic
│   ├── routes.py            # API routes
│   ├── database.py          # MongoDB connection setup
│   └── controllers.py       # Business logic and controllers
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

---

### **4. Running the Application**
Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

---

### **5. API Endpoints**

#### **1. Submit an Event Log**
**POST** `/api/v1/events`
- **Body Example**:
  ```json
  {
    "event_type": "user_login",
    "timestamp": "2024-11-23T12:34:56",
    "source_id": "app123",
    "payload": {
      "username": "user1",
      "ip": "192.168.1.1"
    }
  }
  ```

#### **2. Query Event Logs**
**GET** `/api/v1/events`
- **Query Parameters**:
  - `start_time`: Start of the timestamp range.
  - `end_time`: End of the timestamp range.
  - `event_type`: Filter by event type.
  - `source_id`: Filter by source application ID.

#### **3. Real-time Updates (Optional)**
If implemented, a WebSocket or SSE endpoint will allow real-time streaming of logs.

---

### **6. Testing**
Run stress tests using tools like **Postman** or **locust**:
- Test POST requests with large payloads.
- Query with filters and validate performance.

---

## **Future Enhancements**
- Implement WebSocket for real-time log streaming.
- Add dashboard for visualizing event logs and chain consistency.
- Introduce consensus mechanisms for decentralized server operations.

---

## **License**
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---



This `README.md` serves as a detailed guide for setting up, running, and understanding the project. Let me know if you need help customizing any part!