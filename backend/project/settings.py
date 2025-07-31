# backend/project/settings.py
INSTALLED_APPS = [
    'rest_framework',          
    'app',     
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',           
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]