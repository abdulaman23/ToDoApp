# To-Do List API

A **RESTful To-Do List API** built with **Django REST Framework**, featuring **JWT authentication**, **CustomUser model**, **task CRUD**, **Redis caching**, and **Celery background reminders**. Designed as a **production-ready backend project** for learning and portfolio purposes.

---

## Features

* **User authentication & registration** (JWT)
* **Custom User model** (`AUTH_USER_MODEL`)
* **CRUD operations** for tasks (create, read, update, delete)
* **Task reminders** using **Celery**
* **Caching frequently accessed tasks** using **Redis**
* **Filtering, pagination, and ordering** for task lists
* **Unit testing** for API endpoints
* **Production-ready structure** (modular apps, DRF, async tasks)

---

## Tech Stack

* **Backend:** Python 3, Django, Django REST Framework
* **Authentication:** JWT (djangorestframework-simplejwt)
* **Database:** PostgreSQL / MySQL
* **Caching:** Redis
* **Async Tasks:** Celery (with Redis broker)
* **Testing:** Django REST Framework APITestCase
* **Optional Dev Tools:** Docker, docker-compose, Swagger/OpenAPI

---

## Project Structure

```
todo_project/
│
├─ todo_project/          # Project configuration
│   ├─ settings.py        # DB, cache, JWT, Celery configs
│   ├─ urls.py            # Project URL routes
│   ├─ celery.py          # Celery setup
│
├─ users/                 # User authentication module
│   ├─ models.py          # CustomUser model
│   ├─ serializers.py     # User registration serializer
│   ├─ views.py           # Registration view
│   ├─ urls.py            # /register/, /login/, /token/refresh/
│
├─ tasks/                 # Task management module
│   ├─ models.py          # Task model
│   ├─ serializers.py     # Task CRUD serializer
│   ├─ views.py           # TaskViewSet
│   ├─ urls.py            # Task API routes
│   ├─ tasks.py           # Celery background tasks
│   ├─ tests.py           # Unit tests for tasks
│
├─ requirements.txt       # Python dependencies
└─ manage.py
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/todo-project.git
cd todo-project
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure database

Update `settings.py` with PostgreSQL or MySQL credentials.

### 5. Run migrations

```bash
python manage.py makemigrations users tasks
python manage.py migrate
```

### 6. Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Start Redis

* Local installation: `redis-server`
* Docker: `docker run -d --name redis -p 6379:6379 redis`

### 8. Start Celery worker

```bash
celery -A todo_project worker -l info
# For periodic tasks
celery -A todo_project beat -l info
```

### 9. Run Django server

```bash
python manage.py runserver
```

---

## API Endpoints

### Users

| Method | Endpoint                    | Description       |
| ------ | --------------------------- | ----------------- |
| POST   | `/api/users/register/`      | User registration |
| POST   | `/api/users/login/`         | Obtain JWT token  |
| POST   | `/api/users/token/refresh/` | Refresh JWT token |

### Tasks

| Method | Endpoint           | Description                       |
| ------ | ------------------ | --------------------------------- |
| GET    | `/api/tasks/`      | List all tasks for logged-in user |
| POST   | `/api/tasks/`      | Create a new task                 |
| GET    | `/api/tasks/<id>/` | Retrieve a specific task          |
| PUT    | `/api/tasks/<id>/` | Update a task                     |
| DELETE | `/api/tasks/<id>/` | Delete a task                     |

---

## Testing

```bash
python manage.py test users
python manage.py test tasks
```

* Unit tests cover **user registration, login, and task CRUD endpoints**.

---

## Future Improvements / Stretch Goals

* Add **task deadlines & notifications via email/SMS**
* Add **task priority and categories**
* Implement **Swagger/OpenAPI** documentation
* Dockerize project for **production-ready deployment**
* Add **role-based permissions** for collaborative tasks

---

## License

This project is **MIT licensed** – feel free to use it for learning or portfolio purposes.
