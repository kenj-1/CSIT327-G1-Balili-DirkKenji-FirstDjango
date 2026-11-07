# AGENT_CONTEXT.md — Balili_CampusConnect

Persistent project memory, architecture map, and phase-by-phase changelog for **CampusConnect** (`CSIT327` Lab Challenge).

---

## Current Project Status

### Phase Progress
- [x] **Phase 1: Audit, `.gitignore`, & `AGENT_CONTEXT.md` Initialization**
- [x] **Phase 2: Base Template & Bootstrap 5 CDN Setup**
- [ ] **Phase 3: Sign-up Success Message & Auth Form Styling**
- [ ] **Phase 4: Secure Profile `UpdateView` & Template**
- [ ] **Phase 5: `README.md` & Final Verification**

### Lab Requirements Checklist
- [x] Comprehensive `.gitignore` (`venv/`, `.venv/`, `env/`, `__pycache__/`, `*.pyc`, `.env`, IDE configs)
- [x] Persistent `AGENT_CONTEXT.md` tracking status, architecture, and changelog
- [x] Shared `templates/base.html` loading Bootstrap 5 CSS & JS bundle via CDN
- [x] Responsive Bootstrap 5 navbar (dynamic guest vs. authenticated links)
- [x] Dismissible Bootstrap 5 alert block (`alert alert-success alert-dismissible fade show`) for Django `messages`
- [ ] Sign-up view triggers `messages.success` (or `SuccessMessageMixin`) upon registration
- [ ] All forms styled with Bootstrap 5 classes (`form-control`, `form-label`, `btn btn-primary`, `card`) via `forms.py` widget attributes
- [ ] All templates (`signup.html`, `login.html`, `profile.html`, `home.html`) extend `base.html` and include `{% csrf_token %}` on forms
- [ ] Secure Profile view using class-based `UpdateView` + `LoginRequiredMixin`
- [ ] `get_object(self, queryset=None)` overridden to return `self.request.user` (preventing unauthorized profile access via URL manipulation)
- [ ] `README.md` formatted for `CSIT327` (Student Name: Dirk Kenji Balili, Section placeholder, feature overview, setup steps)

---

## Architecture & File Map

### Project Overview
- **Framework:** Django 6.1.2 (`python manage.py`)
- **Custom User Model:** `accounts.CustomUser` (extends `AbstractUser` with `role` (`STUDENT`, `INSTRUCTOR`, `ADMIN`) and `course` fields)
- **Auth Redirects:** `LOGIN_REDIRECT_URL = 'dashboard'`, `LOGOUT_REDIRECT_URL = 'login'`

### Directory & File Structure
```text
Balili_CampusConnect/
├── manage.py
├── .gitignore
├── AGENT_CONTEXT.md
├── campusconnect/              # Project configuration package
│   ├── settings.py             # Installed apps, templates dir, AUTH_USER_MODEL, redirects
│   ├── urls.py                 # Root URL routing (admin/, accounts/, dashboard)
│   ├── wsgi.py
│   └── asgi.py
├── accounts/                   # Authentication & CustomUser app
│   ├── models.py               # CustomUser model (role, course)
│   ├── forms.py                # CustomUserCreationForm (to be styled in Phase 3)
│   ├── views.py                # SignUpView (CreateView)
│   ├── urls.py                 # /accounts/signup/
│   └── admin.py                # CustomUserAdmin
├── dashboard/                  # Core dashboard & user-facing pages
│   ├── models.py
│   ├── views.py                # DashboardView (LoginRequiredMixin), AdminPanelView (UserPassesTestMixin)
│   └── urls.py                 # / (dashboard), /admin-panel/
└── templates/                  # Global templates directory
    ├── base.html               # Bootstrap 5 CDN layout, responsive navbar, dismissible messages alert
    ├── registration/
    │   ├── login.html          # Login form template (to be styled in Phase 3)
    │   └── signup.html         # Sign-up form template (to be styled in Phase 3)
    └── dashboard/
        ├── home.html           # Authenticated user dashboard
        └── admin_panel.html    # Admin-only panel
```

---

## Changelog

### [2026-11-07 19:25] — Phase 2: Base Template & Bootstrap 5 CDN Setup
- **Files Modified:**
  - `templates/base.html`
  - `AGENT_CONTEXT.md`
- **Technical Summary:**
  - Integrated Bootstrap 5.3.3 CSS and JS bundle strictly via jsDelivr CDN in `templates/base.html`.
  - Built a responsive Bootstrap 5 navigation bar (`navbar-expand-lg navbar-dark bg-primary`) with dynamic links: displays `Log in` and `Sign up` for guests, and greeting, `Dashboard`, `Profile`, and `Log out` (POST form with `{% csrf_token %}`) for authenticated users.
  - Added a Django `messages` loop rendering dismissible Bootstrap 5 alerts (`alert alert-success alert-dismissible fade show`) with a close button (`data-bs-dismiss="alert"`).

### [2026-11-07 19:14] — Phase 1: Audit, `.gitignore`, & `AGENT_CONTEXT.md` Initialization
- **Files Created/Modified:**
  - `.gitignore` (Created)
  - `AGENT_CONTEXT.md` (Created)
- **Technical Summary:**
  - Audited existing project configuration (`campusconnect/settings.py`, `campusconnect/urls.py`), apps (`accounts`, `dashboard`), models (`CustomUser`), views, forms, and templates.
  - Restored repository working tree to the baseline unstyled commit (`2e20c81`) so each phase can be committed cleanly and incrementally.
  - Added a comprehensive `.gitignore` excluding virtual environments (`venv/`, `.venv/`, `env/`), Python bytecode (`__pycache__/`, `*.pyc`), `.env` files, and IDE configurations.
  - Initialized `AGENT_CONTEXT.md` with project status checklist, architecture map, audit findings, and changelog.
