#  Codrix Premium+ — Django Agency Website

**Codrix Premium+** is a modern, full-stack Django web application designed for creative agencies, freelancers, or developers to showcase their services, portfolio, careers, and client contact options.  
This version was developed as part of a Codrix Solutions practical evaluation, demonstrating advanced Django, TailwindCSS, and UI/UX integration skills.

---

## Features

###  Front-End
- **Responsive premium design** (TailwindCSS + Alpine.js)
- **Animated hero section** with gradients and smooth scrolling
- **Dark / light mode toggle**
- **Glassmorphism navbar and cards**
- **Dynamic portfolio grid** with category filters and hover overlays
- **Career listings** with CV upload functionality
- **Contact form** (saves to DB and sends emails)
- **Testimonials, services, and team sections**
- **SEO-friendly meta tags and Open Graph**

###  Back-End
- Django 5.x, Python 3.13
- Modular apps: `pages`, `portfolio`, `careers`, `contact`
- Models for Projects, Jobs, Job Applications, Inquiries
- File uploads with media management
- Admin panel completely restyled and branded as **“Codrix Admin Panel”**
- Automatic demo data seeding (`seed_demo` command)

###  Admin
- Custom dark theme
- Dashboard showing key models
- Manage projects, jobs, applications, and contacts
- Upload images, edit content directly from the backend

---

##  Project Structure
codrix_premium_plus/
│
├── core/ # Main project config
├── pages/ # Home, About, Services
├── portfolio/ # Portfolio models & views
├── careers/ # Jobs & applications
├── contact/ # Contact form + email handler
├── static/ # CSS, JS, images, logo
├── templates/ # HTML templates
├── manage.py
└── requirements.txt


---

##  Technology Stack

| Layer | Technology |
|-------|-------------|
| **Framework** | Django 5.x |
| **Styling** | TailwindCSS v3, Alpine.js, AOS animations |
| **Database** | SQLite (local) / PostgreSQL (production) |
| **Deployment** | Render / Railway / PythonAnywhere |
| **Server** | Gunicorn + WhiteNoise |
| **Language** | Python 3.13 |

---

##  Quick Start (Local)

```bash
# 1 Create virtual environment
python -m venv webpro
webpro\Scripts\activate        # Windows
# source webpro/bin/activate   # macOS/Linux

# 2 Install dependencies
pip install -r requirements.txt

# 3 Database setup
python manage.py migrate
python manage.py createsuperuser

# 4 (Optional) Seed demo content
python manage.py seed_demo

# 5 Run the server
python manage.py runserver

Then open http://127.0.0.1:8000

Admin panel → http://127.0.0.1:8000/admin


* Email Configuration

By default, contact form messages print to the console.

To enable SMTP, edit your .env file:

DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost,yourdomain.com
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.yourhost.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=you@domain.com
EMAIL_HOST_PASSWORD=yourpassword
DEFAULT_FROM_EMAIL=Codrix <noreply@domain.com>
CONTACT_TO_EMAIL=hello@domain.com



Author

Aziz Ahmad
Full-Stack Developer | AI & Web Engineer
GitHub: @azizahmad7751

Email: contact.azizahmad7751@gmail.com
