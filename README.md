# Task API

A small FastAPI task API backed by SQLite. The app exposes basic task management endpoints and stores records in a local `tasks.db` file.

## What it does

- Starts a FastAPI application with automatic docs
- Creates a SQLite `tasks` table on startup if it does not already exist
- Supports creating, listing, updating, and deleting tasks
- Returns simple JSON responses for the root and health endpoints

## Tech Stack

- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn

## Getting Started

### Install dependencies

```bash
pip install fastapi uvicorn
```

### Run the app

```bash
uvicorn main:app --reload
```

By default the app runs at `http://localhost:8000`.

### Open the docs

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| GET | `/` | Basic API information | 200 |
| GET | `/Health` | Health check | 200 |
| GET | `/tasks` | List all tasks from SQLite | 200 |
| GET | `/tasks/{id}` | Get a task by ID | 200 |
| POST | `/tasks` | Create a new task | 201 |
| PUT | `/tasks/{id}` | Update an existing task | 200 |
| DELETE | `/tasks/{id}` | Delete a task | 204 |

## Task Model

Stored rows use this shape:

```json
{
  "id": 1,
  "title": "Buy milk",
  "done": false
}
```

| Field | Type | Notes |
|-------|------|-------|
| `id` | integer | Assigned by the server |
| `title` | string | Required and cannot be empty |
| `done` | boolean | Defaults to `false` |

## Examples

List all tasks:

```bash
curl http://localhost:8000/tasks
```

Create a task:

```bash
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk"}'
```

Update a task:

```bash
curl -i -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy rasgulla and milk", "done": true}'
```

Delete a task:

```bash
curl -i -X DELETE http://localhost:8000/tasks/1
```

## Project Structure

```text
.
├── main.py
├── README.md
└── tasks.db
```

## Notes

- The database file is local to the project and persists between runs.
- Task IDs are generated in code using `randrange`, so they are not sequential.
- The current `GET /tasks/{id}` handler still references a sample in-memory list in the code and should be fixed to read from SQLite for that endpoint to work correctly.