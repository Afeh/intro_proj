# HNG13 Stage 0 Task

## Task Overview
A simple FastAPI app with a `/me` endpoint returning user profile info and a random cat fact.

---

## Setup Instructions

### 1 Clone the Repo
```bash
git clone https://github.com/<your-username>/backend-wizards-stage0.git
cd backend-wizards-stage0
```

### 2 Install Dependencies
```bash
pip install -r requirements.txt
```

### 3 Run the Server
```bash
uvicorn api.main:app --reload
```

### Example Response
```
{
  "status": "success",
  "user": {
    "email": "balogunafebu@gmail.com",
    "name": "Balogun Afebu",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T14:30:00Z",
  "fact": "Cats can rotate their ears 180 degrees."
}
```


