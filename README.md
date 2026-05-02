# ⛰️ Mountain Coders — Offline E-Learning Platform

**Mountain Coders** is a fully functional e-learning platform built for students in rural and mountain areas of India where internet connectivity is limited or unavailable.

## 🚀 Features
- **Offline-First**: Students can download lessons, PDFs, and materials
- **Free for All**: 100% free courses — no payment required
- **Multi-language**: Hindi and Hindi/English courses available
- **Quiz System**: MCQ quizzes with instant results and review
- **Progress Tracking**: Visual progress bars for each course
- **User Profiles**: Location-based profiles (village, district, state)
- **Admin Panel**: Full Django admin for content management
- **Responsive Design**: Works on mobile and desktop

## 📁 Project Structure
```
mountain_coders/
├── config/              # Django project settings & URLs
├── courses/             # Main app: courses, lessons, quizzes
├── users/               # Authentication & profiles
├── templates/           # HTML templates (base + all pages)
│   ├── base.html
│   ├── courses/
│   └── users/
├── static/
│   ├── css/main.css     # Full custom CSS (no framework)
│   └── js/main.js       # Interactive JS
├── media/               # Uploaded files (thumbnails, PDFs, videos)
├── db.sqlite3           # SQLite database
└── manage.py
```

## 🛠️ Tech Stack
- **Backend**: Django 4.x + Python
- **Database**: SQLite (production: PostgreSQL recommended)
- **Frontend**: Vanilla HTML5, CSS3, JavaScript
- **Fonts**: Google Fonts (Playfair Display + Nunito)
- **Auth**: Django built-in authentication

## ▶️ Running Locally

```bash
# 1. Install dependencies
pip install django pillow

# 2. Apply migrations
python manage.py migrate

# 3. Create superuser (if fresh install)
python manage.py createsuperuser

# 4. Run development server
python manage.py runserver

# Visit: http://127.0.0.1:8000
```

## 👤 Demo Accounts
| Role    | Username       | Password    |
|---------|----------------|-------------|
| Admin   | admin          | admin123    |
| Teacher | teacher_ravi   | teacher123  |
| Student | student_anita  | student123  |

## 🌐 Key URLs
| Page           | URL                    |
|----------------|------------------------|
| Home           | /                      |
| All Courses    | /courses/              |
| Admin Panel    | /admin/                |
| Register       | /users/register/       |
| Login          | /users/login/          |
| My Courses     | /my-courses/           |
| Profile        | /users/profile/        |

## 📥 Offline Strategy
- All course materials (PDFs, videos) stored locally on server
- Frontend uses Service Worker-ready structure
- Offline detection banner via JavaScript navigator.onLine
- Download buttons on every lesson for PDF/video

## 🗄️ Database Schema
- **Category**: Course categories with emoji icons
- **Course**: Full course with level, language, instructor
- **Lesson**: Text content + video + PDF per lesson
- **Enrollment**: Student-course enrollment with progress
- **LessonProgress**: Per-lesson completion tracking
- **Quiz / Question**: MCQ quizzes with 4 options
- **Profile**: Extended user profile with location data
- **Announcement**: Site-wide announcements

## 🚀 Production Deployment
```bash
# Install production requirements
pip install django gunicorn whitenoise pillow

# Add to settings.py
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATIC_ROOT = BASE_DIR / 'staticfiles'
DEBUG = False

# Collect static files
python manage.py collectstatic

# Run with gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

Made with ❤️ for rural India by Mountain Coders
