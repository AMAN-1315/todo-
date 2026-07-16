# Task API

A simple in-memory Task/Todo List API built with **FastAPI**. Supports full CRUD (Create, Read, Update, Delete) on tasks, with basic input validation and proper HTTP status codes.

Built as a learning project to practice REST API design principles — status codes, validation, and resource-based routing.

---

## Features

- List all tasks
- Get a single task by ID
- Create a new task (with validation)
- Update an existing task's title/done status
- Delete a task
- Health check endpoint
- In-memory storage (no database required — great for learning/testing)

---

## Tech Stack

- **Python 3.10+**
- **FastAPI** — web framework
- **Pydantic** — request/response validation
- **Uvicorn** — ASGI server

---

## Getting Started

### 1. Install dependencies

```bash
pip install fastapi uvicorn
```

### 2. Run the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000` (FastAPI's default port) — adjust the URL below if you're running it elsewhere (e.g. `--port 3000`).

### 3. Explore the API

FastAPI automatically generates interactive docs:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## API Endpoints

| Method | Endpoint | Description | Success Status |
|--------|----------|-------------|-----------------|
| GET | `/` | API info | 200 |
| GET | `/Health` | Health check | 200 |
| GET | `/tasks` | List all tasks | 200 |
| GET | `/tasks/{id}` | Get a single task by ID | 200 |
| POST | `/tasks` | Create a new task | 201 |
| PUT | `/tasks/{id}` | Update a task by ID | 200 |
| DELETE | `/tasks/{id}` | Delete a task by ID | 204 |

---

## Task Object

```json
{
  "id": 1,
  "title": "Buy milk",
  "done": false
}
```

| Field | Type | Notes |
|-------|------|-------|
| `id` | integer | Assigned by the server, read-only |
| `title` | string | Required, cannot be empty |
| `done` | boolean | Defaults to `false` |

---

## Examples

### List all tasks

```bash
curl http://localhost:8000/tasks
```

### Get a task by ID

```bash
curl http://localhost:8000/tasks/1
```

Returns `404` if the ID doesn't exist.

### Create a task

```bash
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk"}'
```

Returns `201` with the created task (server assigns the `id`, sets `done` to `false`).

Posting an empty or missing title:

```bash
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{}'
```

Returns `400 Bad Request`.

### Update a task

```bash
curl -i -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy rasgulla and milk", "done": true}'
```

Returns `200` with the updated task, `404` if the task doesn't exist, `400` if the title is empty.

### Delete a task

```bash
curl -i -X DELETE http://localhost:8000/tasks/1
```

Returns `204 No Content` on success, `404` if the task doesn't exist.

---

## Validation Rules

- `title` is required and cannot be empty — the server never trusts the client. Missing or blank titles return `400 Bad Request`.
- `id` is always assigned by the server, never accepted from the client.
- Requests for a non-existent task ID return `404 Not Found`.

---

## Project Structure

```
.
├── main.py       # All routes and logic
└── README.md
```

---

## Known Limitations / Notes

- **In-memory storage:** tasks reset every time the server restarts — no database is used.
- **IDs:** currently generated with `random.randrange`, which works for a demo but doesn't guarantee no collisions at scale. A production version should derive the next ID from the existing list (e.g. `max(existing ids) + 1`) or use a database's auto-increment/UUID.
- **No authentication:** the API is fully open; anyone can create, update, or delete tasks.
- **No persistence across restarts.**

---

## Possible Future Improvements

- Swap in-memory list for a real database (SQLite/Postgres via SQLAlchemy)
- Add pagination and filtering (e.g. `?done=true`) to `GET /tasks`
- Add authentication (API keys or OAuth2)
- Add automated tests (pytest + FastAPI's TestClient)
- Add PATCH endpoint for partial updates