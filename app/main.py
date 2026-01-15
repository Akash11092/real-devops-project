from fastapi import FastAPI

app = FastAPI(title="Real DevOps Project")

tasks = []

@app.get("/")
def home():
    return {"message": "Real DevOps project is running successfully"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added", "tasks": tasks}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}
