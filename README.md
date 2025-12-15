# 📝 Todo List (Django)

Simple Todo List application built with Django and Bootstrap.

## 🚀 Features

- Create, update, delete tasks
- Mark tasks as completed / undone
- Assign multiple tags to tasks
- Create, update, delete tags
- Tasks are ordered:
  - not done → done
  - newest → oldest
- Sidebar navigation on all pages
- Responsive UI using Bootstrap

## 🧱 Tech Stack

- Python
- Django
- SQLite (development)
- Bootstrap 5
- Class-Based Views (CBV)

## 📂 Project Structure

- `todo_list/` – main app
- `templates/` – HTML templates
- `static/` – static files
- `db.sqlite3` – local database (ignored in git)

## 🖥 Pages

- Home page (`/`) – task list
- Create / Update / Delete task
- Complete / Undo task
- Tag list (`/tags/`)
- Create / Update / Delete tag

## ▶️ How to run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
