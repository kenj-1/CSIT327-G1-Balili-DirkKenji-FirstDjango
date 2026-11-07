# CampusConnect (`Balili_CampusConnect`)

**Course:** CSIT327 — Application Development and Emerging Technologies  
**Student Name:** Dirk Kenji Balili  
**Section:** G1  

---

## Project Overview

**CampusConnect** is a role-based Django web application built for **CSIT327**. It provides student and administrator authentication, a personalized member dashboard, a secure profile management system, real-time feedback alerts, and a responsive UI styled with **Bootstrap 5 (via CDN)**.

---

## Key Features

1. **Custom User & Role Management (`accounts.CustomUser`)**
   - Extends Django's `AbstractUser` with academic fields (`role`: Student, Instructor, Administrator; and `course`).
   - Role-aware dashboard with restricted Admin Panel access (`UserPassesTestMixin`).

2. **Secure Profile View & Editing (`UpdateView` + `LoginRequiredMixin`)**
   - Implemented using Django's class-based `UpdateView` combined with `LoginRequiredMixin`.
   - **Security Lock:** Overrides `get_object(self, queryset=None)` to return `self.request.user`, ensuring authenticated users can only view and modify their own profile (`/profile/`) and preventing unauthorized access via URL manipulation.
   - All POST forms enforce CSRF protection (`{% csrf_token %}`).

3. **Real-Time User Feedback (`django.contrib.messages`)**
   - Triggers a success notification immediately upon user registration on the Sign-up page (`messages.success`) and when saving profile updates.
   - Renders messages in `base.html` using dismissible Bootstrap 5 alerts (`alert alert-success alert-dismissible fade show`).

4. **Bootstrap 5 UI & Form Styling (via CDN)**
   - Loads Bootstrap 5.3 CSS and JS bundle strictly via CDN in `templates/base.html`.
   - Includes a responsive navigation bar that dynamically displays **Log in / Sign up** links for guests and **Dashboard / Profile / Log out** actions for authenticated users.
   - All forms (`CustomUserCreationForm`, `CustomAuthenticationForm`, `ProfileUpdateForm`) override widget attributes in `accounts/forms.py` with `attrs={'class': 'form-control'}` and are rendered inside clean Bootstrap 5 cards.

---

## Project Structure

```text
Balili_CampusConnect/
├── manage.py
├── README.md
├── AGENT_CONTEXT.md
├── .gitignore
├── campusconnect/              # Project settings & root URL configuration
│   ├── settings.py
│   └── urls.py
├── accounts/                   # Authentication, CustomUser model, & styled forms
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── dashboard/                  # Dashboard, Admin Panel, & Secure Profile UpdateView
│   ├── views.py
│   └── urls.py
└── templates/                  # Shared base layout & app templates
    ├── base.html
    ├── registration/
    │   ├── login.html
    │   └── signup.html
    └── dashboard/
        ├── home.html
        ├── profile.html
        └── admin_panel.html
```

---

## Step-by-Step Setup & Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/kenj-1/Balili_CampusConnect.git
cd Balili_CampusConnect
```

### 2. Create and Activate a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

*(Optional) Create a Superuser for the Django Admin & Admin Panel:*
```bash
python manage.py createsuperuser
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
- **Dashboard / Home:** `http://127.0.0.1:8000/`
- **Sign Up:** `http://127.0.0.1:8000/accounts/signup/`
- **Log In:** `http://127.0.0.1:8000/accounts/login/`
- **My Profile:** `http://127.0.0.1:8000/profile/`
