from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional, List
from time import time
from fastapi.middleware.cors import CORSMiddleware

# Define the Todo models
class Todo(BaseModel):
    id: Optional[int] = None
    task: str
    is_completed: bool = False

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# In-memory storage for todos
todos = []

# Middleware to log request processing time
@app.middleware("http")
async def log_middleware(request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    print(f"Request: {request.method} {request.url.path} processed in {process_time:.4f} seconds")
    return response

# Simulate sending an email notification
async def send_email(todo: Todo):
    print(f"Email notification for Todo {todo.id} sent.")

# Endpoint to add a new todo
@app.post("/todos", response_model=Todo)
async def add_todos(todo: Todo, background_tasks: BackgroundTasks):
    # Generate a unique ID for the todo
    todo.id = len(todos) + 1
    # Append the todo as a dictionary for serialization
    todos.append(todo.dict())
    # Add email notification to background tasks
    background_tasks.add_task(send_email, todo)
    return todo

# Endpoint to retrieve all todos
@app.get("/todos", response_model=List[Todo])
async def read_todos(completed: Optional[bool] = None):
    if completed is None:
        return todos
    else:
        return [todo for todo in todos if todo["is_completed"] == completed]

# Endpoint to retrieve a specific todo by ID
@app.get("/todos/{id}", response_model=Todo)
async def read_todo(id: int):
    for todo in todos:
        if todo["id"] == id:
            return todo
    raise HTTPException(status_code=404, detail="Item not found")

# Endpoint to update a specific todo by ID
@app.put("/todos/{id}", response_model=Todo)
async def update_todo(id: int, new_todo: Todo):
    for index, todo in enumerate(todos):
        if todo["id"] == id:
            new_todo.id = id
            todos[index] = new_todo.dict()
            return new_todo
    raise HTTPException(status_code=404, detail="Item not found")

# Endpoint to delete a specific todo by ID
@app.delete("/todos/{id}")
async def delete_todo(id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == id:
            del todos[index]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")