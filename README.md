# Question_paper_2_mushakar  

A lightweight Django application for creating, managing, and distributing examination papers.  
The project demonstrates a clean architecture with a dedicated `QuestionPaper` configuration package and a functional `QuestionPaperapp` that handles models, forms, views, and admin integration.

---

## Overview  

`Question_paper_2_mushakar` provides a simple web interface for:

* Defining courses, students, and exam papers.  
* Uploading course‑related images (e.g., syllabus scans).  
* Generating printable PDFs of question papers.  
* Managing student roles and enrollment data.

The repository is structured as a standard Django project, making it easy to extend or integrate into larger educational platforms.

---

## Features  

| ✅ | Feature |
|---|---------|
| ✅ | **Course & Student Management** – CRUD operations via Django admin. |
| ✅ | **Exam Paper Creation** – Associate multiple papers with students and courses. |
| ✅ | **File Uploads** – Store course pictures and paper attachments. |
| ✅ | **Role‑Based Access** – Student, teacher, and admin roles. |
| ✅ | **Database Migrations** – Fully versioned with 10 migration files. |
| ✅ | **Ready for Production** – ASGI/WSGI entry points included. |

---

## Tech Stack  

| Layer | Technology |
|-------|------------|
| **Framework** | Django 4.x (Python 3.9+) |
| **Database** | SQLite (default) – can be swapped for PostgreSQL, MySQL, etc. |
| **Frontend** | Django templates (Bootstrap optional) |
| **Deployment** | ASGI (`asgi.py`) & WSGI (`wsgi.py`) ready |
| **Version Control** | Git (GitHub) |

---

## Installation  

> **Prerequisites**  
> - Python 3.9 or newer  
> - Git  

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/Question_paper_2_mushakar.git
cd Question_paper_2_mushakar

# 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt   # (Create this file if not present)
# If requirements.txt is missing, install Django directly:
pip install Django==4.*

# 4️⃣ Apply migrations
python manage.py migrate

# 5️⃣ Create a superuser (admin access)
python manage.py createsuperuser
```

> **Optional** – If you prefer a different database, update `QuestionPaper/settings.py` accordingly and run `python manage.py migrate` again.

---

## Usage  

```bash
# Run the development server
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

* **Admin panel:** `http://127.0.0.1:8000/admin/` – log in with the superuser credentials.  
* **App URLs:** The main application is mounted at the root (`QuestionPaper/urls.py`). Adjust routing in `QuestionPaper/urls.py` if you need a custom prefix.

### Common commands

| Command | Description |
|---------|-------------|
| `python manage.py makemigrations` | Create new migration files after model changes. |
| `python manage.py collectstatic` | Gather static files for production. |
| `python manage.py test` | Run the test suite (add tests as needed). |
| `python manage.py loaddata <fixture>` | Load initial data fixtures. |

---

## License  

This project is licensed under the **MIT License**. See the `LICENSE` file for