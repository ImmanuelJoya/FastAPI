# 📋 Todo Application (FastAPI)

This is a simple **Todo Application** built using **FastAPI**, a modern, fast (high-performance) web framework for building APIs with Python 3.7+.

The application allows users to manage a list of tasks (todos) via RESTful API endpoints. It supports creating, reading, updating, and deleting todos, as well as filtering completed or incomplete tasks. Additionally, it includes CORS support, background task processing (e.g., email notifications), and request logging middleware.

---

## 🚀 Features

- **CRUD Operations**: Create, Read, Update, and Delete todos.
- **Filtering**: Retrieve all todos or filter by completion status (`completed=True/False`).
- **Background Tasks**: Simulates sending email notifications asynchronously when a new todo is added.
- **CORS Support**: Allows cross-origin requests from any domain (`*`).
- **Request Logging Middleware**: Logs the processing time for each request.
- **In-Memory Storage**: Todos are stored in memory (no database required).

---

## 📦 Installation and Setup

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)
- `uvicorn` (ASGI server for running FastAPI)

### Steps to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/todo-fastapi.git
