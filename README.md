# Todo API

A minimal RESTful API for managing a todo list. Built with FastAPI and designed to be simple to run and extend.

**Features**
- **Create, read, update, delete** todos
- Simple JSON API with predictable request/response shapes
- Lightweight and easy to run with `uvicorn`

**Tech stack**
- Python 3.10+
- FastAPI
- Uvicorn (ASGI server)

**Quick Start**

1. Create a virtual environment and install dependencies (if you have a `requirements.txt`):

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the API with Uvicorn (development mode):

```
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000` and automatic docs at `http://127.0.0.1:8000/docs`.

**API Endpoints**

- `GET /todos` — List all todos
- `GET /todos/{id}` — Get a todo by ID
- `POST /todos` — Create a new todo
- `PUT /todos/{id}` — Replace an existing todo
- `PATCH /todos/{id}` — Partially update a todo
- `DELETE /todos/{id}` — Delete a todo

All request and response bodies are JSON.

**Data model**

Example todo object:

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "created_at": "2026-07-16T12:00:00Z",
  "updated_at": "2026-07-16T12:00:00Z"
}
```

**Examples**

Create a todo:

```bash
curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs"}'
```

List todos:

```bash
curl http://127.0.0.1:8000/todos
```

Update a todo:

```bash
curl -X PUT http://127.0.0.1:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries and snacks", "description": "Milk, eggs, chips", "completed": false}'
```

Delete a todo:

```bash
curl -X DELETE http://127.0.0.1:8000/todos/1
```

**Configuration**

- By default the app binds to `127.0.0.1:8000`. To change host/port, pass `--host` and `--port` to `uvicorn` or use your preferred deployment configuration.

**Testing**

If you have tests (pytest), run:

```
pytest
```

**Extending**

- Add authentication (JWT, OAuth) for private lists
- Persist todos to a database (SQLite, PostgreSQL) via SQLModel/SQLAlchemy
- Add filtering, sorting, and paging to `GET /todos`

**Files**
- The application entrypoint is `main.py`.

**License**

This project is provided as-is. Add a LICENSE file if you need an explicit license.
