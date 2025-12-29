# GitHub Copilot Instructions - OctoFit Tracker

## Project Overview
OctoFit Tracker is a full-stack fitness application with Django REST backend and React frontend, deployed in GitHub Codespaces. It supports user authentication, activity logging, team management, competitive leaderboards, and personalized workout suggestions.

**Architecture:** Django + DRF + MongoDB (via djongo) + React + Bootstrap

## Critical Commands & Workflows

### Environment & Virtual Environment
```bash
# Activate Python venv (always do this before Django work)
source octofit-tracker/backend/venv/bin/activate

# Install backend dependencies (if requirements.txt changes)
pip install -r octofit-tracker/backend/requirements.txt

# Check MongoDB is running
ps aux | grep mongod
```

### Backend Development
```bash
# Run Django development server (port 8000)
python manage.py runserver 0.0.0.0:8000

# Create Django app/models
python manage.py startapp <app_name>

# Test endpoints
curl http://localhost:8000/api/
```

### Frontend Development
```bash
# Start React dev server (port 3000)
npm start --prefix octofit-tracker/frontend

# Install new packages
npm install <package> --prefix octofit-tracker/frontend
```

## Codespace-Specific Configuration

**Critical:** The app detects GitHub Codespace environment via `CODESPACE_NAME` variable.

- **Django `settings.py`:** Must include:
  ```python
  import os
  ALLOWED_HOSTS = ['localhost', '127.0.0.1']
  if os.environ.get('CODESPACE_NAME'):
      ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")
  ```

- **Django `urls.py`:** Build dynamic base_url:
  ```python
  import os
  codespace_name = os.environ.get('CODESPACE_NAME')
  if codespace_name:
      base_url = f"https://{codespace_name}-8000.app.github.dev"
  else:
      base_url = "http://localhost:8000"
  ```

## Port Configuration
**Only these ports are forwarded:**
- **8000** (Django backend) - PUBLIC
- **3000** (React frontend) - PUBLIC  
- **27017** (MongoDB) - PRIVATE

Do NOT propose alternative ports or make others public.

## Project Structure & Patterns

```
octofit-tracker/
├── backend/
│   ├── venv/                    # Python virtual environment
│   ├── octofit_tracker/         # Django project root
│   ├── requirements.txt         # Python dependencies
│   └── manage.py
├── frontend/
│   ├── src/
│   │   ├── index.js            # Must import Bootstrap CSS first
│   │   ├── App.js
│   │   └── components/
│   └── package.json
└── docs/
    ├── octofitapp-small.png    # App logo/image
    └── octofit_story.md        # Business requirements
```

## Technology Stack & Key Conventions

### Backend (Django)
- **Framework:** Django 4.1.7 + Django REST Framework 3.14.0
- **Database:** MongoDB via djongo (1.3.6) + pymongo (3.12)
- **Auth:** django-allauth + dj-rest-auth for REST authentication
- **CORS:** django-cors-headers for frontend communication
- **Serializers:** Must convert ObjectId fields to strings for REST responses
- **Testing:** Use curl for endpoint verification

### Frontend (React)
- **Bootstrap 4** for styling - CSS import MUST be first in `src/index.js`
- **React Router DOM** for navigation
- **Logo location:** `docs/octofitapp-small.png`

## Directory Command Patterns

**Critical rule:** Never `cd` into directories during agent commands. Instead, point to the directory:

❌ **Wrong:**
```bash
cd octofit-tracker/backend && python manage.py runserver
```

✅ **Correct:**
```bash
python octofit-tracker/backend/manage.py runserver 0.0.0.0:8000
```

## Database Management

- **Always use Django ORM**, not direct MongoDB scripts
- Use `python manage.py makemigrations` and `python manage.py migrate` for schema changes
- MongoDB connection configured via djongo in Django settings
- No direct mongosh/mongo shell commands for data creation

## App Goals (Reference)
1. User authentication and profiles
2. Activity logging and tracking  
3. Team creation and management
4. Competitive leaderboard
5. Personalized workout suggestions
