# HNG Stage 0 Task API

A simple FastAPI application that calls an external API and returns a random cat fact with rate limiting and logging.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **External API Integration**: Fetches random cat facts from [catfact.ninja](https://catfact.ninja/)
- **Rate Limiting**: Protects endpoints from abuse with configurable limits
- **Comprehensive Logging**: Detailed logging for debugging and monitoring
- **Clean Architecture**: Well-structured codebase following best practices

## 📋 API Endpoints

### `GET /me`
Returns user information along with a random cat fact.

**Rate Limit**: 5 requests per minute

**Response**:
```json
{
  "status": "success",
  "user": {
    "email": "balogunafebu22@@gmail.com",
    "name": "Balogun Afebu",
    "stack": "backend"
  },
  "timestamp": "2024-01-15T10:30:00.000Z",
  "fact": "A random cat fact from the external API"
}
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd intro_proj
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Application

### Development Mode
```bash
uvicorn app.main:app --reload
```

The application will be available at:
- **API**: http://localhost:8000
- **Interactive API Docs**: http://localhost:8000/docs

### Production Mode
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 📁 Project Structure

```
api/
├── __init__.py          # Package initialization
├── main.py             # App initialization, middleware, rate 
```

### File Responsibilities

- **`main.py`**: FastAPI app initialization, rate limiting configuration, and router setup

## 🧪 Testing the API

### Using curl

**Test the root endpoint:**
```bash
curl http://localhost:8000/
```

**Test the user info endpoint:**
```bash
curl http://localhost:8000/me
```

### Using the Interactive Docs
Visit http://localhost:8000/docs to test the API endpoints directly in your browser.


## 📦 Dependencies

- **FastAPI**: Web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applicationsfix: 

## 📄 License

This project is part of the HNG Internship Stage 0 Task.